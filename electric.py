class Car:
    def __init__(self,make,model):
        self.make = make
        self.model = model
    
    def start(self):
        print("Starting the car")
    def changeGear(self):
        print("Changegear in Car Class")

class ElectricCar(Car):
    def __init__(self,make,model,range,autopilot):
        super().__init__(make,model)
        self.range = range
        self.autopilot = autopilot
    
    def start(self):
        print("Starting the Electric Car")
    
    def changeGear(self):
        print("Changegear in Electric Car")
class SolarCar(ElectricCar):
    def __init__(self,make,model,range,autopilot):
        pass


electric_car = ElectricCar('Tesla','Model X',40,True)
print(electric_car.make)
print(electric_car.model)