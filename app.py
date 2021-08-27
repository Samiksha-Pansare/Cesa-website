# importing libraries
from flask import Flask,redirect,url_for,request,render_template,session
from flask_mail import mail, Message
app = Flask(__name__)

@app.route('/',methods=['POST', 'GET'])
def index():
	if request.method=='POST':
		name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        fav_char = request.form['fav_char']
        rating = request.form['radio1']
        feedback = request.form['feedback']
        # print(name,email,screen_name,genre,fav_char,rating,feedback)
        if name=='' or email=='' or subject==0:
            return render_template('index.html',message='Please enter required fields')
		msg = Message(
                'Hello',
                sender ='yourId@gmail.com',
                recipients = ['reciever’sid@gmail.com']
               )
		msg.body = 'Hello Flask message sent from Flask-Mail'
		mail.send(msg)
		return render_template('index.html')
	else:
		return render_template('index.html')

@app.route('/events')
def events():
	return render_template('events.html')
	

if __name__ == '__main__':
	app.run(debug=True)