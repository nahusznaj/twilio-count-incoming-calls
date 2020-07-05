from twilio.rest import Client
import os
from datetime import datetime, timedelta

account_sid = os.environ['ACCOUNT_SID']
auth_token = os.environ['AUTH_TOKEN']

client = Client(account_sid, auth_token)

startHour = input('Pass your start hour in CEST: ')
startDay = input('Pass your start day (date number): ')
startMonth = input('Pass your start month: ')

endHour = input('Pass your end hour in CEST: ')
endDay = input('Pass your end day (date number): ')
endMonth = input('Pass your end month: ')

TwilioNumber = input('Pass the Twilio number to count the calls made to it: ')

TwilioNumber = TwilioNumber.replace(' ', '')

startHour = int(startHour)
startDay = int(startDay) 
startMonth = int(startMonth)

endHour = int(endHour)
endDay = int(endDay)
endMonth = int(endMonth)

def timeRange(startHour, startDay, startMonth, endHour, endDay, endMonth):
    startTime = datetime(2020, startMonth, startDay, startHour)
    endTime = datetime(2020, endMonth, endDay, endHour)
    return(startTime, endTime)


timeRange = timeRange(startHour, startDay, startMonth, endHour, endDay, endMonth)

startTime= timeRange[0] - timedelta(hours=2)
endTime = timeRange[1] - timedelta(hours=2)

calls = client.calls.list(
                        start_time_after=startTime,
                        start_time_before=endTime,
                        to=TwilioNumber
                        )


Count = 0
for record in calls:
    Count +=1

#print(TwilioNumber)

print(f'Total count of calls made to {TwilioNumber} from {startTime.strftime("%H hs, %d-%m-%Y")} to {endTime.strftime("%H hs, %d-%m-%Y")}  is: {Count}')