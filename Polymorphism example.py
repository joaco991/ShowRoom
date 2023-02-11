# Polymorphism example
# A superclass Vehicle creates the module turn, linking it to module change_dir emplty (abstract)
# According to each subclass, the module change_dir changes linking it to a new module, defined in each new subclass
# So, now each class shares a turn module, that works differently from each other
import time

class Vehicle:

    def change_dir(self,left, on):
        pass

    def turn(self,left):

        self.change_dir(left, True)
        time.sleep(0.25)
        self.change_dir(left, False)



class TruckedVehicle(Vehicle):

    def trucked_control(self,left, stop):
        pass

    def change_dir(self,left, on):

        self.trucked_control(left, on)



class LandVehicle(Vehicle):

    def turn_front_wheels(self,left, on):
        pass

    def change_dir(self,left, on):

        self.turn_front_wheels(left, on)