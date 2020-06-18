#import modules
import inquirer
from inquirer.themes import GreenPassion
from store import buy_weapons, enter_store, buy_magic
from npc import * 

#functions
def base_value(ch_class):
    stats = {}
    if ch_class == "Diplomat":
        stats['stealth'] = 2 
        stats['charisma'] = 6
        stats['strength'] = 1
        stats['magic'] = 1
    elif ch_class == "Barbarian":
        stats['stealth'] = 1
        stats['charisma'] = 1
        stats['strength'] = 6
        stats['magic'] = 2
    elif ch_class == "Mage":
        stats['stealth'] = 2
        stats['charisma'] = 1
        stats['strength'] = 1
        stats['magic'] = 6
    elif ch_class == "Theif":
        stats['stealth'] = 6
        stats['charisma'] = 1
        stats['strength'] = 2
        stats['magic'] = 1
    
    return stats
    
def village():
    direction = [
        inquirer.List('go', message = "Where do you want to go?",
        choices=['Store', 'Plaza', 'Mictlan Desert', 'Xochimilco', 'Smoking Mountain Pass', 'Sea of Cortez']),
    ]
    andale = inquirer.prompt(direction)
    return andale['go']
def store():
    print("welcome to the Store!")
    direction = [
        inquirer.List('go', message = "What do you want to do now?",
        choices=['Buy items', 'Return to Village']),
    ]
    andale = inquirer.prompt(direction)
    return andale['go'] 

def plaza():
    direction = [
        inquirer.List('go', message = "What do you want to do now?",
        choices=['Talk to Doc', 'Talk to Cow', 'Return to Village']),
    ]
    andale = inquirer.prompt(direction)
    return andale['go'] 

def mictlan_desert():
    direction = [
        inquirer.List('go', message = "What do you want to do now?",
        choices=['Talk to Mictlan', 'Go to the Fiesta', 'Return to Village']),
    ]
    andale = inquirer.prompt(direction)
    return andale['go'] 
def xochimilco():
    direction = [
        inquirer.List('go', message = "What do you want to do now?",
        choices=['Talk to ferryman', 'Return to Village']),
    ]
    andale = inquirer.prompt(direction)
    return andale['go'] 

def smoking_mt_pass():
    direction = [
        inquirer.List('go', message = "What do you want to do now?",
        choices=['Talk to lama', 'Return to Village']),
    ]
    andale = inquirer.prompt(direction)
    return andale['go'] 

def sea_of_cortez():
    direction = [
        inquirer.List('go', message = "What do you want to do now?",
        choices=['Talk to Captain', 'Return to Village']),
    ]
    andale = inquirer.prompt(direction)
    return andale['go']
    
def t_to_captain():
    direction = [
        inquirer.List('go', message = "Hello land lover I'm the Captain of the finest and fastest ship in the Spanish Armada, Whats your buisness on LA ESPERANZA?",
        choices=['Join the Crew', 'Fight the Captain', 'Barter for Passage', 'Inspect the Ship', 'Stop talking to Captian']),
    ]
    andale = inquirer.prompt(direction)
    return andale['go']
def join_the_crew():
    direction = [
        inquirer.List('go', message = "Welcome to the crew Ensign " + user['name'] + "! What say you?",
        choices=['Set sail Captain', 'Lets stay at Port', 'Search the Ship']),
    ]
    andale = inquirer.prompt(direction)
    return andale['go']
#idk if 'go' will work here since it stops at fight and theres no change to another direction
def fight_the_captain(user, captain):
    print("So its a fight you want " + user['name'] + ", then it's a fight you'll get?")
    print("The Captain atacks with " +  str(captain['power']) + ".")
    return "sea_of_cortez"

def barter_for_passage():
    direction = [
        inquirer.List('go', message = "It will be 40 gold to get passsage on La Esperanza",
        choices=['Magic a rock into 40 gold', 'Give Captain 30 gold', 'Give Captain 40 gold', 'Give Captain 20 gold']),
    ]
    andale = inquirer.prompt(direction)
    return andale['go']




#variables
user = {}

profile = [
    inquirer.Text('name', message = "Hello traveler I am Ehecatl. What is your name?"),
    inquirer.List('class', message = "What class are you?",
    choices=['Diplomat', 'Barbarian', 'Mage', 'Theif']),
    inquirer.Text('nightmare', message = "What is your worst nightmare?")
]
user = inquirer.prompt(profile)


stats = base_value(user['class'])

user['stealth'] = stats['stealth']
user['charisma'] = stats['charisma']
user['strength'] = stats['strength']
user['magic'] = stats['magic']
user['life'] = 'alive'
user['inventory'] = [{'name': 'knife', 'strenght': 1, 'cost': 25},{'name': 'hands', 'strenght': 0, 'cost': 0}]
user['weapon_inuse'] = {'hands': {'name': 'hands', 'strenght': 0}}
user['gold'] = 100
#base scores for class D:2,6,1,1/B:1,1,6,2/M:2,1,1,6/T:6,1,2,1




print(user)
user['location'] = 'village' 

while user['life'] == 'alive':
    if user['location'] == 'village' or user['location'] == 'Return to Village':
        user['location'] = village() 
    elif user['location'] == 'Store':
        items_bought = {}
        items_bought = enter_store(user['gold']) #needs if statement if no purchase
        if items_bought != None:
            
            user['inventory'].append(items_bought)
            print(user['inventory'])
            print(items_bought)
            user['gold'] = user['gold'] - items_bought['cost']
            print(user)  
        user['location'] = 'village'
    elif user['location'] == 'Plaza':
        user['location'] = plaza()
        
    elif user['location'] == 'Mictlan Desert':
        user['location'] = mictlan_desert()

    elif user['location'] == 'Xochimilco':
        user['location'] = xochimilco()

    elif user['location'] == 'Smoking Mountain Pass':
        user['location'] = smoking_mt_pass()

    elif user['location'] == 'Sea of Cortez':
        user['location'] = sea_of_cortez()
    elif user['location'] == 'Talk to Captain':
        user['location'] = t_to_captain()
    elif user['location'] == 'Join the Crew':
        user['location'] = join_the_crew()
    elif user['location'] == 'Fight the Captain':
        user['location'] = fight_the_captain(user, captain)

    
    elif user['location'] == 'Barter for Passage':
        user['location'] = barter_for_passage()
    elif user['location'] == 'Inspect the Ship':
        user['location'] = i_the_ship
    elif user['location'] == 'Stop talking to Captain':
        user['location'] = s_t_to_captain()
    print(user['location'])