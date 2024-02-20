#testFile
from Car import *
from CarInventoryNode import *
from CarInventory import *

car1 = Car("Tesla", "X", 2020, 25000)
car2 = Car("Honda", "Accord", 2019, 22000)
car3 = Car("Ford", "Mustang", 2022, 35000)

def test_car_inventory_node():
    node1 = CarInventoryNode(car1)
    assert node1.getMake() == "TESLA"
    assert node1.getModel() == "X"
    assert node1.getParent() is None
    assert node1.getLeft() is None
    assert node1.getRight() is None

def test_car_inventory():
    inventory = CarInventory()
    assert inventory.root is None

    inventory.addCar(car1)
    assert inventory.root == node1
    assert inventory.root.getMake() == "TESLA"
    assert inventory.root.getModel() == "X"
    assert inventory.root.getLeft() is None
    assert inventory.root.getRight() is None

    inventory.addCar(car2)
    assert inventory.root.getRight().getMake() == "HONDA"
    assert inventory.root.getRight().getModel() == "ACCORD"
    assert inventory.root.getRight().getLeft() is None
    assert inventory.root.getRight().getRight() is None

    inventory.addCar(car3)
    assert inventory.root.getLeft().getMake() == "FORD"
    assert inventory.root.getLeft().getModel() == "MUSTANG"
    assert inventory.root.getLeft().getLeft() is None
    assert inventory.root.getLeft().getRight() is None



    assert inventory.doesCarExist(car1) is True
    assert inventory.doesCarExist(car2) is False
    
    assert inventory.inOrder() == str(car1) + "\n"

    assert inventory.preOrder() == str(car1) + "\n"

    assert inventory.postOrder() == str(car1) + "\n"

    assert inventory.getBestCar("TESLA", "X") == car1
    assert inventory.getBestCar("Honda", "Accord") is None

    assert inventory.getWorstCar("TESLA", "X") == car1
    assert inventory.getWorstCar("Ford", "Mustang") is None

    assert inventory.getTotalInventoryPrice() == 25000

    assert car1 > car2
    assert car1 < car3
    assert car1 == car1

'''
def testorder():
    bst = CarInventory()

    car1 = Car("Nissan", "Leaf", 2018, 18000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("Mercedes", "Sprinter", 2022, 40000)

    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)


    assert bst.preOrder() == \
"""\
Make: Nissan, Model: Leaf, Year: 2018, Price: $18000
Make: Mercedes, Model: Sprinter, Year: 2022, Price: $40000
Make: Tesla, Model: Model3, Year: 2018, Price: $50000
"""


    assert bst.inOrder() == \
"""\
Make: Mercedes, Model: Sprinter, Year: 2022, Price: $40000
Make: Nissan, Model: Leaf, Year: 2018, Price: $18000
Make: Tesla, Model: Model3, Year: 2018, Price: $50000
"""

    assert bst.postOrder() == \
"""\
Make: Mercedes, Model: Sprinter, Year: 2022, Price: $40000
Make: Tesla, Model: Model3, Year: 2018, Price: $50000
Make: Nissan, Model: Leaf, Year: 2018, Price: $18000
"""

testorder()

assert bst.getBestCar("Nissan", "Leaf") == car1
assert bst.getBestCar("Mercedes", "Sprinter") == car3
assert bst.getBestCar("Honda", "Accord") == None

assert bst.getWorstCar("Nissan", "Leaf") == car1
assert bst.getWorstCar("Mercedes", "Sprinter") == car4
assert bst.getBestCar("Honda", "Accord") == None

assert bst.getTotalInventoryPrice() == 158000

'''
