from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = '**************'
app.config['MAIL_PASSWORD'] = '***********'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/")
def index():
  msg = Message('aqui probando el mail de flask', sender = '*************', recipients = ['**************'])
  msg.body = "Aqui probando el mail con flask"
  mail.send(msg)
  return "mensaje enviado"

if __name__ == '__main__':
   app.run(debug = True)