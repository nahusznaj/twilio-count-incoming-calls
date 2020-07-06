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

This will install Twilio's [helper library for Python](https://www.twilio.com/docs/libraries/python), and `python-dotenv`. The latter library will help us with the environment variables for the script.

Once the install is complete, let's set up the environment variables.

Ah, you would need a Twilio account for this! If you don't have one, create one with this [referral link](www.twilio.com/referral/yrF7VV).

Now, from your Twilio console, copy the following:

- Account SID, which is shown in https://twilio.com/console, 
- AuthToken, which is shown in https://twilio.com/console, and

- Twilio number that you want to count the incoming calls. Your incoming phone numbers are in https://www.twilio.com/console/phone-numbers/incoming. This is optional! Just make sure the phone number you pass, is a number owned by the AccountSID used above.

Once you have your authentication details to consume Twilio's APIs and the phone number you want to work with, you can populate the file.

To this, first, copy the template into a `.env`:

```
$ cp .env.template .env
```

Then, edit the `.env`, you can do this with from the terminal with `nano .env`.

Once you saved, with `command X` and confirm with `Y`, you need to source environmental varialbes, so

```
$ source .env
```

That's it.

Now, in the terminal, run

```
$ python3 voice_call_logs.py
```

You'll be prompted to input the details and then you'll see the outcome with the count of calls. The expected timezone is CEST, the timezone of Central Europe in the Summer, which is 2 hours away from GMT. GMT is the timezone used (see the optional time properties, `start_time` and `end_time` in [Twilio docs](https://www.twilio.com/docs/voice/api/call-resource#read-multiple-call-resources)) and that's why I added a delta of 2 hours to adjust this.

In my case, when I run the script I did:

```
(calls-venv) ~ $ python3 voice_call_logs.py
Pass your start hour in CEST: 3
Pass your start day (date number): 1
Pass your start month: 1
Pass your end hour in CEST: 5
Pass your end day (date number): 5
Pass your end month: 7
Pass the Twilio number to count the calls made to it: +redacted
Total count of calls made to +redacted from 03 hs, 01-01-2020 to 05 hs, 05-07-2020  is: 71
```

In this case, I didn't use the environmental variable! I will include this in future versions of this script.

I've now added also a CSV writer. The idea is to add a new row with the Twilio number, the start time, the end time, and the number of incoming calls.

To do:

- enter a date range loop through, to create a week days report, and a weekend report.
- include logic to try/catch whether the day is a weekend day or week day. Depending on what day it is, pass different hours. The idea is to be able to either pass a 7 days range, or "7 days prior to now", and count for weekend days in an hour range, and for another time of the day for week days.
- Perhaps: embed this in a Flask application so that a user can navigate to a website, pass AccountSID, API Key and Secret, and phone number. There are security risks obviously involved, in sharing API Keys and Secret, so I'd need a way to ensure they are deleted as soon as the script is run and they are not stored anywhere else in the application.
