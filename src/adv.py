from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

items = {'belt': Item('belt', 'A belt for keeping your pants up'), 'pants': Item('pants', 'Pants for covering your bum'), 
            'shirt': Item('shirt', 'A shirt for keeping you warm'), 'hat': Item('hat', 'A hat that looks really cool'),
            'gloves': Item('gloves', 'So you won\'t leave any fingerprints'), 'shoes': Item('shoes', 'Shoes that keep your toes safe'),
            'glasses': Item('glasses', 'Glasses to help you see')}

room['outside'].items = items['pants']
room['foyer'].items = [items['belt'], items['shirt']]
room['overlook'].items = [items['gloves'],items['shoes']]
room['narrow'].items =  items['glasses']
room['treasure'].items = items['hat']

print('Welcome to the GAME')
print('===================')



player = Player('Jeff',room['outside'])
print(player.position)
print('Please type: options')
while True:
    cmd = input('->').lower()
    if cmd == 'options':
        print('ok here are your options\n The cardinal directions: n, s, e, w\n detect items\n Get \'item\'')
    elif cmd in ['n','s','e','w']:
        player.move(cmd)
    elif cmd == 'detect items':
        items = player.position.items
        print(items)
    elif cmd == f'get {items}':
        player.inventory.append(items)
        player.position.remove(items)
        print('You have acquired the {items}')
    elif cmd == f'drop {items}':
        if items in player.inventory:
            player.inventory.remove(items)
            print('You dropped the {items}')
        else:
            print('You don\'t have the {items} in your inventory')   
    elif cmd == 'q':
        print('You quit!')
        exit()
    else:
        print('Improper command!')

'''
* Make rooms able to hold multiple items
* Make the player able to carry multiple items
* Add items to the game that the user can carry around
* Add `get [ITEM_NAME]` and `drop [ITEM_NAME]` commands to the parser
'''