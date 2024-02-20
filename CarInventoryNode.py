#CarInventoryNode.py
from Car import Car


class CarInventoryNode():
    def __init__(self, car):
        self.make = car.make.upper()
        self.model = car.model.upper()
        self.cars = [car]
        self.parent = None
        self.left = None
        self.right = None

    def getMake(self):
        return self.make

    def getModel(self):
        return self.model

    def getParent(self):
        return self.parent

    def setParent(self, parent):
        self.parent = parent

    def getLeft(self):
        return self.left

    def setLeft(self, left):
        self.left = left

    def getRight(self):
        return self.right

    def setRight(self, right):
        self.right = right

    def __str__(self):
        result = []
        for car in self.cars:
            result.append(str(car))
            result.append('\n')
        return "".join(result)
    
    def __gt__(self, rhs):
        if self.make.upper() > rhs.make.upper():
            return True
        elif self.make.upper() < rhs.make.upper():
            return False
        if self.model.upper() > rhs.model.upper():
            return True
        elif self.model.upper() < rhs.model.upper():
            return False


    def __lt__(self, rhs):
        if self.make.upper() < rhs.make.upper():
            return True
        elif self.make.upper() > rhs.make.upper():
            return False
        if self.model.upper() < rhs.model.upper():
            return True
        elif self.model.upper() > rhs.model.upper():
            return False

   
    def __eq__(self, rhs):
        
        if rhs and self.make.upper() and self.model.upper() == rhs.model.upper():
            return True
        return False


