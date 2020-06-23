import inquirer
from npc import mountain_troll 
import random

def talk_to_llama(user):
    print('Welcome to the Smokey Mountain Pass' + user['name'] + '! The pass is the only known route to reach the Northern Territories. very few have made it to the other side and much less have made it back. I am one of those that did. Let me guide you.')
    answer = [
        inquirer.List('go', message = "What do you want to do now?",
        choices=['Listen to advise from Llama', 'Do not listen and head into pass', 'Smoking Mountain Pass']),
    ]
    andale = inquirer.prompt(answer)
    return andale['go']

def fight_the_mountain_troll(user, moutain_troll):
    print("So its a fight you want " + user['name'] + ", then it's a fight you'll get?")
    print("The Captain atacks with " +  str(moutain_troll['power']) + " power.")
    print(user)
    print(user['weapon_inuse'][0]['strenght'])
    power = (user['strength'] + user['magic'] + user['weapon_inuse'][0]['strenght']) * random.uniform(0.9, 1.5)
    print("You attack with " + str(power) + " power.")
    if power >= moutain_troll['power']:
        print("You defeated the Mountain Troll!")
    else: 
        print("You have been deafeated by the Mountain Troll!")
    return "Smokey Moutain Pass"