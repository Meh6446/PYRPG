import sys
import os
import pyfiglet
import monsters
import random
import pickle
'''
IDEAS : Add Sell feature(done), Add Level up feature(WIP), Add more monsters, Add more Weapons
Add a feature that pairs you with higher leveled monsters when you are high level
Re-balance game stats lol
'''
#filename = 'save'
#os.makedirs(os.path.dirname(filename), exist_ok=True)
# PYfiglet Banners
pyrpg_bnr = pyfiglet.figlet_format('PyRPG', font='small')
menu_bnr = pyfiglet.figlet_format('Menu', font='small')
profile_bnr = pyfiglet.figlet_format('Profile', font='small')
win_bnr = pyfiglet.figlet_format('You Win!', font='small')
die_bnr = pyfiglet.figlet_format('You Died!', font='small')
info_bnr = pyfiglet.figlet_format('Info', font='small')

 # Equip Dictionaries
weapons = {'Bronze Sword':10,'Iron Sword':20,'Great Sword':40}
potions = {'Health Potion':5}
armors = {'Wood Armor':10, 'Chain Armor':20}
shields = {'Wood Shield':5, 'Iron Shield':15}

#Player Class
class player:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.exp = 0
        self.exp_next = 10
        self.maxhealth = 100
        self.health = self.maxhealth
        self.base_def = 0
        self.base_attack = 10
        self.gold = 100
        self.pots = 1
        self.weap = ['Rusty Sword']
        self.arm = []
        self.shld = []
        self.eq_weap = 'Stick'
        self.eq_arm = 'Basic Clothes'
        self.eq_shld = 'None'

# calculate attack
    @property
    def attack(self):
        attack = self.base_attack

        if self.eq_weap == 'Stick':
            attack += 0

        if self.eq_weap == 'Rusty Sword':
            attack += 2

        if self.eq_weap == 'Bronze Sword':
            attack += 4
        
        if self.eq_weap == 'Iron Sword':
            attack += 6

        if self.eq_weap == 'Great Sword':
            attack += 8
        
        return attack

    @property #Calculate armor def
    def def_armor(self):
        defence = self.base_def

        if self.eq_arm == 'Basic Clothes':
            defence += 0

        if self.eq_arm == 'Wood Armor':
            defence += 4
        
        if self.eq_arm == 'Chain Armor':
            defence += 6
        
        #if self.eq_def == ''
        return defence

    @property #calculate shield def
    def def_shield(self):
        defence = self.base_def

        if self.eq_shld == 'None':
            defence += 0
        
        if self.eq_shld == 'Wood Shield':
            defence += 2

        if self.eq_shld == 'Iron Armor':
            defence += 4
        
        return defence

    @property # shield def + armor def for final Defence total
    def defence(self):
        defence = p1.def_armor + p1.def_shield

        return defence

# Enemy class
class enemy:
    def __init__(self, name, desc, maxhealth, attack, gold_get, exp, level):
        self.name = name
        self.desc = desc
        self.maxhealth = maxhealth
        self.health = self.maxhealth
        self.attack = attack
        self.gold_get = gold_get
        self.exp = exp
        self.level = level

    def randomizer(self):
        global popped
        choice = random.randint(1, 2)
        if choice == 1:
            monsters.goblin(self)
        elif choice == 2:
            monsters.skeleton(self)
        self.level = p1.level + 1
        self.attack *= int(self.level / 2)
        self.maxhealth *= int(self.level / 2)
        #popped = self.name, self.maxhealth, self.attack, self.gold_get

#Function used to clear terminal
def clear():
	if os.name == 'nt':
		os.system('CLS')
	if os.name == 'posix':
		os.system('clear')

