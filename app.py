from flask import Flask
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)



@app.route('/')
def hello_world():
       return "Hello World"


@app.route('/sms', methods=['POST'])
def sms():
        messg="Hello There"
        res = MessagingResponse()
        res.message(messg)
        return str(res)

if __name__=='__main__':
    app.run()
