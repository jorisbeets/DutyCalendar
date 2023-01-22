# A shift is a event. And is build from the schedule.
# Everything is captured in a calendar. That has a set length.
# A schedule are the building blocks. aka 20 off 15 on days. and has a start date.
# modules ics, UUID, maybe dateutil.


from datetime import date, timedelta

from ics import Calendar, Event

from schedule import Schedule


def main()->None:
    # instanciate Schedules with startdates
    # . 
    joris = Schedule(name = "JorisSched",days_on =[15],days_off = [20],startdate=[date(2023,1,17)],counter_length = 11)
    caroline = Schedule(name = "caroline",days_on =[8,9],days_off = [22,21],startdate=[date(2022,12,26),date(2022,12,10)],counter_length = 10)
    
    # Create lists with the startdates
    joris.start_dates(count=joris.counter_length)
    caroline.start_dates(count=caroline.counter_length)

    #create calendar: Kan evt ook in een andere file.
    c = Calendar()
    for date in joris.startdates:
        i = 0
        e= Event()
        e.description = f"{joris.name} {i}"
        e.begin = date
        e.duration = timedelta(days=joris.days_on) #nu moet ik om en om de kort en lange hebben?????
    

if __name__ == "__main__":
    main()