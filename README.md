# MysticParser-a-python-text-game
This is a fully capibile example of a zork like in python

#how to use
just download the repository using the green button, extract it and check a look at the code

# basic expination
so.... I just used a library.

okokok i'll be more in deapth
the library lets you make 3 things
rooms
items
and bags
rooms are just objects that store the name of the room and some discriptive text
items are well items, you can give them an infinite number of arguments and live your best life (in my game items are the base for the NPC's, never would I ever think a 
comment I would have to put in would be "This is to stop you from picking up NPC's")
Bags hold items, then just hold items

this is all tyed together by @when
From my basic understanding, the @when thing is just a callout that says "hey! the next function that gets difined.... ya through it in the main game loop ples"
as an example 

###### i wrote this at 2:something am....typos will be a thing, will i fix them.... probaly not


```
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
        
```



just says when the player inputs the command take or snach or steal and then the name of an object: check if its an NPC if it is yell at them if its not take the object
out of the rooms Bag and into the players

#### I hope this is helpful!
