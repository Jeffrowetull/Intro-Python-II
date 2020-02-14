# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.inventory = []
        
    def move(self, direction):
        next_room = getattr(self.position, f'{direction}_to')
        if next_room is not None:
           self.position = next_room
           print(self.position)
        else:
           print('The way is blocked') 