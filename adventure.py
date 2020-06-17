#import modules
import inquirer
from store import buy_weapons, enter_store, buy_magic

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
        inquirer.List('go', message = "Hello skipper I'm the Captain of the finest and fastest ship in the Spanish Armada, Whats your buisness on LA ESPERANZA?",
        choices=['Join te crew', 'Fight the Captian', 'Barter for Passage', 'Inspect the Ship', 'Stop talking to Captian']),
    ]
    andale = inquirer.prompt(direction)
    return andale['go']








#variables
user = {}

#creating user profile
#user['name'] = input("Hello what is your name?")
#print(user)
#user['class'] = input("What class are you? (Diplomat/Barbarian/Mage/Theif)")

profile = [
    inquirer.Text('name', message = "Hello nomad I am Ehecatl. What is your name?"),
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
        items_bought = enter_store(user['gold'])
        user['inventory'].update(items_bought)
        print(user['inventory'])
        print(items_bought)
        for key in items_bought.items:
            user['gold'] = user['gold'] - items_bought[key]['cost']
        print(user)    
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
    elif user['location'] == 'Join the crew':
        user['location'] = join_the_crew()
    elif user['location'] == 'Fight the Captain':
        user['location'] = fight_the_captain()
    elif user['location'] == 'Barter for Passage':
        user['location'] = barter_for_passage()
    elif user['location'] == 'Inspect the Ship':
        user['location'] = i_the_ship
    elif user['location'] == 'Stop talking to Captain':
        user['location'] = s_t_to_captain()
    print(user['location'])

#answer = input("You wake up on a cold morning with the wind shaking the rafters. Do you want to but on a scarf or sweater? (scarf/sweater)")

#if answer.lower().strip() == "scarf":