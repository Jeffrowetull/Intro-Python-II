# Implement a class to hold room information. This should have name and
# description attributes.
import random
class Room:
    def __init__(self,title,description):
        self.title = title
        self.description = description
        self.items = []
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
    def __repr__(self):
        return f'{self.items}'
    def __str__(self):
        return f'{self.title}\n\n{self.description}'
    
    def add_item_to_room(self,item):
        self.items.append(item)

    def fight(self):
        random_int = random.randint(1,6)
        if random_int <= 3:
            is_there_a_fight = True
            print("Time for a fight!")

