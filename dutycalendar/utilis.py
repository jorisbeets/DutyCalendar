from datetime import date
from dateutil.rrule import rrule, DAILY



def start_dates(date:date) -> list:
    startdates = list(rrule(freq=DAILY,dtstart=date, count =10,interval=35))
    return startdates

e = start_dates(date(2023,1,17))

for date in e:
    print(date)