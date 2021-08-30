# importing libraries
from flask import Flask,redirect,url_for,request,render_template,session
from flask_mail import Mail, Message
# from Flask-Ext import Mail
app = Flask(__name__)
mail = Mail(app) # instantiate the mail class
   
# configuration of mail
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'feedbackcesa@gmail.com'
app.config['MAIL_PASSWORD'] = 'feedbackcesa@321'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/',methods=['POST', 'GET'])
def index():
    if request.method=='POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        if name=='' or email=='' or subject=='':
            return render_template('index.html',message='Please enter required fields')
        msg = Message(
                subject,
                sender ='yourId@gmail.com',
                recipients = ['cesa.vidyalankar@gmail.com']
               )
        msg.body = 'Name:'+ name + '\n' + 'Email: ' + email + '\n' 'Message:\n' + message
        # msg = Message(subject, sender = email, recipients = ['cesa.vidyalankar@gmail.com'])
        # msg.body = message
        mail.send(msg)
        return render_template('index.html')
    return render_template('index.html')

@app.route('/events')
def events():
	return render_template('events.html')
	

if __name__ == '__main__':
	app.run(debug=True)