from enum import Enum, auto, unique
class AutoName(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name.lower().split("_")
    
    
"""
from enum import Enum

class _Inside(Enum):
    Downstairs = 'downstairs'
    Upstairs = 'upstairs'

class Location(Enum):
    Outside = 'outside'
    Inside = _Inside 

print(Location.Inside.value.Downstairs.value)
downstairs
"""


class _RigideCadavre(Enum):
    Absence = "Absence de cadavre"
    PrensenceDeepMuscle = 'upstairs'
    Presence = "au niveuasaasd"

@unique
class TracesRemarquables(AutoName):
    RigideCadavre = _RigideCadavre
    
    """TSLA = auto()
    VIX = auto()
    GME = auto()
    SP500 = auto()"""



if __name__ == '__main__':   
    for tick in TracesRemarquables:
        print(tick)
        for b in tick.value:
            print(b.value)
            print(type(b))
            
    #print(TracesRemarquables.RigideCadavre.value.Absence.value)

    print(TracesRemarquables)