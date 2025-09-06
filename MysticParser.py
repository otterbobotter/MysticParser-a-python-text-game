from adventurelib import *
from NPC import NPC, GirlNPC, BoyNPC                                              
import os

print(r"""
{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}
{}     #####   ##    ##       ##### ##    {}
{}  ######  /#### #####    ######  /###   {}
{} /#   /  /  ##### ##### /#   /  /  ###  {}
{}/    /  /   # ##  # ## /    /  /    ### {}
{}    /  /    #     #        /  /      ## {}
{}   ## ##    #     #       ## ##      ## {}
{}   ## ##    #     #       ## ##      ## {}
{}   ## ##    #     #     /### ##      /  {}
{}   ## ##    #     #    / ### ##     /   {}
{}   ## ##    #     ##      ## ######/    {}
{}   #  ##    #     ##      ## ######     {}
{}      /     #      ##     ## ##         {}
{}  /##/      #      ##     ## ##         {}
{} /  #####           ##    ## ##         {}
{}/     ##             ##   ## ##         {}
{}#                   ###   #  /          {}
{} ##                  ###    /           {}
{}                      #####/            {}
{}                        ###             {}
{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}
""")
Win = False
# Create a bag for items to be placed in rooms
Room.items = Bag()

def load_room_description(filename):
    with open(filename, 'r') as file:
        return file.read()


# Create the rooms
town_hall = Room("""
You are in the town hall.
There is an armory to the north, and the exit is to the south.
""")

armory = Room("""
You see an old rusted sword and a pack of bandages!
""")

outside = Room("""
You see a path down to the rest of town to the east, and a trail up to the forest to the west.
""")

town = Room("""
You walk past stores and houses intill you reach an old wizerds tower (enter with enter)
""")

tower = Room("""
You press the book up against the wall, it hums... and then creaks open, showing an emaculate dining hall.
the wizerd joe is waitng for you, staff off to the side, robes creesed and worn. 
""")
tower_blueroom = Room("""
The door opens, revealing a small cristal. This cristal chiters and gerbls like it wants to talk to you!
""")
tower_redroom = Room("""
A fire pixie is flutering about it has somthing for you!
""")

tower_greenroom = Room("""
You step into a butiful garden, one with buterfiles and what not... You have won!
do "credits" to see the credits
""")
tower_doorroom = Room("""
there are three door's head
a blue door 
a red door  
and a green door 
""")
tower_keyroom = Room("""
you see boxes and boxes of...just stuff.
a few boxes of bags, a few of wands, a few of swords.
and a few of keys.
""")
forest = Room("""
You hike up the trail intill you see a clearing
farther west is a small hut
to your north theres a lookout overlooking the sea
""")

hut = Room("""
theres an old wise wooman and a crow waiting for you
""")

lookout = Room("""
                                                                                                   
                                                                                                   
                                                                                                   
                                                                                                   
                                                                                                   
                                                                                                   
                                                                                                   
                                                                                                   
        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░        
        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░        
        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░        
        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░        
        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░        
        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░        
        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░        
        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░        
        ▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒        
        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░▒▒▒▒        
        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒        
        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒        
        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒        
        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒        
        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒        
        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒        
        ▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒        
        ▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒        
        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒░░▒▒        
        ▒▒▒░░░▒▒▒▒░▒░░▒▒▒░▒▒░░░░░░░░░░░░░░░░░░░░░░░░▒░░░░░░░░░░░░░░░░░░░░▒░░░░░░░░░░░░░░░░░        
        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░        
        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░        
                                                                                                   
                                                                                                   
                                                                                                   
                                                                                                   
                                                                                                   
                                                                                                   
                                                                                                   
                                                                                                   

""")

# keys
tower.key = "spellbook"
tower_blueroom.key = "blue key"
tower_redroom.key = "red key"
tower_greenroom.key = "green key"
# Set exits for the rooms
town_hall.north = armory
town_hall.south = outside
outside.east = town
outside.west = forest
forest.north = lookout
forest.west = hut
tower.north = tower_keyroom
tower.east = tower_doorroom
tower_blueroom.south = tower_doorroom
tower_redroom.south = tower_doorroom
#tower_greenroom.south = tower_doorroom
nogodoors = [tower_doorroom]
# Define items
Rusted_sword = Item('sword',"rusty old sword")
Bandages = Item("bandages","pack of gauze and some pain herbs")
spellbook = Item("spellbook","wethered old book with strange swimming symbels on the spine")
wand = Item("wand","a hand crafted dark oak wand, infused with wild magic")
blue_key = Item("blue key","solid blue stone key... looks inpractial, mostlikly magic")
red_key = Item("red key", "clay like red blob")
green_key = Item("green key", "plant like viney stick thing")
fireball_scroll = Item("fire ball scroll", "Red partchment with ancient yellow and orange runes inscribed on it")
# Define NPCs
wise_wooman = GirlNPC("a wise wooman","wise wooman")
wise_wooman.name = "wise wooman"
wise_wooman.words = "Hey (crow caws) can you do me a favor? Take that spellbook and bring it to joe over at the end of town"
wise_wooman.detail = "Theres a tiny coller on the crow, it reads 'Crowstifer the third' "
joe = BoyNPC("joe","wizerd joe", "guy")
joe.name = "joe"
joe.detail = "His robes are light blue with gold inlining"
joe.words = """
Oh! hey!.... wait I dont know you...
how did you get in here? ohhhhh the book...
but then how did you get that?
did I give that to you?
ohhh i gave that to the wise wooman and she must have givin it to you.
welp that means your an etendy! welcome to the dungen!
make sure to take the key from the room on your right (north) oh and take the wand too
The main room is east of you!"""

