from flask import Flask, request
import requests
import json
from datetime import datetime
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

def getdiff(json1,json2):
    diff = []
    packagename1 = []
    for j in range(0,len(json1)):
        packagename1.append(json1[j]['PackageName'])
    for i in range(len(json2)):
        if json2[i]['PackageName'] not in packagename1:
            diff.append(str(json2[i]['PackageName']+' : '+json2[i]['CodebasePrimaryLanguage']+' : '+json2[i]['VulnerabilityDescription']))
    return diff

def getBounty(status):
    resp = []
    indexjson = requests.get('https://files.huntr.dev/index.json')
    indexjson.raise_for_status()
    index = indexjson.json()
    with open('huntr.json','r') as huntrjson:
        huntr = json.load(huntrjson)
    huntrjson.close()
    if(status == 'new'):
        diff = getdiff(huntr,index)
        if(len(diff) != 0):
            resp = diff
        else:
            resp = resp
    else:
        for bounties in range(len(index)):
            obj = index[bounties]
            if(status == 'all'):
                bont = str(obj['PackageName']+' : '+obj['CodebasePrimaryLanguage']+' : '+obj['VulnerabilityDescription'])
                resp.append(bont)
            elif(status == 'Python'):
                if(obj['CodebasePrimaryLanguage'] == status):
                    bont = str(obj['PackageName']+' : '+obj['CodebasePrimaryLanguage']+' : '+obj['VulnerabilityDescription'])
                    resp.append(bont)
            elif(status == 'JavaScript'):
                if(obj['CodebasePrimaryLanguage'] == status):
                    bont = str(obj['PackageName']+' : '+obj['CodebasePrimaryLanguage']+' : '+obj['VulnerabilityDescription'])
                    resp.append(bont)
            elif(status == 'Java'):
                if(obj['CodebasePrimaryLanguage'] == status):
                    bont = str(obj['PackageName']+' : '+obj['CodebasePrimaryLanguage']+' : '+obj['VulnerabilityDescription'])
                    resp.append(bont)
            elif(status == 'Ruby'):
                if(obj['CodebasePrimaryLanguage'] == status):
                    bont = str(obj['PackageName']+' : '+obj['CodebasePrimaryLanguage']+' : '+obj['VulnerabilityDescription'])
                    resp.append(bont)
            elif(status == 'PHP'):
                if(obj['CodebasePrimaryLanguage'] == status):
                    bont = str(obj['PackageName']+' : '+obj['CodebasePrimaryLanguage']+' : '+obj['VulnerabilityDescription'])
                    resp.append(bont)
            else:
                resp = resp
    with open('huntr.json','w') as huntrwjson:
        json.dump(index, huntrwjson)
    huntrwjson.close()     
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
        if(len(new_bounties) == 0):
            for i in range(len(new_bounties)):
                msg.body(new_bounties[i])
                msg.body("\n")
        else:
            msg.body("No bounties available")
        responded = True
    if 'python' in incoming_msg:
        # return all the bounties with codebase python
        new_bounties = getBounty('Python')
        if(len(new_bounties) == 0):
            for i in range(len(new_bounties)):
                msg.body(new_bounties[i])
                msg.body("\n")
        else:
            msg.body("No bounties available in this language.")
        responded = True
    if 'php' in incoming_msg:
        # return all the bounties with codebase php
        new_bounties = getBounty('PHP')
        if(len(new_bounties) == 0):
            for i in range(len(new_bounties)):
                msg.body(new_bounties[i])
                msg.body("\n")
        else:
            msg.body("No bounties available in this language.")
        responded = True
    if 'javascript' in incoming_msg:
        # return all the bounties with codebase javascript
        new_bounties = getBounty('JavaScript')
        if(len(new_bounties) == 0):
            for i in range(len(new_bounties)):
                msg.body(new_bounties[i])
                msg.body("\n")
        else:
            msg.body("No bounties available in this language.")
        responded = True
    if 'java' in incoming_msg:
        # return all the bounties with codebase javascript
        new_bounties = getBounty('Java')
        if(len(new_bounties) == 0):
            for i in range(len(new_bounties)):
                msg.body(new_bounties[i])
                msg.body("\n")
        else:
            msg.body("No bounties available in this language.")
        responded = True
    if 'ruby' in incoming_msg:
        # return all the bounties with codebase javascript
        new_bounties = getBounty('Ruby')
        if(len(new_bounties) == 0):
            for i in range(len(new_bounties)):
                msg.body(new_bounties[i])
                msg.body("\n")
        else:
            msg.body("No bounties available in this language.")
        responded = True

    if not responded:
        msg.body('Invalid Command!')
    return str(resp)


if __name__ == '__main__':
    app.run()