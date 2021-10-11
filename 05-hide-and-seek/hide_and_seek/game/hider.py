from random import randint

# TODO: Define the Hider class here

class Hider:

    def __init__(self):
        self.location = randint(1, 1000)
        self.distance = [1000, 1000]

    def get_hint(self):
        """
        Gives a hint based on the previous movement of the seeker.

        Args:
            self (Hider): instance of Hider
        
        return (str): The hint given to the user (Seeker) 
        """
        if self.distance[-2] >= self.distance[-1]:
            # if self.distance[-1] <= 100:
            #     hint = "Getting hot!"
            # elif self.distance[-1] <= 50:
            #     hint = "Almost there!"
            # elif self.distance[-1] <= 20:
            #     hint = "So close!!!"
            # else:
            hint = "(>.<) Getting warmer!"
        else:
            hint = "(^.^) Getting colder..."

        if self.distance[-1] == 0:
            hint = "(;.;) You found me!"

        return hint

    def watch(self, location):
        """
        Calculates distance between hider and seker and updates distance list attribute.
        
        Args:
            self (Hider): instance of Hider
            location (int): the seeker's location

        return: None
        """
        new_dist = abs(self.location - location)
        self.distance.append(new_dist)
