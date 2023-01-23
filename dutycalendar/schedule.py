"""
Explain class
"""
from dataclasses import dataclass, field
from datetime import date 

from dateutil.rrule import rrule,rruleset, DAILY

@dataclass
class Schedule:
    # Explain class variables
    name: str
    counter_length: int = field(repr=False)# gedaan om de dataclass mogelijkheden te laten zien.(fields)
    startdate: list =field(default=list)
    dayson: list = field(default_factory=list)
    daysoff: list = field(default_factory=list) 
    startdates: list = field(default_factory=list)

    def start_dates(self, count:int) -> list:
        # Create rruleset() that has two rule if there are two items in the daysoff list. Can still be modified to accomodate flexing to len of list.
        # for i in range(len(daysoff):  etc etc etc)
        self.startdates = rruleset() # DE rruleset verzamelt rrules
        # Rrule No:1 deze wordt altijd gedaan
        self.startdates.rrule(rrule(
            freq=DAILY,
            dtstart=self.startdate[0],
            count =count,#deze kan ook met until gedaan.
            interval=(self.daysoff[0]+self.dayson[0])
            ))
        if len(self.daysoff) > 1:
             # RRule No2: deze wordt gedaan als de lijsten langer zijn dan 1.
            self.startdates.rrule(rrule(
                freq=DAILY,
                dtstart=self.startdate[1],
                count =count,#deze kan ook met until gedaan.
                interval=(self.daysoff[1]+self.dayson[1])
                ))

        return self.startdates
    
"""
    Elke schedule creeert een dateutil rruleset die als er twee schedules zijn samengevoegd
    worden met een rrule set. die daarna pas aan de calendar togevoegd wordt. 
"""