# Main menu
def main():
    clear()
    print(pyrpg_bnr)
    print('Welcome to PyRPG')
    print('1) Start')
    print('2) Continue')
    print('3) Exit')
    a = input('>>> ')

    if a == '1':
        start()
    elif a == '2':
        if os.path.exists('save'):
            clear()
            with open('save', 'rb') as f:
                global p1
                p1 = pickle.load(f)
            f.close()
            print('Save file loaded!')
            input('')
            menu()
        else:
            print('You don\'t have a save file')
            input('')
            main()
    elif a == '3':
        sys.exit()
    else:
        main()

# New game
def start():
    clear()
    print('Enter your name')
    a = input('>>> ')
    global p1
    p1 = player(a)
    menu()

# Menu
def menu():
    clear()
    print(menu_bnr)
    print(f'Name: {p1.name}')
    print(f'Health: {p1.health}')
    print('1) Battle')
    print(f'2) Drink Potion (You have {p1.pots} potions)')
    print('3) Store')
    print('4) Inventory')
    print('5) Profile')
    print('6) Save')
    print('7) Exit')
    a = input('>>> ')

    if a == '1':
        global p
        p = enemy('null', 'null', 0, 0, 0, 0, 0)
        p.randomizer()
        battle()
    elif a == '2':
        drink_potion_menu()
    elif a == '3':
        store()
    elif a == '4':
        inventory()
    elif a == '5':
        profile()
    elif a == '6':
        clear()
        with open('save', 'wb') as f:
            pickle.dump(p1, f)
            print('File have been saved!')
        f.close()
        input('')
        menu()        
    elif a == '7':
        sys.exit()
    else:
        menu()

def drink_potion_menu():
    clear()
    if p1.pots <= 0:
        print('You don\'t have any potions')
    else:
        p1.pots -= 1
        print('You drank a potion')
        p1.health += 50
        if p1.health >= p1.maxhealth:
            p1.health = p1.maxhealth
    input('')
    menu()

def profile():
    page = 1   
    while True:
        print(profile_bnr)
        if page == 1:
            clear()
            print(f'Name: {p1.name}')        
            print(f'Gold: {p1.gold}')
            print(f'Potions: {p1.pots}')
            print(f'Attack: {p1.attack}')
            print(f'Defence: {p1.defence}')
            print(f'Health: {p1.health}/{p1.maxhealth}')
            print('1) Equips')
            print('2) Level')
            print('3) Back')
            a = input('>>> ')
            if a == '1':
                page += 1
            elif a == '2':
                page += 2
            elif a == '3':
                menu()
            else:
                profile()    
        elif page == 2:
            clear()
            print(f'Equipped Weapon: {p1.eq_weap}')
            print(f'Equipped Shield: {p1.eq_shld}')
            print(f'Equipped Armor: {p1.eq_arm}')
            print('1) Back')
            a = input('>>> ')
            if a == '1':
                page -= 1
            else:
                profile()
        elif page == 3:
            clear()
            print(f'Level: {p1.level}')
            print(f'Exp: {p1.exp}')
            print(f'To next level: {p1.exp_next}')
            print('1) Back')
            a = input('>>> ')
            if a == '1':
                page -= 2
            else:
                profile

############### Battle related stuff
#Battle function
def battle():
    clear()
    print(f'A Wild {p.name} has Appeared!')
    print(f'Your Health: {p1.health}/{p1.maxhealth}')
    print(f'Enemy\'s Health: {p.health}/{p.maxhealth}')
    print(f'Potions: {p1.pots}\n')
    print('1) Attack')
    print('2) Dodge')
    print('3) Drink Potion')
    print('4) Monster Info')
    print('5) Run')
    a = input('>>> ')

    if a == '1':
        attack()
    elif a == '2':
        dodge()
    elif a == '3':
        drink_potion()
    elif a == '4':
        monster_info()
    elif a == '5':
        run()
    else:
        battle()

def monster_info():
    clear()
    print(info_bnr)
    print(f'Name: {p.name}')
    print(f'Description: {p.desc}')
    print(f'Health: {p.maxhealth}')
    print(f'Attack: {p.attack}')
    print(f'Level: {p.level}')
    input('')
    battle()

