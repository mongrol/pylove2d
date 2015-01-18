#lgpl

class Object:
    _type = "Object"
    def getType(self):
        return self._type
    
    def typeOf(self, isType):
        if isType == self._type:
            return True

class Data(Object):
    def getPointer(self):
        pass
    def getSize(self):
        pass
    def getString(self):
        pass

    
