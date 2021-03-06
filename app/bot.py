from flask import Flask, request
import requests
import json
from datetime import datetime
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

def getBounty(status):
    dateToday = str(datetime.today().strftime('%Y-%m-%d'))
    resp = []

    def getLanguages(obj, name):
        lang = str(obj['CodebasePrimaryLanguage'])
        if(lang == name):
            bounty = str(obj['PackageName'] + " : " + obj['CodebasePrimaryLanguage'])
            resp.append(bounty)

    response = requests.get('https://files.huntr.dev/index.json')
    response.raise_for_status()
    jsonResponse = response.json()
    for bounties in range(len(jsonResponse)):
        obj = jsonResponse[bounties]
        if(status == "new"):
            # TODO: new bounties - diff
            date = str(obj['DisclosureDate'])
            if(date == dateToday):
                bounty = str(obj['PackageName'] + " : " + obj['CodebasePrimaryLanguage'])
                resp.append(bounty)
        elif(status == "python"):
            getLanguages(obj, "Python")
        elif(status == "js" or status == "javascript"):
            getLanguages(obj, "JavaScript")
        elif(status == "ruby"):
            getLanguages(obj, "Ruby")
        elif(status == "php"):
            getLanguages(obj, "PHP")
        else:
            bounty = str(obj['PackageName'] + " : " + obj['CodebasePrimaryLanguage'])
            resp.append(bounty)       
    return resp

@app.route("/")
def home():
    return "<h1>HuntrBot</h1>"

@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    langs = ['python', 'js', 'ruby', 'php', 'javascript']

    if incoming_msg in langs:
        # return all the bounties in the specific language
        new_bounties = getBounty(incoming_msg)
        if(len(new_bounties) == 0):
            msg.body("No bounties in the requested language.")
        else:
            for i in range(len(new_bounties)):
                msg.body(new_bounties[i])
        responded = True

    if 'new' in incoming_msg:
        # check for new bounties
        new_bounties = getBounty('new')
        if(len(new_bounties) == 0):
            msg.body("No new bounties released today.")
        else:
            for i in range(len(new_bounties)):
                msg.body(new_bounties[i])
        responded = True

    if 'all' in incoming_msg:
        # return all the bounties
        new_bounties = getBounty('all')
        for i in range(len(new_bounties)):
            msg.body(new_bounties[i])
        responded = True
        
    if not responded:
        msg.body('Invalid Command!')
    return str(resp)


if __name__ == '__main__':
    app.run()