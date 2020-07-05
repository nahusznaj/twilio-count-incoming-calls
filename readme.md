This script will be useful to obtain details of incoming voice calls made to your Twilio number in a given time range.

The idea is to count how many calls were made to your Twilio number using the [Call resource](https://www.twilio.com/docs/voice/api/call-resource) from Twilio's Programmable Voice API.

In particular, this script is a modification of [Read multiple Call resources and filter by a period of time](https://www.twilio.com/docs/voice/api/call-resource?code-sample=code-read-multiple-call-resources-and-filter-by-a-period-of-time&code-language=Python&code-sdk-version=6.x).

I'll be using the optional properties documented in the API definitoins to [read multiple call resources](https://www.twilio.com/docs/voice/api/call-resource?code-sample=code-read-multiple-call-resources-and-filter-by-a-period-of-time&code-language=Python&code-sdk-version=6.x#read-multiple-call-resources).

Let's crack on.

# Steps to use this script

Create a folder, open a terminal and navigate to the folder.

Create a virtual environment, in my case, as you see in this repository, I called it calls-venv: 

```
$ python3 -m venv calls-venv
```

Activate the virtual environment
```
$ source calls-venv/bin/activate
```

Install the requirements:

```
$ pip3 install -r requirements.txt
```

This should install Twilio's [helper library for Python](https://www.twilio.com/docs/libraries/python), and `python-dotenv`. The latter will help with setting up and using environment variables for the script.

Once the install is complete, populate the file `.env` with:

- Account SID, which is shown in https://twilio.com/console
- AuthToken, which is shown in https://twilio.com/console.

Also, you can pass the Twilio number that you want to count the incoming calls.

- Twilio Number. Your incoming phone numbers are in https://www.twilio.com/console/phone-numbers/incoming.

Ah, you would need a Twilio account for this! If you don't have one, open one with this [link](www.twilio.com/referral/yrF7VV).