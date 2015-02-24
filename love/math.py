#gpl3
from love.superclasses import Object

class RandomGenerator(Object):
    _seed = 0
    _rng_state = 0
    _last_random_normal = 0
    
    def getSeed(self):
        return self._seed
    
    def getState(self):
        pass
    def random(self):
        pass
    def randomNormal(self):
        pass

    def setSeed(self, seed):
        self._seed = seed
        
    def setState(self):
        pass

rng = RandomGenerator()
    
def gammaToLinear():
    pass

def getRandomSeed():
    pass

def isConvex():
    pass

def linearToGamma():
    pass

def newBezierCurve():
    pass

def newRandomGenerator():
    rng = RandomGenerator()
    return rng

def noise():
    pass

def random():
    pass

def randomNormal():
    pass


def setRandomSeed(seed):
    rng.setSeed(seed)
    

def triangulate():
    pass
