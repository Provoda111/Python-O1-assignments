import random

class Car:
    def __init__(self, regNumber, topSpeed):
        self.regNumber = regNumber
        self.topSpeed = topSpeed
        self.currentSpeed = 0
        self.traveledDistance = 0
        print(f"Car\nRegistration number: {regNumber}\nTop speed: {topSpeed}")
        pass

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
        pass

    def Drive(self, hours):
        if self.currentSpeed >= 1:
            self.traveledDistance = self.traveledDistance + (self.currentSpeed * hours)
            print(f"\nCar has driven {hours} hours at speed {self.currentSpeed} Km/h")
            print(f"Car has driven at this amount of time {self.traveledDistance} Km\n")
            pass
        else:
            print(f"Car didn't drive because current speed is 0")
        pass

cars = []

# This for-loop creates 10 car
for i in range(10):
    car = Car(f"ABC-{i + 1}", random.randint(100, 200))
    cars.append(car)

someoneWon = False

while not someoneWon:
    for car in cars:
        car.Accelerate(random.randint(-10, 15))
        car.Drive(1)

        if car.traveledDistance >= 10000:
            print(f"Car with a registration number {car.regNumber} has won the race!")
            someoneWon = True
            break