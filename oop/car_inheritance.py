class Car:
    def __init__(self):
        self.average_speed = 80
        self.fuel = 'electric: empty'
        print(self.fuel)
    
    def increase_speed(self):
        self.average_speed += 20
    
    def brake(self):
        self.average_speed = 0

class ElectricCar(Car):
    def refuel(self):
        self.fuel = 'electric: full'
        print(self.fuel)


tesla = ElectricCar()
tesla.refuel()
