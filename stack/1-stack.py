# Car dealership inventory list example problem

class Car: # Car class for creating a car object

    def __init__(self, color, mileage, make, model, year): # details of our car object
        self.color = color
        self.mileage = mileage
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return (self.color + " " + str(self.year) + " " + self.make + " " + self.model + " with {:,}".format(self.mileage) + " miles")


car_inventory = [] # creating our list (stack)
# Now we will add 5 cars to our inventory
car_inventory.append(Car("Red", 15251, "Hyundai", "Accent", 2020))
car_inventory.append(Car("Blue", 67098, "Toyota", "Corolla", 2021))
car_inventory.append(Car("Silver", 7089, "Hyundai", "Tuscon", 2019))
car_inventory.append(Car("Black", 20043, "Lincoln", "Navigator", 2018))
car_inventory.append(Car("White", 78065, "Ford", "Mustang", 2016))

print()
print("Dealership Inventory:")
i = 1 # iterator
for car in car_inventory: # this will print every car in our inventory to us
    print(i, "-", car)
    i += 1

"""
This list (stack) is very useful to us because we can easily store car objects inside of it and see what cars we have in our
inventory from a quick glance using a print loop. We could expand this to have more functionality but this is just to give you
a basic idea of what this data structure could be used for. Go ahead and try the problem below and see if you cancome up with 
a solution!
"""

