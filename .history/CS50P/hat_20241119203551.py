import random

class Hat:
    
    houses = ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))


hat = Hat()
hat.sort("Harry")
