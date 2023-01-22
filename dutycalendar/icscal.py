from ics import Calendar, Event


c = Calendar()
i = 0
for datum in joris.startdates:
    
    e= Event()
    e.description = f"{joris.name} {i+1}"
    e.begin = datum
    e.duration = timedelta(days=15) #nu moet ik om en om de kort en lange hebben?????
    e.all_day
    i += 1
    # print(i)
    # print(e)
    c.events.add(e)

print(c)
with open("my.ics", "w") as f:
    f.write(c.serialize())