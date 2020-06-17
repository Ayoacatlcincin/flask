import inquirer

def buy_weapons(gold):
    answers = [
        inquirer.List('item', message = "What weapon do you want to buy?",
        choices=['Wooden Sword', 'Slingshot', 'Basic Bow and Arrow', 'Small Hammer', 'Basic Spear']),
    ]
    item_choosen = inquirer.prompt(answers)
    if item_choosen['item'] == 'Wooden Sword':
        item_bought = {'name': 'Wooden Sword', 'Strenght': 2, 'cost': 100}
    elif item_choosen['item'] == 'Slingshot':
        item_bought = {'name': 'Slingshot', 'Strenght': 2, 'cost': 100}    
    elif item_choosen['item'] == 'Basic Bow and Arrow':
        item_bought = {'name': 'Basic Bow and Arrow', 'Strenght': 2, 'cost': 100}
    elif item_choosen['item'] == 'Small Hammer':
        item_bought = {'name': 'Small Hammer', 'Strenght': 2, 'cost': 100}
    elif item_choosen['item'] == 'Basic Spear':
        item_bought = {'name': 'Basic Spear', 'Strenght': 3, 'cost': 200}            
    return item_bought

def buy_magic(gold):
    answers = [
        inquirer.List('item', message = "What magic item do you want to buy?",
        choices=['Small Wizard Wand', 'Small Magic Medallion', 'Small Pouch of Magic Powder', 'Light Magic Helmet', 'Magic Gloves']),
    ]
    item_bought = inquirer.prompt(answers)
    return item_bought['item']
    
def enter_store(gold): 
    in_store = 'yes'
    weapon_bought = {}
    magic_bought = {}
    while in_store == 'yes':  
        answers = [
            inquirer.List('todo', message = "What would you like to do in our store?",
            choices=['Buy a Weapon', 'Buy a Magical Item', 'Leave Store']),
        ]
        action = inquirer.prompt(answers)  
        
        if action['todo'] == 'Buy a Weapon':
            weapon_bought = buy_weapons(gold)
            
        elif action['todo'] == 'Buy a Magical Item':
            magic_bought = buy_magic(gold) 
            
        elif action['todo'] == 'Leave Store':
            in_store = 'no'
    items_bought = {**weapon_bought, **magic_bought}  
    return items_bought
              