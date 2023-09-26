# python
# 09/26/23

# the class to represent a man in the simulation
class Man:
    # init method 
    def __init__(self, name, age, assets, health):
        self.name = name
        self.age = age
        self.assets = assets
        self.health = health

    # str method to display man object
    def __str__(self):
        return "Name: " + self.name + "\nAge: " + str(self.age) + "\nAssets: " + str(self.assets) + "\nHealth: " + str(self.health)
