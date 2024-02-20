#CarInventory.py
from Car import *
from CarInventoryNode import CarInventoryNode

class CarInventory:
    def __init__(self):
        self.root = None
        

    def _addCar(self, newnode, cnode):
        if newnode == cnode:
            cnode.cars.append(newnode.cars[0])
        elif newnode < cnode:
            if cnode.getLeft():
                self._addCar(newnode, cnode.getLeft())
            else:
                cnode.setLeft(newnode)
                newnode.setParent(cnode)
        elif newnode > cnode:
            if cnode.getRight():
                self._addCar(newnode, cnode.getRight())
            else:
                cnode.setRight(newnode)
                newnode.setParent(cnode)
            
            
    def addCar(self, Car):
        carnode = CarInventoryNode(Car)
        if self.root:
            self._addCar(carnode, self.root)
        else:
            self.root = carnode

        return


    def doesCarExist(self, Car):
        carnode = CarInventoryNode(Car)
        result = self._doesCarExist(carnode, self.root)

        if result:
            for car in result.cars:
                if car == Car:
                    return True
        return False

    
    def _doesCarExist(self, carnode, cnode):
        if not cnode:
            return None
        elif carnode == cnode:
            return cnode
        elif carnode < cnode:
            return self._doesCarExist(carnode, cnode.getLeft())
        elif carnode > cnode:
            return self._doesCarExist(carnode, cnode.getRight())

    
    def _inOrder(self, cnode):
        ret = ""
        if cnode != None:
            ret += self._inOrder(cnode.getLeft())
            ret += str(cnode)
            ret += self._inOrder(cnode.getRight())
        return ret

    def inOrder(self):
        return self._inOrder(self.root)

    def _preOrder(self, cnode):
        ret = ""
        if cnode != None:
            ret += str(cnode)
            ret += self._preOrder(cnode.getLeft())
            ret += self._preOrder(cnode.getRight())
        return ret

    def preOrder(self):
        return self._preOrder(self.root)
            

    def _postOrder(self, cnode):
        ret = ""
        if cnode != None:
            ret += self._postOrder(cnode.getLeft())
            ret += self._postOrder(cnode.getRight())
            ret += str(cnode)
        return ret
        
    def postOrder(self):
        return self._postOrder(self.root)

    def _get(self, CarInventoryNode, cnode):
        if not cnode:
            return None
        elif CarInventoryNode == cnode:
            return cnode
        elif CarInventoryNode < cnode:
            return self._get(CarInventoryNode, cnode.left)
        else:
            return self._get(CarInventoryNode, cnode.right)

    def getBestCar(self, make, model):
        getCar = Car(make, model, 0 , 0)
        carNode = CarInventoryNode(getCar)
        result = self._get(carNode, self.root)

        if result:
            bestCar = result.cars[0]
            for car in result.cars:
                if car > bestCar:
                    bestCar = car
            return bestCar
        return result
        

    def getWorstCar(self, make, model):
        getCar = Car(make, model, 0 , 0)
        carNode = CarInventoryNode(getCar)
        result = self._get(carNode, self.root)

        if result:
            worstCar = result.cars[0]
            for car in result.cars:
                if car < worstCar:
                    worstCar = car
            return worstCar
        return result
    

    def getTotalInventoryPrice(self):
        return self._getTotalInventoryPrice(self.root)

    def _getTotalInventoryPrice(self, cnode):
        total = 0
        if cnode is not None:
            for i in cnode.cars:
                total += i.price
            total += self._getTotalInventoryPrice(cnode.getRight())
            total += self._getTotalInventoryPrice(cnode.getLeft())
        return total
    


    def getSuccessor(self, make, model):
        if self is None:
            return Make

        if self.Car == model:
            if self.getRight:
                return findMin(self.getRight)
        elif self < self.Car:
            succ = self
            return getSuccessor(self.getLeft, make, model)
        else:
            return getSuccessor(self.getRight, make, model)
        return succ

        
    def findMin(self):
        current = self
        while current.getLeft():
            current.leftChild
        return current
        
    def spliceOut(self):
        pass

    def remove(self, cnode):
        if cnode.isLeaf():
            if cnode == cnode.parent.leftChild:
                cnode.parent .leftChild = None
    


        
