import inquirer

def buy_weapons(gold):
    answers = [
        inquirer.List('item', message = "What weapon do you want to buy?",
        choices=['Wooden Sword', 'Slingshot', 'Basic Bow and Arrow', 'Small Hammer', 'Basic Spear']),
    ]
    item_choosen = inquirer.prompt(answers)
    if item_choosen['item'] == 'Wooden Sword':
        item_bought = {'name': item}
        
    return item_bought['item']

def buy_magic(gold):
    answers = [
        inquirer.List('item', message = "What magic item do you want to buy?",
        choices=['Small Wizard Wand', 'Small Magic Medallion', 'Small Pouch of Magic Powder', 'Light Magic Helmet', 'Magic Gloves']),
    ]
    item_bought = inquirer.prompt(answers)
    return item_bought['item']
    
def enter_store(gold): 
    in_store = 'yes'
    while in_store == 'yes':  
        answers = [
            inquirer.List('todo', message = "What would you like to do in our store?",
            choices=['Buy a Weapon', 'Buy a Magical Item', 'Leave Store']),
        ]
        action = inquirer.prompt(answers)  
        
        if action['todo'] == 'Buy a Weapon':
            buy_weapons(gold)
        elif action['todo'] == 'Buy a Magical Item':
            buy_magic(gold) 
        elif action['todo'] == 'Leave Store':
            in_store = 'no'
              