def attack():
    clear()
    patk = int(random.uniform(p1.attack / 2, p1.attack))
    eatk = int(random.uniform(p.attack / 2, p.attack))
    if p1.defence > 0 and eatk > p1.attack / 2:
        eatk = int(eatk - p1.defence / 100 * eatk)
    turn = random.randint(1, 2)
    if turn == 1:
        if patk == p1.attack / 2:
            print('You missed!')
        else:
            p.health -= patk
            print(f'You deal {patk} damage!')                 
        input('')        
        clear()
        if eatk == p.attack / 2:
            print(f'The {p.name} missed!')
        else:
            p1.health -= eatk
            print(f'The {p.name} deal {eatk} damage!')
        input('')
        if p.health <= 0:
            win()
        if p1.health <= 0:
            die()
        else:
            battle() 
      
    elif turn == 2:
        if eatk == p.attack / 2:
            print(f'The {p.name} missed!')
        else:
            p1.health -= eatk
            print(f'The {p.name} deal {eatk} damage!')
        input('')        
        clear()       
        if patk == p1.attack / 2:
            print('You missed!')
        else:
            p.health -= patk
            print(f'You deal {patk} damage!')
        input('')
        if p.health <= 0:
            win()       
        if p1.health <= 0:
            die()
        else:
            battle()

def dodge():
    clear()
    a = random.randint(1, 3)
    dmg = p.attack / 2
    pdmg = int(p1.attack / 3)
    if a == 1:
        print('You successfully dodged the enemy attack')
        input('')
        battle()
    elif a == 2:
        p1.health -= dmg
        print(f'You barely managed to avoid the {p.name} attack!')
        print(f'You took {dmg} damage!')
        input('')
        if p1.health <= 0:
            die()
        else:
            battle()
    elif a == 3:
        p.health -= pdmg
        print('You successfully dodged the enemy!')
        print(f'While at it you accidentlly kicked a pebble hitting the {p.name} dealing {pdmg} damage!')
        input('')
        if p.health <= 0:
            win()
        else:
            battle()

def drink_potion():
    clear()
    if p1.pots <= 0:
        print('You don\'t have any potions')
    else:
        p1.pots -= 1
        print('You drank a potion')
        p1.health += 50
        if p1.health >= p1.maxhealth:
            p1.health = p1.maxhealth
    input('')
    battle()

def run():
    clear()
    a = random.randint(1, 3)
    if a == 1:
        print('You have successfully ran away')
        input('')
        menu()
    else:
        print('You failed to get away')
        input('')
        clear()
        eatk = random.randint(p.attack / 2, p.attack)
        if eatk == p.attack / 2:
            print(f'The {p.name} missed!')
        else:
            p1.health -= eatk
            print(f'The {p.name} deal {eatk} damage!')
        input('')
        if p1.health <= 0:
            die()     
        else:
            battle()

def draw():
    pass

def win():
    clear()
    print(win_bnr)
    
    print(f'You have defeated the {p.name}!!')
    print(f'You found {p.gold_get} gold!!')
    print(f'You got {p.exp} exp!')
    p1.gold += p.gold_get
    p1.exp += p.exp
    if p1.exp >= p1.exp_next:
        p1.level += 1
        p1.exp_next *= 1.5
        print('You Leveled up!!')
        print(f'You are now level {p1.level}')
    input('')
    menu()

def die():
    clear()
    print(die_bnr)
    print(f'You lost {p.exp} exp!')
    p1.exp -= p.exp
    if p1.exp <= 0:
        p1.exp = 0
        print('You lost all your exp!')
        print('Game Over!')
        input('')
        main()
    print('Better Luck Next Time!')
    input('')
    menu()

