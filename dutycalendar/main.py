# A shift is a event. And is build from the schedule.
# Everything is captured in a calendar. That has a set length.
# A schedule are the building blocks. aka 20 off 15 on days. and has a start date.
# modules ics, UUID, maybe dateutil.


from ics import Calendar, Event 

c = Calendar()
e = Event()
e.name ="test"

print(e)