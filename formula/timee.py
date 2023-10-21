from gp import Gp
from championship import Championship
from haydovchi import Haydovchi
class Time:

    def __init__(self, hours, minutes,second,ms) -> None:
        self._hours = hours
        self._minutes = minutes
        self._second = second
        self._ms = ms
        
    
    @property
    def hours(self):
        return self._hours
    @property
    def minutes(self):
        return self._minutes
    @property
    def second(self):
        return self._second
    @property
    def ms(self):
        return self._ms
    
    def toString(self):
        return self.hours, self.minutes, self.second, self.ms
        
    
     
        