############ Item related stuff 
# Store
def store():
    clear()
    print('NPC: Welcome to the shop')
    print('NPC: What would you like to do?')
    print('1) Buy')
    print('2) Sell')
    print('3) Back')
    a = input('>>> ')
    if a == '1':
        buy()
    elif a == '2':
        sell()
    elif a == '3':
        menu()
    else:
        store()

def buy():
    clear()
    print('NPC: What would you like to buy?')
    print('1) Weapons')
    print('2) Armors & Shields')
    print('3) Potions')
    print('4) Back')
    a = input('>>> ')
    if a == '1':
        clear()
        print('NPC: Here are our top quality Weapons fresh out of the forge!')
        print('1) Bronze Sword')
        print('2) Iron Sword')
        print('3) Great Sword')
        print('4) Back')
        a = input('>>> ')
        if a == '1':
            clear()         
            a = 'Bronze Sword'
            if a in p1.weap:
                clear()
                print('NPC: You already have bought this item before')
                print('NPC: There\'s no point in buying it again...')
                input('')
                store()

            if a in weapons:
                if p1.gold >= weapons[a]:
                    clear()
                    p1.gold -= weapons[a]
                    p1.weap.append(a)
                    print('NPC: Nice choice!')
                    print(f'You have bought "{a}"!')
                    input('')
                    store()
                else:
                    clear()
                    print('NPC: You don\'t have enough gold')
                    input('')
                    store()
        elif a == '2':
            clear()         
            a = 'Iron Sword'
            if a in p1.weap:
                clear()
                print('NPC: You already have bought this item before')
                print('NPC: There\'s no point in buying it again...')
                input('')
                store()

            if a in weapons:
                if p1.gold >= weapons[a]:
                    clear()
                    p1.gold -= weapons[a]
                    p1.weap.append(a)
                    print('NPC: Nice choice!')
                    print(f'You have bought "{a}"!')
                    input('')
                    store()
                else:
                    clear()
                    print('NPC: You don\'t have enough gold')
                    input('')
                    store()
        elif a == '3':
            clear()         
            a = 'Great Sword'
            if a in p1.weap:
                clear()
                print('NPC: You already have bought this item before')
                print('NPC: There\'s no point in buying it again...')
                input('')
                store()

            if a in weapons:
                if p1.gold >= weapons[a]:
                    clear()
                    p1.gold -= weapons[a]
                    p1.weap.append(a)
                    print('NPC: Nice choice!')
                    print(f'You have bought "{a}"!')
                    input('')
                    store()
                else:
                    clear()
                    print('NPC: You don\'t have enough gold')
                    input('')
                    store()                  
        elif a == '4':
            store()
        else:
            print('NPC: Hmmm... i don\'t think we sell any of that here')
            input('')
            store()

    elif a == '2': # armors and shields
        clear()
        print('NPC: We make the finest, most durable shields and armors in this whole island')
        print('1) Armors')
        print('2) Shields')
        print('3) Back')
        a = input('>>> ')
        if a == '1':
            clear()
            print('NPC: Choose wisely...')
            print('1) Wood Armor')
            print('2) Chain Armor')
            print('3) Back')
            a = input('>>> ')
            if a == '1':
                a = 'Wood Armor'
                if a in p1.arm:
                    clear()
                    print('NPC: You already have bought this item before')
                    print('NPC: There\'s no point in buying it again...')
                    input('')
                    store()
                if a in armors:
                    if p1.gold >= armors[a]:
                        clear()
                        p1.gold -= armors[a]
                        p1.arm.append(a)
                        print('NPC: Nice pick!')
                        print(f'You have bought {a}')
                        input('')
                        store()
                    else:
                        print(f'NPC: You can\'t afford this {a}, sorry')
                        input('')
                        store()
            elif a == '2':
                a = 'Chain Armor'
                if a in p1.arm:
                    clear()
                    print('NPC: You already have bought this item before')
                    print('NPC: There\'s no point in buying it again...')
                    input('')
                    store()
                if a in armors:
                    if p1.gold >= armors[a]:
                        clear()
                        p1.gold -= armors[a]
                        p1.arm.append(a)
                        print('NPC: Nice pick!')
                        print(f'You have bought {a}')
                        input('')
                        store()
                    else:
                        print(f'NPC: You can\'t afford this {a}, sorry')
                        input('')
                        store()
            elif a == '3':
                store()
            else:
                print('NPC: Hmmm... i don\'t think we sell any of that here')
                input('')
                store()
            
        elif a == '2':
            clear()
            print('NPC: Choose a shield that\'s suitable for you and, well, your wallet')
            print('1) Wood Shield')
            print('2) Iron Shield')
            print('3) Back')
            a = input('>>> ')
            if a == '1':
                a = 'Wood Shield'
                if a in p1.shld:
                    clear()
                    print('NPC: You already have bought this item before')
                    print('NPC: There\'s no point in buying it again...')
                    input('')
                    store()

                if a in shields:
                    if p1.gold >= shields[a]:
                        clear()
                        p1.gold -= shields[a]
                        p1.shld.append(a)
                        print(f'That\'s nice! a {a} wouldn\'t hurt, right?')
                        print(f'You have bought {a}')
                        input('')
                        store()
                    else:
                        print(f'NPC: You can\'t afford this {a}, sorry')
                        input('')
                        store()
            elif a == '2':
                a = 'Iron Shield'
                if a in p1.shld:
                    clear()
                    print('NPC: You already have bought this item before')
                    print('NPC: There\'s no point in buying it again...')
                    input('')
                    store()

                if a in shields:
                    if p1.gold >= shields[a]:
                        clear()
                        p1.gold -= shields[a]
                        p1.shld.append(a)
                        print(f'That\'s nice! a {a} wouldn\'t hurt, right?')
                        print(f'You have bought {a}')
                        input('')
                        store()
                    else:
                        print(f'NPC: You can\'t afford this {a}, sorry')
                        input('')
                        store()               
            elif a == '3':
                store()
            else:
                print('NPC: Hmmm... i don\'t think we sell any of that here')
                input('')
                store()
        elif a == '3':
            store() 
        else:
            print('NPC: Hmmm... i don\'t think we sell any of that here')
            input('')
            store()

    elif a == '3':
        clear()
        print('NPC: We only sell good quality potions')
        print('1) Health Potion')
        print('2) Back')
        a = input('>>> ')
        if a == '1':
            clear()
            a = potions['Health Potion']
            print('NPC: How many do you want to buy?')
            print(f'NPC: Each costs {a} gold')
            try:
                b = int(input('>>> '))
            except ValueError:
                clear()
                print('NPC: Hey! That\'s not a number')
                input('')
                store()
            if p1.gold >= b * a:
                p1.gold -= b * a
                p1.pots += b
                print(f'NPC: Thanks for buying {b} potions!')
                input('')
                store()
            else:
                print(f'NPC: You do not have enough money to purchase {b} potions')
                input('')
                store()
        elif a == '2':
            store()
        else:
            print('NPC: Hmmm... i don\'t think we sell any of that here')
            input('')
            store()

    elif a == '4':
        menu()
    else:
        clear()
        print('NPC: Hmmm... i don\'t think we sell any of that here')
        input('')
        store()

