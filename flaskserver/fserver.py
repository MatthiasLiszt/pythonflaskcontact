from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def landingPage():
    return render_template('landing.html')

@app.route('/sendMessage', methods=['GET'])
def sendMessage():
    if request.method == 'GET':
       subject = request.args.get('subject', '')
       msg='Message with the subject - '+subject+' - has been sent'
       return msg

    
