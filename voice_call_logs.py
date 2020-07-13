from twilio.rest import Client
import csv

# Load .env file using:
from dotenv import load_dotenv
load_dotenv()

# Use the variable with:
import os
account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")


from datetime import datetime, timedelta

client = Client(account_sid, auth_token)

# startHour = input('Pass your start hour in CEST: ')
Day = input('Pass the date of the day you want to query (date number): ')
Day = int(Day)

Month = input('Pass your start month: ')
Month = int(Month)    

# # endHour = input('Pass your end hour in CEST: ')
# endDay = input('Pass your end day (date number): ')
# endMonth = input('Pass your end month: ')

#TwilioNumber = input('Pass the Twilio number to count the calls made to it: ')

TwilioNumber =  os.getenv("TWILIO_NUMBER")

#startHourWeekday = 
# startDay = int(startDay) 
    
# endMonth = int(endMonth)

def timeRangeFunction(startHour, startDay, startMonth, endHour, endDay, endMonth): #Twilio's expected input
    startTime = datetime(2020, startMonth, startDay, startHour)
    endTime = datetime(2020, endMonth, endDay, endHour)
    return(startTime, endTime)

weekendDay = [6,7] #for weekday property of the datetime [0 (Monday) - 7 (Sunday)]
weekDay = range(5)

dummyDatetime = datetime(2020, Month, Day)
DayOfWeek = dummyDatetime.weekday()


startHour = [8, 18]
endHour = [9, 22]
startHourWeekend = [8]
endHourWeekend = [22]

if DayOfWeek in weekDay: # count for week days hour ranges
    if len(startHour) == len(endHour):
        for idx, val in enumerate(startHour): 
            timeRanges = timeRangeFunction(startHour[idx], Day, Month, endHour[idx], Day, Month)
            
            startTime= timeRanges[0] - timedelta(hours=2)
            endTime = timeRanges[1] - timedelta(hours=2)

            calls = client.calls.list(
                                    start_time_after=startTime,
                                    start_time_before=endTime,
                                    to=TwilioNumber
                                    )

            Count = 0
            for record in calls:
                Count +=1

            file = 'call_logs_count.csv'


            with open(file, mode='a', newline='') as callsCSVfile:
                        callsCSVfilewriter = csv.writer(callsCSVfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        row = [TwilioNumber, startTime.strftime('%A'), timeRanges[0].hour, timeRanges[1].hour, Count]
                        callsCSVfilewriter.writerow(row)

            # print(TwilioNumber)

            print(f'Total count of calls made to {TwilioNumber} from {timeRanges[0].strftime("%H hs, %d-%m-%Y")} to {timeRanges[1].strftime("%H hs, %d-%m-%Y")} is: {Count}')


else: #count for weekend days hour ranges
    if len(startHourWeekend) == len(endHourWeekend):
        for idx, val in enumerate(startHourWeekend): 
            timeRanges = timeRangeFunction(startHourWeekend[idx], Day, Month, endHourWeekend[idx], Day, Month)
            
            startTime= timeRanges[0] - timedelta(hours=2)
            endTime = timeRanges[1] - timedelta(hours=2)

            calls = client.calls.list(
                                    start_time_after=startTime,
                                    start_time_before=endTime,
                                    to=TwilioNumber
                                    )

            Count = 0
            for record in calls:
                Count +=1

            file = 'call_logs_count.csv'


            with open(file, mode='a', newline='') as callsCSVfile:
                        callsCSVfilewriter = csv.writer(callsCSVfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        row = [TwilioNumber, startTime.strftime('%A'), timeRanges[0].hour, timeRanges[1].hour, Count]
                        callsCSVfilewriter.writerow(row)

            # print(TwilioNumber)

            print(f'Total count of calls made to {TwilioNumber} from {timeRanges[0].strftime("%H")} to {timeRanges[1].strftime("%H hs, %d-%m-%Y %Z")} is: {Count}')