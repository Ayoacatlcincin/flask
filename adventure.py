#import modules
import inquirer

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
    
    








#variables
user = {}

#creating user profile
#user['name'] = input("Hello what is your name?")
#print(user)
#user['class'] = input("What class are you? (Diplomat/Barbarian/Mage/Theif)")

profile = [
    inquirer.Text('name', message = "Hello this is dog. What is your name?"),
    inquirer.List('class', message = "What class are you?",
    choices=['Diplomat', 'Barbarian', 'Mage', 'Theif']),
    inquirer.Text('nightmare', message = "What is your worst nightmare?")
]
user = inquirer.prompt(profile)
print(user)

stats = base_value(user['class'])
print(stats)
user['stealth'] = stats['stealth']
user['charisma'] = stats['charisma']
user['strength'] = stats['strength']
user['magic'] = stats['magic']
#base scores for class D:2,6,1,1/B:1,1,6,2/M:2,1,1,6/T:6,1,2,1


print(user)

#answer = input("You wake up on a cold morning with the wind shaking the rafters. Do you want to but on a scarf or sweater? (scarf/sweater)")

#if answer.lower().strip() == "scarf":