def sell():
    clear()
    print('NPC: What would you like to sell?')
    print('1) Weapons')
    print('2) Shields')
    print('3) Armors')
    print('4) Back')
    a = input('>>> ')
    if a == '1':
        clear()
        for weapon in p1.weap:
            print(weapon)
        print('B to go back')
        a = input('>>> ')
        if a in p1.weap:
            if a == p1.eq_weap:
                p1.eq_weap = 'Stick'
            else:
                pass
            if a in weapons:
                clear()
                p1.gold += weapons[a]
                p1.weap.remove(a)
                print(f'You have sold {a} for {weapons[a]} gold')
                input('')
                sell()
        elif a == 'b':
            sell()
        else:
            sell()
    elif a == '2':
        clear()
        for shield in p1.shld:
            print(shield)
        print('B to go back')
        a = input('>>> ')
        if a in p1.shld:
            if a == p1.eq_shld:
                p1.eq_shld = 'None'
            else:
                pass
            if a in shields:
                clear()
                p1.gold += shields[a]
                p1.shld.remove(a)
                print(f'You have sold {a} for {shields[a]} gold')
                input('')
                sell()
        elif a == 'b':
            sell()
        else:
            sell()
    elif a == '3':
        clear()
        for armor in p1.arm:
            print(armor)
        print('B to go back')
        a = input('>>> ')
        if a in p1.arm:
            if a == p1.eq_arm:
                p1.eq_arm = 'None'
            else:
                pass
            if a in armors:
                clear()
                p1.gold += armors[a]
                p1.arm.remove(a)
                print(f'You have sold {a} for {armors[a]} gold')
                input('')
                sell()
        elif a == 'b':
            sell()
        else:
            sell()
    elif a == '4':
        store()
    else:
        sell()

