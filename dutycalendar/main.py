# A shift is a event. And is build from the schedule.
# Everything is captured in a calendar. That has a set length.
# A schedule are the building blocks. aka 20 off 15 on days. and has a start date.
# modules ics, UUID, maybe dateutil.

from datetime import date, timedelta, datetime
from configparser import ConfigParser
from schedule import Schedule

#Read config.ini file
parser = ConfigParser()
parser.read("config.ini")

def main()->None:
    # instanciate Schedules with startdates
    # Future this needs to be done from a confg file. 
    sched1 = parser["SCHEDULE 1"] #lees de ini file
    # print(datetime.strptime(sched1["startdate"],"%d-%m-%Y")) # gebruik een waarde uit de gelezen gedeelte.
    joris = Schedule(name = sched1["name"],dayson =[int(sched1["dayson"])],daysoff = [int(sched1["daysoff"])],startdate=[datetime.strptime(sched1["startdate"],"%d-%m-%Y").date()],counter_length = 11) # moet nog de startdate juist verwerken.
    caroline = Schedule(name = "caroline",dayson =[8,9],daysoff = [22,21],startdate=[date(2022,12,26),date(2022,12,10)],counter_length = 10)
    
    # Create lists with the startdates
    joris.start_dates(count=joris.counter_length)
    caroline.start_dates(count=caroline.counter_length)


    for i in joris.startdates:
        print(i)
    

if __name__ == "__main__":
    main()