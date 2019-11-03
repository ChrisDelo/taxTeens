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
  if data['sender_type'] == 'user':
#     if data['text'] == "w-2" or "w2" or "w2 forms" or "w-2 forms" or "W2" or "W-2":
#       send_msg("A form you receive from your employer before the end of January that includes necessary information to file your taxes, such as wages, tips earned, medicare taxes, etc.If you haven’t received your W-2 form from your employer by February 15th, ask your employer to send you your W-2 form, if they refuse, the IRS will then tell the employer to send the W-2 form within 10 days or face penalties. Be sure to provide the IRS an estimate of your income as well as dates worked and rate of pay. The IRS also allows an employee who cannot get the W-2 from his employer to send in the substitute Form 4852")
     if "w-2" in data['text']:
        send_msg_pic("A form you receive from your employer before the end of January that includes necessary information to file your taxes, such as wages, tips earned, medicare taxes, etc.If you haven’t received your W-2 form from your employer by February 15th, ask your employer to send you your W-2 form, if they refuse, the IRS will then tell the employer to send the W-2 form within 10 days or face penalties. Be sure to provide the IRS an estimate of your income as well as dates worked and rate of pay. The IRS also allows an employee who cannot get the W-2 from his employer to send in the substitute Form 4852. Here is an example of a W-2 Form", "https://giftcpas.com/wp-content/uploads/2017/12/2017_Form_W-2.png")
     elif "w2" in data['text']:
        send_msg_pic("A form you receive from your employer before the end of January that includes necessary information to file your taxes, such as wages, tips earned, medicare taxes, etc.If you haven’t received your W-2 form from your employer by February 15th, ask your employer to send you your W-2 form, if they refuse, the IRS will then tell the employer to send the W-2 form within 10 days or face penalties. Be sure to provide the IRS an estimate of your income as well as dates worked and rate of pay. The IRS also allows an employee who cannot get the W-2 from his employer to send in the substitute Form 4852 Here is an example of a W-2 Form", "https://giftcpas.com/wp-content/uploads/2017/12/2017_Form_W-2.png")
     if "joint return" in data['text'].lower():
        send_msg(" A form that allows married couples to combine their tax liability and report their income, deductions, and credits on the same joint return")
     if "claim" in data['text'].lower():
        send_msg("To claim someone or something, usually, on the tax return it is referred to claiming someone as a dependantWhen you claim someone as your dependent, it reduces the amount of your income subjected to taxYou can not claim someone as a dependent if someone already has claimed him as a dependent.")
     if "dependant" in data['text'].lower():
        send_msg("Someone who relies on your income, such as children or relatives. You can claim yourself as a dependent if you meet the qualifications so no one else can claim you as a dependent, which is called a personal exemption.")
     elif "dependent" in data['text'].lower():
        send_msg("Someone who relies on your income, such as children or relatives. You can claim yourself as a dependent if you meet the qualifications so no one else can claim you as a dependent, which is called a personal exemption.")
     if "tax withheld" in data['text'].lower():
        send_msg("Found in Box 2 of your W-2 Form, it is a percentage of your income withheld from your employer to pay the government as tax. If too much is withheld, you are entitled to a tax refund, if too little, you will receive a bill or a penalty.To find out an estimate of your federal income tax withheld, use this website provided by the IRS https://apps.irs.gov/app/tax-withholding-estimator.")
     if "unemployment compensation" in data['text'].lower():
        send_msg("Unemployment compensation is paid by the state to unemployed workers who have lost their jobs due to layoffs")
     if "taxable interest" in data['text'].lower():
        send_msg("Interest earned either through a savings account, dividends or bonds that are taxable by the IRS.")
     if "1099" in data ['text']:
         send_msg("A 1099 form reports the various types of income you may receive throughout the year other than the information provided by the w-2 form. The person or entity that pays you is responsible for filling out the appropriate 1099 tax form and sending it to you by January 31.") 
     if "earned income credit" in data['text'].lower():
        send_msg("The Federal earned income credit is a refundable tax credit for low- to moderate-income working individuals and couples, particularly those with children.")
     elif "EIC" in data['text']:
        send_msg("The Federal earned income credit is a refundable tax credit for low- to moderate-income working individuals and couples, particularly those with children.")
     elif "EITC" in data['text']:
        send_msg("The Federal earned income credit is a refundable tax credit for low- to moderate-income working individuals and couples, particularly those with children.")
     if "routing transit number" in data['text'].lower():
        send_msg("Your routing number identifies the location where your account was opened.The routing number for your bank can be found through.")
     elif "RTN" in data['text']:
        send_msg("Your routing number identifies the location where your account was opened.The routing number for your bank can be found through.")
     elif "routing number" in data['text'].lower():
        send_msg("Your routing number identifies the location where your account was opened.The routing number for your bank can be found through.")
     if "cool dude" in data['text'].lower():
        send_msg("https://www.youtube.com/watch?v=I7Tps0M-l64")
     if "routing number" in data['text'].lower():
        send_msg("Your routing number identifies the location where your account was opened.The routing number for your bank can be found through.")
     if  "preparer tax identification number" in data['text'].lower():
        send_msg("The Preparer Tax Identification Number (PTIN) is an identification number that all paid tax return preparers must use on U.S. federal tax returns or claims for refund submitted to the Internal Revenue Service (IRS)")
     elif "PTIN" in data['text']:
        send_msg("The Preparer Tax Identification Number (PTIN) is an identification number that all paid tax return preparers must use on U.S. federal tax returns or claims for refund submitted to the Internal Revenue Service (IRS)")
     if "file tax" in data['text'].lower():
        send_msg_pic("You are required to file taxes if your gross income is more than 12,000. However, if your adjusted gross income is under 66,000 you can file your taxes for free using freefile.", "https://cdn.discordapp.com/attachments/512727198570905604/640420453797593138/unknown.png")
     if "when" in data['text'].lower():
        send_msg_pic("You will need to file form 1040 by April 15 (super important)")
     if "help" in data['text'].lower(): 
        send_msg("Hi I am the Tax Teen chatbot. I can help you with your student taxes. You can ask me about w2 forms, joint claims, and much more. I would recomend you start with the 1040 IRS form. You can download it here: https://www.irs.gov/pub/irs-pdf/f1040.pdf. If you need help calculating your income tax type\"math\". Let me know if you have any questions.")
  
  
  
  
  
  
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