#Inventory
def inventory():
    clear()
    print('What do you want to do?')
    print('1) Equip')
    print('2) View')
    print('3) Back')
    a = input('>>> ')
    
    if a == '1':
        equip()
    elif a == '2':
        view()
    elif a == '3':
        menu()
    else:
        inventory()

def view():
    print('Backpack:')
    for weapon in weapons:
        print(weapon)
    for armor in armors:
        print(armor)
    for shield in shields:
        print(shield)
    print('B to go back')
    a = input('>>> ')

def equip():
    clear()
    print('What do you want to equip')
    print('1) Weapons')
    print('2) Armors')
    print('3) Shields')
    print('4) Back')
    print('Enter the name of the weapon you want to equip (Case Sensitive!)')
    a = input('>>> ')
    if a == '1':
        eq_weapon()
    elif a == '2':
        eq_armor()
    elif a == '3':
        eq_shield()
    elif a == '4':
        inventory()
    else:
        equip()

def eq_weapon():
    clear()
    print(f'Equipped Currently: {p1.eq_weap}')
    for weapon in p1.weap:
        print(weapon)
    print('B to go back')
    a = input('>>> ')
    if a == p1.eq_weap:
        clear()
        print(f'You already have {a} equipped')
        input('')
        equip()
    elif a == 'b':
        equip()
    elif a in p1.weap:
        clear()
        p1.eq_weap = a
        print(f'You have equipped {a}')
        input('')
        equip()
    else:
        clear()
        print(f'You don\'t have {a} in your inventory')
        input('')
        equip()

def eq_armor():
    clear()
    print(f'Equipped Currently: {p1.eq_arm}')
    for armor in p1.arm:
        print(armor)
    print('B to go back')
    a = input('>>> ')
    if a == p1.eq_arm:
        clear()
        print(f'You already have {a} equipped')
        input('')
        equip()
    elif a == 'b':
        equip()
    elif a in p1.arm:
        clear()
        p1.eq_arm = a
        print(f'You have equipped {a}')
        input('')
        equip()
    else:
        clear()
        print(f'You don\'t have {a} in your inventory')
        input('')
        equip()

def eq_shield():
    clear()
    print(f'Equipped Currently: {p1.eq_shld}')
    for shield in p1.shld:
        print(shield)
    print('B to go back')
    a = input('>>> ')
    if a == p1.eq_shld:
        clear()
        print(f'You already have {a} equipped')
        input('')
        equip()
    elif a == 'b':
        equip()
    elif a in p1.shld:
        clear()
        p1.eq_shld = a
        print(f'You have equipped {a}')
        input('')
        equip()
    else:
        clear()
        print(f'You don\'t have {a} in your inventory')
        input('')
        equip()

if __name__ == '__main__':
    main()