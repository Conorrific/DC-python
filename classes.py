class Car: 
    def __init__(self,make,model,color):
        self.model = 'Accord'
        self.make = 'Honda'
        self.color = 'White'
    def changeColor(self,toColor):
        print(f"Changing rom {self.color} to {toColor}")
        self.color = toColor    
    def openDoor(self):
        print("Open the door")
    def displayColor(self):
        print(f"The color is {self.color}")

car = Car('Toyota','Camry','Orange')
car.color = "Green"
print(car.model)
print(car.make)
print(car.color)
car.openDoor()
car.displayColor()

class Table:
    def __init__(self,width,height,price,model,material_type):
        self.width = 19
        self.height = 24
        self.price = 20
        self.model = "Tables"
        self.material_type = "Iron"
    def raiseTable(self):
        self.height += 4
        print(self.height)
Table.height(14)

class Employee:
    def __init__(self, first_name, last_name, employee_id):
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.address = ""
emp = Employee('John','Doe','EDRF456')