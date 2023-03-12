import random
from enum import Enum
import numpy.random as rnd

class Distribution(Enum): # If we will use rnd-functions like rnd.normal etc
    UNIFORM = 0
    NORMAL = 1
class RandEngine(object):
    def __int__(self, begin=0, end=1, distr=rnd.uniform):
        self.begin = begin
        self.end = end
        if distr == rnd.uniform:
            self.f = rnd.uniform
        else:
            if type(distr) == function:
                self.f = distr
            else:
                raise TypeError
    def get(self):
        if self.f == rnd.uniform:
            return (self.end-self.begin) * self.f() + self.begin
        else:
            return self.f()
