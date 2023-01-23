"""This file creates the instances from the config.ini file and then mkaes the startdates used in the main.py file."""

from schedule import Schedule
from configparser import ConfigParser
from datetime import datetime as dt


#Read config.ini file
parser = ConfigParser()
parser.read("config.ini")



def instanciate():
    # Create instances from the config.ini file.
    scheds = []
    for i in parser.sections():
        schedName = parser[i]["name"]
        counter_length = parser[i]["counter_length"]
        s = Schedule(schedName,counter_length)
        s.startdate = dt.strptime(parser[i]["startdate"],"%d-%m-%Y") # converti it to date with strptime
        s.dayson = int(parser[i]["dayson"])
        s.daysoff = int(parser[i]["daysoff"])
        scheds.append(s)
        # s = Schedule(name=schedName, counter_length=counter_length,startdate=list(startdate),dayson=list(dayson),daysoff=list(daysoff)) 
        
    # for sched in scheds:
    #     sched.start_dates(5)    
    print(scheds)
        # print(schedName)
        # print(counter_length)
        # print(startdate)
    
    

instanciate()
