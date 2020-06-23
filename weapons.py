import inquirer

#selecting your weapon from inventory
def select_weapon(user):
    answers = [
            inquirer.List('item', message = "What weapon do you want to use?",
            choices=user['inventory']),
        ]
    weapon_choosen = inquirer.prompt(answers)
    user['weapon_inuse'] = weapon_choosen['item']    
    return user['weapon_inuse']
    