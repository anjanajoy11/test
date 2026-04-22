class Vehicle:
    def vehicle_info(self):
        print("Inside vehicle class")
# child class
class Car(Vehicle):
    def car_info(self):
        print("Inside car class")
# creating object of car object
c1 = Car()
# access vehicles info using car object
c1.vehicle_info()
c1.car_info()