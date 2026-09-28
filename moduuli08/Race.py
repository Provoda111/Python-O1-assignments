import random


class Race:
    def __init__(self, name, distance):
        self.name = name
        self.distance = distance
        self.participants = []
        self.raceEnded = False

    def AddParticipant(self, participant):
        self.participants.append(participant)

    def StartRace(self):
        while self.raceEnded == False:
            for car in self.participants:
                car.Accelerate(random.randint(-10, 15))
                car.Drive(1)

                if car.traveledDistance >= self.distance:
                    print(f"Car with a registration number {car.regNumber} has won the race!")
                    self.EndRace()
                    break
    def EndRace(self):
        self.raceEnded = True
        self.ActualSituation()

    def ActualSituation(self):
        for car in self.participants:
            print(f"The car {car.regNumber} has driven {car.traveledDistance} KM")
    
    