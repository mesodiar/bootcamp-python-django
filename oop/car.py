class Car:
    def __init__(self):
        self.average_speed = 80
    
    def increase_speed(self):
        self.average_speed += 20
        print(self.average_speed)
    
    def brake(self):
        self.average_speed = 0

tesla = Car()
tesla.increase_speed()

