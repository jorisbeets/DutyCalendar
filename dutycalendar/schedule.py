"""
schedule.py contains the class Schedule. 
Every Schedule has:
name
days on
days off
startdate
counter_length
"""
from dataclasses import dataclass
from datetime import date 


@dataclass
class Schedule():
    name = str
    days_on = int
    days_off = int
    startdate = date
    counter_length = int

