class Hissi:
    def __init__(self):
        self.actualFloor = 0

    # Goes to the selected floor
    def GoToFloor(self, floor):
        # If target floor is larger than actual floor goes up
        if floor > self.actualFloor:
            for i in range(floor - self.actualFloor):
                self.GoUp()

        # If target floor is smaller than actual floor goes down
        elif floor < self.actualFloor:
            for i in range(self.actualFloor - floor):
                self.GoDown()

        # If target floor is same as actual floor doesn't go anywhere
        elif floor == self.actualFloor:
            print("Elevator didn't go anywhere, elevator is on the same floor as target floor")
            pass

    # Goes up by one floor
    def GoUp(self):
        self.actualFloor += 1
        print(self.ReturnActualFloor())

    # Goes down by one floor
    def GoDown(self):
        self.actualFloor -= 1
        print(self.ReturnActualFloor())

    # Returns to user an actual floor of where elevator is located
    def ReturnActualFloor(self):
        return f"The elevator is on {self.actualFloor} floor\n"


class Apartment:
    def __init__(self, elevators, highestFloor, lowestFloor = 0,):
        self.lowestFloor = lowestFloor
        self.highestFloor = highestFloor
        self.elevators = elevators
        pass

    # Adds a new elevator to apartment
    def AddNewElevator(self, elevator):
        self.elevators.append(elevator)
        print("Succesfully added a new elevator")

    # Turns on fire alarm and makes every elevator go to the first (lowest) floor in apartment
    def FireAlarm(self):
        for elevator in self.elevators:
            elevator.GoToFloor(self.lowestFloor)

    # Moves selected elevator to the target floor
    def UseElevator(self, targetFloor, targetElevator):
        self.elevators[targetElevator - 1].GoToFloor(targetFloor)
        print(f"Elevator {targetElevator} moved to {targetFloor} floor")
        
            



kone = Hissi()
kone2 = Hissi()
print(kone.ReturnActualFloor())
#kone.GoToFloor(5)
#kone.GoToFloor(3)
#kone.GoToFloor(7)
house = Apartment([kone, kone2], 6)
house.UseElevator(3, 1)
house.FireAlarm()