cristal = BoyNPC("cristal", "orb")
cristal.name = "cristal"
cristal.words = """oh! a human! how are you? hows being a human ? what year is it? I have so many questions!
oh I forgot! I have a job.
I am to ask you a question and if you awnser corectly give you the key to the next door
"""
cristal.question = "whats joes favorit color?"
cristal.ans = "gold"
cristal.gift = red_key
cristal.wrongans = "Try looking at joe"

fire_pixie = GirlNPC("fire pixie")
fire_pixie.name = "fire pixie"
fire_pixie.words = """
Hello! I am here to give you your spell and your key
buuuuut I am going to quiz you first
"""
fire_pixie.question = "whats the wise ladys crow's name?"
fire_pixie.ans = "Crowstifer the third"
fire_pixie.gift = [green_key, fireball_scroll]
# Add items to rooms
armory.items = Bag([Rusted_sword, Bandages])
hut.items = Bag([spellbook,wise_wooman]) # Add NPCs to rooms as if they are items
tower.items = Bag([wand, joe])
tower_keyroom.items = Bag([blue_key])
tower_blueroom.items = Bag([cristal])
tower_redroom.items = Bag([fire_pixie])

# Player's inventory
player_stuff = Bag()
player_spells = Bag()

# Set the starting room
current_room = town_hall  # <-- Add this line to set the initial current room

# Define movement commands
@when('north', direction='north')
@when('south', direction='south')
@when('east', direction='east')
@when('west', direction='west')
@when('n', direction='north')
@when('s', direction='south')
@when('e', direction='east')
@when('w', direction='west')
def go(direction):
    global current_room
    
    if direction == 'north' and current_room in nogodoors:
        # Prevent north movement from tower_doorroom (one-way)
        say("That way is locked")
        return  # No action if north is not allowed
    
    room = current_room.exit(direction)
    if room:
        current_room = room
        say('You go %s.' % direction)
        look()
    else:
        say("You can't go that way.")

# Command to enter a room
@when("enter PLACE")
def enter(place):
    global current_room
    place = place.lower()

    # Lookup for named rooms you can enter
    room_lookup = {
        "tower": tower,
        "blue door": tower_blueroom,
        "red door": tower_redroom,
        "green door": tower_greenroom
        # Add more rooms as needed
    }

    if place not in room_lookup:
        say(f"You can't enter '{place}'.")
        return

    room = room_lookup[place]

    # Check for key requirement
    if hasattr(room, 'key'):
        required_key = room.key.lower()
        if any(required_key == alias.lower() for item in player_stuff for alias in item.aliases):
            say(f"You use the {required_key} to unlock the {place}.")
            current_room = room
            look()
        else:
            say(f"You need the {required_key} to enter the {place}.")
    else:
        say(f"You enter the {place}.")
        current_room = room
        look()

# The take command to pick up an item
@when('take ITEM')
@when("snach ITEM")
@when("steal ITEM")
def take(item):
    obj = current_room.items.take(item)
    if obj:
        # Prevent taking NPCs
        if isinstance(obj, NPC):  
            say(f"You can't take {obj.object_pronoun}, {obj.subject_pronoun}'s not an item!")
        else:
            say('You pick up the %s.' % obj)
            player_stuff.add(obj)
    else:
        say('There is no %s here.' % item)

@when("talkto NAME")
@when("talk NAME")
def talk(name):
    character = current_room.items.find(name)
    if character and isinstance(character, NPC):
        say(f"You talk to {character.name}. {character.words}")
        
        # If the NPC has a question, ask it
        if hasattr(character, 'question') and character.question:
            say(f"{character.name} asks: {character.question}")
            
            player_responce = input("What will you answer? >")  # Get the player's response
            
            # Compare the player's response with the NPC's answer
            if player_responce.strip().lower() == character.ans.lower():
                # Check if the gift is a list, and add each item individually
                if isinstance(character.gift, list):
                    for item in character.gift:
                        player_stuff.add(item)
                        say(f"Correct! {character.name} gives you {item}.")
                else:
                    player_stuff.add(character.gift)
                    say(f"Correct! {character.name} gives you {character.gift}.")
            else:
                say(f"Wrong answer! {character.name} says: {character.wrongans}")
    else:
        say(f"There is no one named '{name}' here.")





# The drop command to drop an item
@when('drop THING')
def drop(thing):
    obj = player_stuff.take(thing)
    if not obj:
        say('You do not have a %s.' % thing)
    else:
        say('You drop the %s.' % obj)
        current_room.items.add(obj)

# The look command to describe things in the room
@when('look')
@when("look around")
def look():
    say(current_room)
    if current_room.items:
        for i in current_room.items:
            say(f"A {i} is here.")

@when("look at NAME")
@when("look NAME")
def lookNPC(name):
    character = current_room.items.find(name)
    if character and isinstance(character, NPC):
        say(character.detail)
    else:
        say(f"There is no one named '{name}' here.")

# The inventory command to show the player's inventory
@when("i")
@when('inventory')
def show_inventory():
    if player_stuff:
        say('You have:')
        for thing in player_stuff:
            say(thing)
    else:
        say("Your inventory is empty.")

@when("credits")
def credits():
    say("""
Thank you for playing MysticParser

Made by: Otter Rose
could not be made with out adventurelib (I mean it "could" it would just be harder)
""")

if Win == True:
    credits()
else:
    pass

if current_room == tower_greenroom:
    win = True
    
# Start the game
print("""




""")
look()
start()
