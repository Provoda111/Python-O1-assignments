import random
from Race import Race

class Car:
    def __init__(self, regNumber, topSpeed):
        self.regNumber = regNumber
        self.topSpeed = topSpeed
        self.currentSpeed = 0
        self.traveledDistance = 0

    def Accelerate(self, velocity):
        if velocity >= 1 and velocity <= self.topSpeed:
            print(f"Car accelerated by {velocity} Km/h\n")
            if velocity + self.currentSpeed > self.topSpeed:
                print(f"Car {self.regNumber} can't go any faster")
            else:
                self.currentSpeed += velocity

        #TODO THINK IF NEED TO CUT VELOCITY TO CAR'S TOP SPEED OR NOT
        elif velocity > self.topSpeed:
            print("Velocity can't be higher than car's top speed")

        elif velocity < 0:
            print(f"Car brakes by {abs(velocity)} Km/h\n")
            if self.currentSpeed < abs(velocity):
                self.currentSpeed = 0
            else:
                self.currentSpeed = self.currentSpeed - abs(velocity)
        print(f"Car current speed: {self.currentSpeed} Km/h\n")

    def Drive(self, hours):
        if self.currentSpeed >= 1:
            self.traveledDistance = self.traveledDistance + (self.currentSpeed * hours)
            print(f"\nCar has driven {hours} hours at speed {self.currentSpeed} Km/h")
            print(f"Car has driven at this amount of time {self.traveledDistance} Km\n")
            if type(self) == ElectricCar:
                self.batteryCapacity -= self.currentSpeed / hours / 25
                print(f"The car has used {self.currentSpeed / hours / 25} kW of power")
            if type(self) == FuelCar:
                self.fuelCapacity -= self.currentSpeed / hours / 25
                print(f"The car has used {self.currentSpeed / hours / 25} l of fuel")
        else:
            print(f"Car didn't drive because current speed is 0")

class ElectricCar(Car):
    def __init__(self, regNumber, topSpeed, batteryCapacity):
        super().__init__(regNumber, topSpeed)
        self.batteryCapacity = batteryCapacity
        print(f"Car\nRegistration number: {self.regNumber}\nTop speed: {self.topSpeed} Km/h\nBattery Capacity: {self.batteryCapacity} kW")


class FuelCar(Car):
    def __init__(self, regNumber, topSpeed, fuelCapacity):
        super().__init__(regNumber, topSpeed)
        self.fuelCapacity = fuelCapacity
        print(f"Car\nRegistration number: {self.regNumber}\nTop speed: {self.topSpeed} Km/h\nFuel Capacity: {self.fuelCapacity} l")
    pass

if __name__ == "__main__":
    romu_ralli = Race("Romuralli", 8000)
    # This for-loop creates 10 car
    for i in range(10):
        romu_ralli.AddParticipant(Car(f"ABC-{i + 1}", random.randint(100, 200)))
    romu_ralli.StartRace()