from flask import Flask
from flask import request
from flask import render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def landingPage():
    return render_template('landing.html')

@app.route('/sendMessage', methods=['GET'])
def sendMessage():
    if request.method == 'GET':
       subject = request.args.get('subject', '')
       message = request.args.get('message', '')
       msg='Message with the subject - '+subject+' - has been sent'
       storeMessage(subject,message)
       return msg

def storeMessage(sbj,msg):
    db = sqlite3.connect('database')
    cursor=db.cursor()
    cursor.execute('''INSERT INTO msg(subject,message) VALUES(?,?)''', (sbj,msg))
    db.commit()
    db.close()    
