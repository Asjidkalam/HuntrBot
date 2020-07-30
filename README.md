<h1 align="center">HuntrBot</h1>
<h4 align="center">WhatsApp bot for huntr.dev bug notification</h4>

******************

[Huntr.dev](https://www.huntr.dev/) is a platform to find and fix opensource vulnerabilities, you could login with your GitHub account, choose a program and start fixing. **HuntrBot** is a WhatsApp bot which checks for new submissions added to huntr platform.

Made using [Twilio API for Whatsapp](https://www.twilio.com/whatsapp) and [Flask framework](https://www.palletsprojects.com/p/flask/) for python, hosted on heroku.

You can either use the app hosted on Heroku(https://huntr-bot.herokuapp.com/), or clone the repo and host it somewhere else. You will need a Twilio account and an active WhatsApp sandbox for the bot to work.


### Usage:

Currently it's configured for only two functions:
* **all** - returns all the bugs/vulnerable packages currently active.
* **new** - returns only the new submission made in that current day.


### Setup:

* Connect your whatsapp to Twilio WhatsApp sandbox:
From your [Twilio Console](https://www.twilio.com/console), select [Programmable Messaging](https://www.twilio.com/console/sms/dashboard), then click on "Try it Out" and finally click on [Try WhatsApp](https://www.twilio.com/console/sms/whatsapp/learn). The WhatsApp sandbox page will show you the sandbox number assigned to your account, and a join code.

* To enable the WhatsApp sandbox for your smartphone send a WhatsApp message with the given code to the number assigned to your account. The code is going to begin with the word join, followed by a randomly generated two-word phrase. Shortly after you send the message you should receive a reply from Twilio indicating that your mobile number is connected to the sandbox and can start sending and receiving messages.

* In order to deploy the flask app to heroku, here's a article https://devcenter.heroku.com/articles/git

* After generating a public app URL, bo back to the [Twilio Console](https://www.twilio.com/console), click on [Programmable Messaging](https://www.twilio.com/console/sms/dashboard), then on Settings, and finally on [WhatsApp Sandbox Settings](https://www.twilio.com/console/sms/whatsapp/sandbox). Copy the https:// URL from the Heroku app and then paste it on the “When a message comes in” field and append `/bot` endpoint. Make sure the request method is set to HTTP Post.



_If you are running the bot locally_,
```
$ python bot.py
 * Serving Flask app "bot" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```



#### Happy Hunting!
✨🍰 
