import os
import sys
import json
import random
import requests
import time
from flask import Flask, request

#define our flask app
app = Flask(__name__)

#Method will automatically execute when our endpoint receives a POST call
@app.route('/', methods=['POST'])
def msg_received_from_group():

  #Format the data we receive as a JSON
  data = request.get_json()
  log('{}'.format(data))
  
  #Check the text of the message sent to the chat to see if it matches our command word
  if data['text'] == "w-2" or "w2" or "w2 forms" or "w-2 forms" or "W2" or "W-2":
    send_msg("A form you receive from your employer before the end of January that includes necessary information to file your taxes, such as wages, tips earned, medicare taxes, etc.If you haven’t received your W-2 form from your employer by February 15th, ask your employer to send you your W-2 form, if they refuse, the IRS will then tell the employer to send the W-2 form within 10 days or face penalties. Be sure to provide the IRS an estimate of your income as well as dates worked and rate of pay. The IRS also allows an employee who cannot get the W-2 from his employer to send in the substitute Form 4852")


  return "ok", 200

 
#Sends a message to the chat that the bot originates from
def send_msg(msg):

  url  = 'https://api.groupme.com/v3/bots/post'
  
  data ={
  'bot_id' : os.getenv('GROUPME_BOT_ID'),
  'text'   : msg
  }
        
  request = requests.post(url=url, data=data)

#sends a picture and a message to the chat
#Picture URL must be registered with GroupMe first
def send_msg_pic(msg, picURL):

  url  = 'https://api.groupme.com/v3/bots/post'

  data ={
  'bot_id' : os.getenv('GROUPME_BOT_ID'),
  'text'   : msg,
  "attachments" : [
    {
      "type"  : "image",
      "url"   : picURL
    }
  ],
  'picture_url': picURL
  }

  request = requests.post(url=url, data=data)


#logging function to help debug
def log(msg):
  print(str(msg))
  sys.stdout.flush()
