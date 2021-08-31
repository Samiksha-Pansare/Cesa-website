from flask import Flask, render_template, request
from nltk import tag
from werkzeug.utils import redirect
from werkzeug.wrappers import response
import json
import numpy as np
import nltk
import pickle
from nltk.stem import WordNetLemmatizer
import tflearn
from training import model
import tensorflow
import datetime
import random

lemmatizer = WordNetLemmatizer()
with open("Intent.json") as file:
    intents = json.load(file)

words = pickle.load(open("words.pkl", "rb"))
labels = pickle.load(open("labels.pkl", "rb"))

app = Flask(__name__)
app.static_folder = 'static'

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        input = request.form['msg']
        # print(input)
        response = chat(input)
        return {"input": response}
    else:
        return render_template('index.html')

# @app.route("/get")
# def get_bot_response():
#     userText = request.args.get('msg')
#     return str(chatbot.get_response(userText))

def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]
    swds = nltk.word_tokenize(s)
    swds = [lemmatizer.lemmatize(w.lower()) for w in swds]

    for swd in swds:
        for i, w in enumerate(words):
            if w == swd:
                bag[i] = 1
    return np.array(bag)

def chat(input):
    results = model.predict([bag_of_words(input, words)])[0]
    results_index = np.argmax(results)
    tag = labels[results_index]

    if results[results_index] > 0.6:
        for tg in intents["intents"]:
            if tg["tag"] == tag:
                responses = tg["responses"]
                return random.choice(responses)
    else:
        return "I didn't get that. Please try again."


if __name__ == "__main__":

    app.run(debug=True)