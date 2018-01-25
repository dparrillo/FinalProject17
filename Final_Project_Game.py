import random # for use later in generating fight instances
import math # for use later when leveling up

# the game map is referencing the color coded chart on the google doc linked on the README. the keys are the box numbers in the coordinate grid. The first list item in the items is the location on the map (for use with the where am i function) and any items after the first are npcs that can be found in the area
game_map = {0:['town0'], 1:['steppe1'], 2:['steppe2'], 3:['town3'], 4:['town4'], 5:['river5'], 6:['river6'], 7:['river7'], 8:['river8'], 9:['river9'], 10:['steppe10'], 11:['steppe11'], 12:['steppe12'], 13:['steppe13'], 14:['steppe14'], 15:['river15'], 16:['river16'], 17:['Mt Hood'], 18:['river18'], 19:['The Tongass'], 20:['town20'], 21:['steppe21'], 22:['steppe22'], 23:['steppe23'], 24:['steppe24'], 25:['steppe25'], 26:['river26'], 27:['river27'], 28:['river28'], 29:['Wenatchee'], 30:['steppe30'], 31:['steppe31'], 32:['steppe32'], 33:['steppe33'], 34:['hills34'], 35:['hills35'], 36:['hills36'], 37:['river37'], 38:['Nordrassil', 'Glenn'], 39:['steppe39'], 40:['hills40'], 41:['hills41'], 42:['hills42'], 43:['steppe43'], 44:['hills44'], 45:['Mt Antero'], 46:['hills46'], 47:['river47'], 48:['steppe48'], 49:['steppe49'], 50:['hills50'], 51:['Longs Peak', 'Baine'], 52:['hills52'], 53:['steppe53'], 54:['hills54'], 55:['hills55'], 56:['river56'], 57:['river57'], 58:['steppe58'], 59:['steppe59'], 60:['hills60'], 61:['hills61'], 62:['hills62'], 63:['lake63'], 64:['lake64'], 65:['river65'], 66:['river66'], 67:['grassland67'], 68:['grassland68'], 69:['grassland69'], 70:['steppe70'], 71:['steppe71'], 72:['steppe72'], 73:['lake73'], 74:['lake74'], 75:['grassland75'], 76:['hills76'], 77:['hills77'], 78:['hills78'], 79:['grassland79'], 80:['hills80'], 81:['hills81'], 82:['river82'], 83:['lake83'], 84:['lake84'], 85:['grassland85'], 86:['hills86'], 87:['Aerie Peak'], 88:['hills88'], 89:['grassland89'], 90:['Grays Peak'], 91:['hills91'], 92:['river92'], 93:['grassland93'], 94:['grassland94'], 95:['grassland95'], 96:['grassland96'], 97:['hills97'], 98:['hills98'], 99:['grassland99']}

def location(v):
    """takes the location of the character and turns it into an aestetically pleasing word ex.(hills is more game friendly than hills42, but the player can still find exactly which hills by using where am i"""
    # the player does not call this function, it is called automatically when they move around on the map
    if 'hills' in v:
        return 'hills'
    elif 'town' in v:
        return 'town'
    elif 'river' in v:
        return 'river'
    elif 'lake' in v:
        return 'lake'
    elif 'steppe' in v:
        return 'steppe'
    elif 'grassland' in v:
        # purpose of the if statements is for a specific quest, new_kid_in_town, that requires an amulet be found in the grasslands
        if 'new_kid_in_town' in incomplete_quests:
            # first checks to see if the quest is in their quest log
            if 'amulet' not in character.inventory:
                #then checks if they already have the amulet
                if random.randint(0,100) < 30:
                    # finally, makes a 30% chance that the amulet will be found, so the game is not too easy
                    while True:
                        # attaching a while loop to an input statement assures that the code won't crash on a bad input
                        a = input("That glistening object could be Kokesh's amulet. Pick it up? y/n ")
                        if a == 'y':
                            character.pick_up('amulet')
                        if a =='y' or a == 'n':
                            break
                        else:
                            print(error_message)
            return 'grassland'
        else:
            return 'grassland'
    elif 'amulet' in v:
        while True:
            a = input("pick it up? y/n ")
            if a == 'y':
                character.pick_up('amulet')
            if a == 'y' or a == 'n':
                break
            else:
                print(error_message)
    else:
        return v
def get_key(b):
    """this function is not original - i found it on stack overflow - it returns the key of a dictionary given the item"""
    for k, v in game_map.items():
        # for use in moving the character - see Eagle.move()
        if v[0] == b:
            return k

class Eagle():
    """the character class for the player - the player instance"""
    def __init__ (self, name = 'Hey you!', faction = 'faction', level = 0, location = 'location', skill_number = 0, inventory = {}):
        """initialized when the character is made - given a preset name, faction, level, location, skill_number, and empty inventory. The name and faction are edited later by user inputs."""
        self.name = name
        self.faction = faction
        self.level = level
        self.location = location
        self.skill_number = skill_number
        self.inventory = inventory

    def determine_name(self):
        """here is when the name changes"""
        self.name = input("\nWhat is your name? > ")

    def determine_faction(self):
        """here is when the faction changes"""
        while True:
            self.faction = input("\nOnly one question remains - are you a cliff-soarer, or a tree-eagle? > ")
            if self.faction == "cliff-soarer":
                self.enemy = ["tree-eagle", "Regal Eagle", "Bald Eagle"]
                self.ally = ["Lethal Eagle", "Golden Eagle"]
            if self.faction == "tree-eagle":
                self.enemy = ["cliff-soarer", "Lethal Eagle", "Golden Eagle"]
                self.ally = ["Regal Eagle", "Bald Eagle"]
            if self.faction == "cliff-soarer" or self.faction == "tree-eagle":
                self.init_loc()
                break
            else:
                print(error_message)

    def init_loc(self):
        """called depending on the faction name. Determines where the character starts and adds the talking ability for the npcs in the area to actions list"""
        if self.faction == 'cliff-soarer':
            self.location = game_map[51][0]
            for item in game_map[51]:
                if (f'{item}'+'.talk()') not in acceptable_inputs:
                    acceptable_inputs.append(f'{item}'+'.talk()')
            acceptable_inputs.remove(f'{game_map[51][0]}'+'.talk()')
        elif self.faction == 'tree-eagle':
            self.location = game_map[38][0]
            for item in game_map[38]:
                if (f'{item}'+'.talk()') not in acceptable_inputs:
                    acceptable_inputs.append(f'{item}'+'.talk()')
            acceptable_inputs.remove(f'{game_map[38][0]}'+'.talk()')

    def level_up(self):
        """The math for leveling up. Should be called after every quest handed in"""
        # if self.level == math.sqrt(len(completed_quests) - 2) - 1: (for use only if content gets really big)
        if self.level == math.sqrt(len(completed_quests)-1):
            self.level += 1
            self.skill_number += 1
            print(f"You leveled up! Level {self.level}")

    def where(self):
        """for use in the 'where am i' function"""
        print(self.location)

    def move(self, direction):
        """code for moving around on the coordinate grid. takes into account the fight instances and npcs in home areas"""
        z = get_key(self.location)
        if direction == 'north':
            if list(str(z))[-1] == '9':
                print('To the North lies the cold tundra. There is no reason to go there')
            else:
                z += 1
                self.location = game_map[z][0]
                print(f'Flying over {location(self.location)}')
                if character.faction == 'cliff-soarer':
                    if self.location == 'The Tongass' or self.location == 'Mt Hood' or self.location == 'Nordrassil' or self.location == 'Wenatchee':
                        print(f"You can't go there! That territory belongs to the {random.choice(self.enemy)}s. Flying back to a safe location.")
                        fly('south')
                    elif location(character.location) == 'hills':
                        mob = Mob()
                        mob.fight_instance()
                elif character.faction == 'tree-eagle':
                    if self.location == 'Aerie Peak' or self.location == 'Grays Peak' or self.location == 'Longs Peak' or self.location == 'Mt Antero':
                        print(f"You can't go there! That territory belongs to the {random.choice(self.enemy)}s. Flying back to a safe location.")
                        fly('north')
                    elif location(character.location) == 'river' or location(character.location) == 'lake':
                        mob = Mob()
                        mob.fight_instance()
        elif direction == 'south':
            if list(str(z))[-1] == '0':
                print('To the South lies the arid Sonoran Desert. No reason to go there.')
            else:
                z -= 1
                self.location = game_map[z][0]
                print(f'Flying over {location(self.location)}')
                if character.faction == 'cliff-soarer':
                    if self.location == 'The Tongass' or self.location == 'Mt Hood' or self.location == 'Nordrassil' or self.location == 'Wenatchee':
                        print(f"You can't go there! That territory belongs to the {random.choice(self.enemy)}s. Flying back to a safe location.")
                        fly('south')
                    elif location(character.location) == 'hills':
                        mob = Mob()
                        mob.fight_instance()
                elif character.faction == 'tree-eagle':
                    if self.location == 'Aerie Peak' or self.location == 'Grays Peak' or self.location == 'Longs Peak' or self.location == 'Mt Antero':
                        print(f"You can't go there! That territory belongs to the {random.choice(self.enemy)}s. Flying back to a safe location.")
                        fly('north')
                    elif location(character.location) == 'river' or location(character.location) == 'lake':
                        mob = Mob()
                        mob.fight_instance()
        elif direction == 'east':
            if list(str(z))[0] == '9':
                print('Man has ventured so far East that he now has towns and farms in the plains on the Eastern side of the Rockies. To go there would be suicide')
            else:
                z += 10
                self.location = game_map[z][0]
                print(f'Flying over {location(self.location)}')
                if character.faction == 'cliff-soarer':
                    if self.location == 'The Tongass' or self.location == 'Mt Hood' or self.location == 'Nordrassil' or self.location == 'Wenatchee':
                        print(f"You can't go there! That territory belongs to the {random.choice(self.enemy)}s. Flying back to a safe location.")
                        fly('south')
                    elif location(character.location) == 'hills':
                        mob = Mob()
                        mob.fight_instance()
                elif character.faction == 'tree-eagle':
                    if self.location == 'Aerie Peak' or self.location == 'Grays Peak' or self.location == 'Longs Peak' or self.location == 'Mt Antero':
                        print(f"You can't go there! That territory belongs to the {random.choice(self.enemy)}s. Flying back to a safe location.")
                        fly('north')
                    elif location(character.location) == 'river' or location(character.location) == 'lake':
                        mob = Mob()
                        mob.fight_instance()
        elif direction == 'west':
            if len(list(str(z))) == 1:
                print('Any farther West and you would be over the Pacific Ocean. No reason to go there.')
            else:
                z -= 10
                self.location = game_map[z][0]
                print(f'Flying over {location(self.location)}')
                if character.faction == 'cliff-soarer':
                    if self.location == 'The Tongass' or self.location == 'Mt Hood' or self.location == 'Nordrassil' or self.location == 'Wenatchee':
                        print(f"You can't go there! That territory belongs to the {random.choice(self.enemy)}s. Flying back to a safe location.")
                        fly('south')
                    elif location(character.location) == 'hills':
                        mob = Mob()
                        mob.fight_instance()
                elif character.faction == 'tree-eagle':
                    if self.location == 'Aerie Peak' or self.location == 'Grays Peak' or self.location == 'Longs Peak' or self.location == 'Mt Antero':
                        print(f"You can't go there! That territory belongs to the {random.choice(self.enemy)}s. Flying back to a safe location.")
                        fly('north')
                    elif location(character.location) == 'river' or location(character.location) == 'lake':
                        mob = Mob()
                        mob.fight_instance()
        self.home_area()

    def home_area(self):
        """just enables you to talk to the npcs in the area, and shows you who you can interact with"""
        z = get_key(self.location)
        if len(game_map[z]) > 1:
            for accept in acceptable_inputs:
                if '.talk()' in accept:
                    acceptable_inputs.remove(accept)
            for item in game_map[z]:
                acceptable_inputs.append(f'{item}'+'.talk()')
            acceptable_inputs.remove(f'{game_map[z][0]}'+'.talk()')
            print(f'Entering {game_map[z][0]}')
            for item in game_map[z][1:]:
                print(f'\nYou see {item}.')

    def pick_up(self, item):
        """adds items to the inventory with a max item limit of 2 (2 legs)"""
        # not called by the player, called by meeting conditions when you have quests or by killing an animal
        if sum(self.inventory.values()) < 2:
            if item not in self.inventory.keys():
                self.inventory[item] = 1
            else:
                self.inventory[item] = self.inventory[item] + 1
        else:
            while True:
                leggo = input('You only have 2 feet! Drop an item? y/n ')
                if leggo == 'y':
                    i()
                    which = input(f'Which item? ')
                    if which in self.inventory.keys():
                        character.let_go(which)
                        character.pick_up(item)
                        break
                elif leggo == 'n':
                    break
                else:
                    print(error_message)
    def let_go(self, item):
        """drops an item"""
        # also not called by the player
        if item in self.inventory.keys():
            self.inventory[item]-=1
            if self.inventory[item] == 0:
                del self.inventory[item]
        else:
            print('You are not carrying that item')
acceptable_inputs = ['where am i', 'i']
completed_quests = []
incomplete_quests = []
# the intent is for the player to never see the total_quests list, otherwise they would know which quests they have to get. The only reason
# total_quests is a list is for coding transitioning quests from the total_quests list to the incomplete_quests list to the completed_quests
# list
innate_quests = []
total_quests = []

npcs = []
met_npcs = {}

error_message = 'Not recognizable. Possible problems: spelling, capitalization, bad input'

def i():
    """command to print the inventory"""
    print(character.inventory)
def actions():
    """MAJOR COMMAND - a player who doesn't use this command will be lost and confused"""
    print(acceptable_inputs)
def where_am_i():
    """for use in comparing the location to the game map"""
    character.where()
def fly(direction):
    """aestetic command for flying, instead of character.move('direction')"""
    character.move(direction)
cardinal = ['north', 'south', 'east', 'west']
def fly_to_acceptable():
    """allows you to fly"""
    for item in cardinal:
        acceptable_inputs.append('fly(\''+f"{item}"+'\')')
def user_input_tutor():
    """WHILE the INPUTS. This prevents the game crashing if they input an unrecognizable command"""
    while True:
        a = input()
        if a == acceptable_inputs[-1]:
            if a == 'log':
                log()
            elif a == 'i':
                i()
            elif a == 'actions':
                actions()
            elif a == 'where am i':
                where_am_i()
            else:
                eval(a)
            break
        elif a in acceptable_inputs:
            if a == 'log':
                log()
            elif a == 'i':
                i()
            elif a == 'actions':
                actions()
            elif a == 'where am i':
                where_am_i()
            else:
                eval(a)
        else:
            print(error_message)
def user_input():
    while True:
        a = input()
        if a in acceptable_inputs:
            if a == 'log':
                log()
            elif a == 'i':
                i()
            elif a == 'actions':
                actions()
            elif a == 'where am i':
                where_am_i()
            else:
                eval(a)
        else:
            print(error_message)

def read_to_acceptable():
    for item in incomplete_quests:
        if item+".read()" not in acceptable_inputs:
            acceptable_inputs.append(f"{item}"+".read()")
def log():
    print(incomplete_quests)

class Quest():
    def __init__(self, title, description, objective, category):
        self.title = title
        self.description = description
        self.objective = objective
        self.category = category
        total_quests.append(self.title)
        self.quest_branch()

    def read(self):
        print(f"{self.title}\n{self.description}\nObjective : {self.objective}\n")
        self.quest_status()

    def quest_status(self):
        if self.title in completed_quests:
            status = 'complete'
        elif self.title in incomplete_quests:
            status = 'incomplete'
        elif self.title in total_quests:
            status = 'You do not have that quest'
        else:
            status = 'That is not a quest'
        print(status)

    def quest_branch(self):
        if self.category == 'innate':
            innate_quests.append(self.title)
            if innate_quests[0] not in incomplete_quests:
                incomplete_quests.append(innate_quests[0])

    def complete(self):
        if self.title == 'i_cant_tell_you_why':
            if 'rabbit' in character.inventory.keys():
                print(f"Thanks, {character.name}. I'll put that with the stockpile. But we are going to need more.")
                character.let_go('rabbit')
                completed_quests.append(self.title)
                incomplete_quests.remove(self.title)
                acceptable_inputs.remove(f"{self.title}"+".read()")
                character.level_up()
                game_map[51] = ['Longs Peak', 'Baine', 'Kokesh']
                Glenn.task = peaceful_easy_feeling
                character.home_area()
            else:
                print('Do you have the rabbit yet?')
        elif self.title == 'new_kid_in_town':
            if 'amulet' in character.inventory.keys():
                print(f"What took you so long? Oh, by the way, that amulet is completely worthless. It was test to see it I could trust you.")
                character.let_go('amulet')
                completed_quests.append(self.title)
                incomplete_quests.remove(self.title)
                acceptable_inputs.remove(f"{self.title}"+".read()")
                character.level_up()
                game_map[51] = ['Longs Peak', 'Baine', 'Kokesh']
                character.home_area()
            else:
                print("Where's the amulet? It's very valuable.")
        elif self.title == 'peaceful_easy_feeling':
            if 'squirrel' in character.inventory.keys() and 'groundhog' in character.inventory.keys():
                print(f"Well, {character.name}. Your abilities at hunting have impressed and relieved me. It's time for you to move on to bigger things.")
                character.let_go('squirrel')
                character.let_go('groundhog')
                completed_quests.append(self.title)
                incomplete_quests.remove(self.title)
                acceptable_inputs.remove(f"{self.title}"+".read()")
                character.level_up()
                game_map[51] = ['Longs Peak', 'Baine', 'Kokesh']
                character.home_area()
            else:
                print("I need both the groundhog and the squirrel.")
        elif self.title == 'glenn_fry':
            if 'brown trout' in character.inventory.keys():
                print(f"Thanks, {character.name}, but one small fish wouldn't feed an eaglet. I'm going to need more than this.")
                character.let_go('brown trout')
                completed_quests.append(self.title)
                incomplete_quests.remove(self.title)
                acceptable_inputs.remove(f"{self.title}"+".read()")
                character.level_up()
            else:
                print("I need that brown trout!")
        else:
            if self.title in innate_quests:
                innate_quests.remove(self.title)
                if len(innate_quests) > 0:
                    incomplete_quests.append(innate_quests[0])
            completed_quests.append(self.title)
            incomplete_quests.remove(self.title)
            acceptable_inputs.remove(f"{self.title}"+".read()")
            character.level_up()

class Mob():
    def __init__(self, animal = 'placeholder', skill_number = 0):
        self.animal = animal
        self.skill_number = skill_number
        self.animal_level()
        self.animal_name()

    def animal_level(self):
        self.skill_number = random.uniform(character.level-2, character.level+2)
        if self.skill_number < 0:
            self.animal_level()

    def fight_instance(self):
        while True:
            fight = input(f"""You see a {self.animal} below. It appears to have a skill level of {self.skill_number}. Your skill
    level is {character.skill_number}. Do you go for it? y/n """)
            if fight == 'y':
                if character.skill_number == self.skill_number:
                    if random.randint(0,100) < 50:
                        while True:
                            take = input(f"You caught the {self.animal}. Would you like to take it? y/n ")
                            if take == 'y':
                                character.pick_up(self.animal)
                            if take == 'y' or take == 'n':
                                character.skill_number+=1
                                break
                            else:
                                print(error_message)
                    else:
                        print(f"The {self.animal} got away.")
                        if character.skill_number > 0:
                            character.skill_number -=1
                elif character.skill_number == self.skill_number + 1:
                    if random.randint(0,100) < 84:
                        while True:
                            take = input(f"You caught the {self.animal}. Would you like to take it? y/n ")
                            if take == 'y':
                                character.pick_up(self.animal)
                            if take == 'y' or take == 'n':
                                character.skill_number+=.5
                                break
                            else:
                                print(error_message)
                    else:
                        print(f"The {self.animal} got away.")
                        if character.skill_number > 0:
                            character.skill_number -=.5
                elif character.skill_number == self.skill_number + 2:
                    if random.randint(0,100) < 97:
                        while True:
                            take = input(f"You caught the {self.animal}. Would you like to take it? y/n ")
                            if take == 'y':
                                character.pick_up(self.animal)
                            if take == 'y' or take == 'n':
                                character.skill_number+=.25
                                break
                            else:
                                print(error_message)
                    else:
                        print(f"The {self.animal} got away.")
                        if character.skill_number > 0:
                            character.skill_number -= .25
                elif character.skill_number <= self.skill_number + 3 and character.skill_number > self.skill_number + 2.5:
                    if random.randint(0,100) < 99:
                        while True:
                            take = input(f"You caught the {self.animal}. Would you like to take it? y/n ")
                            if take == 'y':
                                character.pick_up(self.animal)
                            if take == 'y' or take == 'n':
                                character.skill_number+=.125
                                break
                            else:
                                print(error_message)
                    else:
                        print(f"The {self.animal} got away.")
                        if character.skill_number > 0:
                            character.skill_number -= .125
                elif character.skill_number > self.skill_number + 3:
                    while True:
                        take = input(f"You caught the {self.animal}. Would you like to take it? y/n ")
                        if take == 'y':
                            character.pick_up(self.animal)
                        if take == 'y' or take == 'n':
                            break
                        else:
                            print(error_message)
                elif character.skill_number == self.skill_number - 1:
                    if random.randint(0,100) < 16:
                        while True:
                            take = input(f"You caught the {self.animal}. Would you like to take it? y/n ")
                            if take == 'y':
                                character.pick_up(self.animal)
                            if take == 'y' or take == 'n':
                                character.skill_number+=1.5
                                break
                            else:
                                print(error_message)
                    else:
                        print(f"The {self.animal} got away.")
                        if character.skill_number > 1.5:
                            character.skill_number -= 1.5
                        else:
                            character.skill_number = 0
                elif character.skill_number == self.skill_number - 2:
                    if random.randint(0,100) < 3:
                        while True:
                            take = input(f"You caught the {self.animal}. Would you like to take it? y/n ")
                            if take == 'y':
                                character.pick_up(self.animal)
                            if take == 'y' or take == 'n':
                                character.skill_number+=1.75
                                break
                            else:
                                print(error_message)
                    else:
                        print(f"The {self.animal} got away.")
                        if character.skill_number > 1.75:
                            character.skill_number -= 1.75
                        else:
                            character.skill_number = 0
                elif character.skill_number >= self.skill_number - 3 and character.skill_number < self.skill_number - 2.5:
                    if random.randint(0,100) < 1:
                        while True:
                            take = input(f"You caught the {self.animal}. Would you like to take it? y/n ")
                            if take == 'y':
                                character.pick_up(self.animal)
                            if take == 'y' or take == 'n':
                                character.skill_number+=1.875
                                break
                            else:
                                print(error_message)
                    else:
                        print(f"The {self.animal} got away.")
                        if character.skill_number > 1.875:
                            character.skill__number -= 1.875
                        else:
                            character.skill_number = 0
                elif character.skill_number < self.skill_number - 3:
                    print(f"The {self.animal} got away.")
                elif character.skill_number < self.skill_number and character.skill_number >= self.skill_number - .5:
                    if random.randint(0,100) < 40:
                        while True:
                            take = input(f"You caught the {self.animal}. Would you like to take it? y/n ")
                            if take == 'y':
                                character.pick_up(self.animal)
                            if take == 'y' or take == 'n':
                                character.skill_number+=1.2
                                break
                            else:
                                print(error_message)
                    else:
                        print(f"The {self.animal} got away.")
                        if character.skill_number > 1.2:
                            character.skill_number -= 1.2
                        else:
                            character.skill_number = 0
                elif character.skill_number < self.skill_number - .5 and character.skill_number > self.skill_number -1:
                    if random.randint(0,100) < 20:
                        while True:
                            take = input(f"You caught the {self.animal}. Would you like to take it? y/n ")
                            if take == 'y':
                                character.pick_up(self.animal)
                            if take == 'y' or take == 'n':
                                character.skill_number+=1.3
                                break
                            else:
                                print(error_message)
                    else:
                        print(f"The {self.animal} got away.")
                        if character.skill_number > 1.3:
                            character.skill_number -= 1.3
                        else:
                            character.skill_number = 0
                elif character.skill_number < self.skill_number - 1 and character.skill_number >= self.skill_number - 1.5:
                    if random.randint(0,100) < 10:
                        while True:
                            take = input(f"You caught the {self.animal}. Would you like to take it? y/n ")
                            if take == 'y':
                                character.pick_up(self.animal)
                            if take == 'y' or take == 'n':
                                character.skill_number+=1.6
                                break
                            else:
                                print(error_message)
                    else:
                        print(f"The {self.animal} got away.")
                        if character.skill_number > 1.6:
                            character.skill_number -= 1.6
                        else:
                            character.skill_number = 0
                elif character.skill_number < self.skill_number - 1.5 and character.skill_number > self.skill_number - 2:
                    if random.randint(0,100) < 5:
                        while True:
                            take = input(f"You caught the {self.animal}. Would you like to take it? y/n ")
                            if take == 'y':
                                character.pick_up(self.animal)
                            if take == 'y' or take == 'n':
                                character.skill_number+=1.7
                                break
                            else:
                                print(error_message)
                    else:
                        print(f"The {self.animal} got away.")
                        if character.skill_number > 1.7:
                            character.skill_number -= 1.7
                        else:
                            character.skill_number = 0
                elif character.skill_number < self.skill_number - 2 and character.skill_number >= self.skill_number - 2.5:
                    if random.randint(0,100) < 2:
                        while True:
                            take = input(f"You caught the {self.animal}. Would you like to take it? y/n ")
                            if take == 'y':
                                character.pick_up(self.animal)
                            if take == 'y' or take == 'n':
                                character.skill_number+=1.8125
                                break
                            else:
                                print(error_message)
                    else:
                        print(f"The {self.animal} got away.")
                        if character.skill_number > 1.8125:
                            character.skill_number -= 1.8125
                        else:
                            character.skill_number = 0
                elif character.skill_number > self.skill_number and character.skill_number <= self.skill_number + .5:
                    if random.randint(0,100) < 60:
                        while True:
                            take = input(f"You caught the {self.animal}. Would you like to take it? y/n ")
                            if take == 'y':
                                character.pick_up(self.animal)
                            if take == 'y' or take == 'n':
                                character.skill_number+=.8
                                break
                            else:
                                print(error_message)
                    else:
                        print(f"The {self.animal} got away.")
                        if character.skill_number > .8:
                            character.skill_number -= .8
                        else:
                            character.skill_number = 0
                elif character.skill_number > self.skill_number + .5 and character.skill_number < self.skill_number + 1:
                    if random.randint(0,100) < 70:
                        while True:
                            take = input(f"You caught the {self.animal}. Would you like to take it? y/n ")
                            if take == 'y':
                                character.pick_up(self.animal)
                            if take == 'y' or take == 'n':
                                character.skill_number+=.7
                                break
                            else:
                                print(error_message)
                    else:
                        print(f"The {self.animal} got away.")
                        if character.skill_number > .7:
                            character.skill_number -= .7
                        else:
                            character.skill_number = 0
                elif character.skill_number > self.skill_number + 1 and character.skill_number <= self.skill_number + 1.5:
                    if random.randint(0,100) < 90:
                        while True:
                            take = input(f"You caught the {self.animal}. Would you like to take it? y/n ")
                            if take == 'y':
                                character.pick_up(self.animal)
                            if take == 'y' or take == 'n':
                                character.skill_number+=.4
                                break
                            else:
                                print(error_message)
                    else:
                        print(f"The {self.animal} got away.")
                        if character.skill_number > .4:
                            character.skill_number -= .4
                        else:
                            character.skill_number = 0
                elif character.skill_number > self.skill_number + 1.5 and character.skill_number < self.skill_number +2:
                    if random.randint(0,100) < 95:
                        while True:
                            take = input(f"You caught the {self.animal}. Would you like to take it? y/n ")
                            if take == 'y':
                                character.pick_up(self.animal)
                            if take == 'y' or take == 'n':
                                character.skill_number+=.3
                                break
                            else:
                                print(error_message)
                    else:
                        print(f"The {self.animal} got away.")
                        if character.skill_number > .3:
                            character.skill_number -= .3
                        else:
                            character.skill_number = 0
                elif character.skill_number > self.skill_number + 2 and character.skill_number <= self.skill_number + 2.5:
                    if random.randint(0,100) < 98:
                        while True:
                            take = input(f"You caught the {self.animal}. Would you like to take it? y/n ")
                            if take == 'y':
                                character.pick_up(self.animal)
                            if take == 'y' or take == 'n':
                                character.skill_number+=.1875
                                break
                            else:
                                print(error_message)
                    else:
                        print(f"The {self.animal} got away.")
                        if character.skill_number > .1875:
                            character.skill_number -= .1875
                        else:
                            character.skill_number = 0
                break
            if fight == 'n':
                print('It got away.')
                break
            else:
                print(error_message)

    def animal_name(self):
        if location(character.location) == 'hills':
            if self.skill_number <= 5:
                self.animal = random.choice(["rabbit", "groundhog", "squirrel", "mouse", "chipmunk"])
            elif self.skill_number > 5 and self.skill_number <= 10:
                self.animal = random.choice(["snake", "pheasant", "ptarmigan"])
            elif self.skill_number > 10:
                self.animal = random.choice(["deer", "fox"])
        elif location(character.location) == 'river' or location(character.location) == 'lake':
            if self.skill_number <= 5:
                self.animal = random.choice(["rainbow trout", "brown trout", "largemouth bass", "cutthroat trout", "Greenback cutthroat trout"])
            elif self.skill_number > 5 and self.skill_number <= 10:
                self.animal = random.choice(["walleye", "sucker fish", "brook trout"])
            elif self.skill_number > 10:
                self.animal = random.choice(["yellow pike", "tiger muskie"])

class NPC():
    def __init__(self, name, quest):
        self.name = name
        self.task = quest
        npcs.append(self.name)

    def talk(self):
        met_npcs[self.name] = self.task.title
        if met_npcs[self.name] == 'none' or met_npcs[self.name] in completed_quests:
            print(f"I have nothing for you, {character.name}.")
        elif met_npcs[self.name] in incomplete_quests:
            self.task.complete()
        else:
            print(f"{character.name}, listen - I have a task for you.")
            self.task.read()
            while True:
                a = input("Do you accept this quest? (y/n) ")
                if a == 'y':
                    incomplete_quests.append(met_npcs[self.name])
                    read_to_acceptable()
                if a  == 'y' or a == 'n':
                    break
                else:
                    print(error_message)

character = Eagle()

Learning_to_Fly = Quest("Learning_to_Fly", 'If you want to play this game, you are going to have to know how to get around. For those of you who are uninformed, eagles fly. Type fly(\'direction\') where direction is a cardinal direction to go in that direction.', 'Learn how to fly', 'innate')

print("""PROLOGUE :

In what became known as the Great War, the Great Elder eagle drove the humans away from the Rocky Mountains, but lost his life in the process.
    His death triggered the structure of the eagle convocation to collapse, leading to the rise of two distinct convocations within the
    mountain range.""")

character.determine_name()
i_cant_tell_you_why= Quest('i_cant_tell_you_why', (f"{character.name}. My name is Baine - I am War Advisor to Chief Gaurkaross. Don't think I a haven't heard the talk about splitting up the convocation. The War Coucil is preparing for civil war. I suspect we will need plenty of food in the near future. If you are a loyal cliff-soarer you will serve the war cause. Could you fly out to the hills and kill a rabbit? I can't tell you why. Bring it back to me."), 'Baine wants you to to bring him a rabbit from the hills.', 'collect')
Baine = NPC('Baine', i_cant_tell_you_why)
glenn_fry = Quest('glenn_fry', (f"{character.name}! I need your help. As head chef in the convocation, I have been ordered to prepare the feast for Queen Varagoth's birthday celebration this afternoon. THIS AFTERNOON! I'm not ready at all. Could you head out to the river, {character.name}, and catch me a brown trout?"), 'Glenn needs a brown trout from the river for the birthday celebration.', 'collect')
peaceful_easy_feeling = Quest('peaceful_easy_feeling', (f"I can't shake this feeling that you are caught up in the cries for anarchy, or will be soon. Nevertheless, we need more food. Bring me a squirrel and a groundhog."), 'Baine needs a groundhog and a squirrel from the plains.' 'collect')
Glenn = NPC('Glenn', glenn_fry)
new_kid_in_town = Quest('new_kid_in_town', (f"Psst. {character.name}. I have a secret to tell you. I'm not going to tell you what it is, though, because I just saw you talking to Baine. You will have to prove yourself to me, first. The last time I was flying over the grasslands, I dropped a shiny amulet. It's very valuable. Bring it back to me, and I'll tell you my secret."), 'Kokesh will only tell you his secret if you bring him his valuable amulet from the grasslands', 'collect')

Kokesh = NPC('Kokesh', new_kid_in_town)

print("""
The strong, patient, and clever tree-eagles: the Regal Eagles, the Bald Eagles, who have made their nests in the boughs of tall pine trees,
    live in the temperate North. Bald Eagles are excellent fighters.
    They have made Varagoth, the Great Elder's daughter, their Queen.

In the South stand the fast, tactical, and aggressive cliff-soarers: the Lethal Eagles, the Golden Eagles, who have always dwelled at the highest
    altitudes on rocky crags. Golden Eagles are expert hunters.
    They rally under the Great Elder’s brother, Gaurkaross, and have named him their Chieftain.""")

character.determine_faction()

if character.faction == 'tree-eagle':
    print("""Back when Queen Varagoth issued a decree saying that no eagle could fly too far East from the Rocky Mountains, nobody believed
    her. Nobody believed that the humans were heading westward. But now, in recent months, when the smoke of human campfires has returned to the
    Rockies, the Bald Eagles live in fear - fear of a gunshot and feaer of the destructive nature of man.""")
if character.faction == 'cliff-soarer':
    print("""When Gaurkaross became chieftain, he did so with the understanding that grouping together was in everyone's best interest to protect
    themselves from the Bald Eagles. Since then, tensions have died down, and talk is going around that some eagles want to overthrow
    Gaurkaross, and replace him with -- nobody.""")
# in the Class, each skill will be a function that will be associated with a specific quest. If the status of the quest is done, they are
# able to do the skill - Or just have skills unlocked after a certain number of quests completed

print("""You wake up. The sun has not yet risen over the western mountain peaks, although the sun would probably be in the sky if you were to fly to the
    western ridge of the mountain range. Something nags at the back of your mind. Oh, right, you had fallen asleep last night promising that
    you would remember to finally complete that mental list of things to do. Why don't you go ahead and recall your mental log by typing log?\n""")
acceptable_inputs.append('log')
user_input_tutor()
print("""\nWow! Look at that! You only have one thing left to do, although that probably won't last very long. Remember, you can always check your
    to-do list by typing log. I wonder what 'Learning to Fly' means? Type Learning_to_Fly.read() to read your quest.\n""")
read_to_acceptable()
user_input_tutor()
print("Go ahead and try to fly!")
fly_to_acceptable()
while True:
        a = input()
        if a == acceptable_inputs[-1] or a == acceptable_inputs[-2] or a == acceptable_inputs[-3] or a == acceptable_inputs[-4]:
            eval(a)
            Learning_to_Fly.complete()
            break
        elif a in acceptable_inputs:
            if a == 'log':
                log()
            elif a == 'i':
                i()
            elif a == 'actions':
                actions()
            elif a == 'where am i':
                where_am_i()
            else:
                eval(a)
        else:
            print(error_message)

print(f"""\nWell, would you look at that? You, {character.name}, have leveled up! You will level up when you complete a number of quests.
    It is easy to level up in the tutorial, but it will get harder later.\nWhenever you enter a new area, you will be told where you are.
    However, if you get lost, the command 'where am i' will give you a location that can be found on the map in the README. For now, you are
    flying back to your home.\n""")
character.init_loc()
print("""When you are stuck, you should check your log, explore a bit, or check your possible actions. The actions you are capable of
change depending on the area you are in. Hint: type actions\n""")
acceptable_inputs.append('actions')
while True:
        a = input()
        if a == acceptable_inputs[-1]:
            eval(a)
            break
        elif a in acceptable_inputs:
            if '.talk()' in a:
                print('Nice try you sly fox, you.')
            elif a == 'log':
                log()
            elif a == 'i':
                i()
            elif a == 'actions':
                actions()
            elif a == 'where am i':
                where_am_i()
            else:
                eval(a)
        else:
            print(error_message)
print(f"""\nNotice how there's that extra command which you haven't seen yet - '.talk()'. When another eagle is in your area, you can talk to it.
That's it for the tutorial. From here on out, you're on your own. Remember the tips you've learned, and don't forget to check the README.""")
if character.faction == 'tree-eagle':
    print(f"\nChapter 1 :\nExtinction?".upper())
else:
    print(f"\nChapter 1 :\nAnarchy".upper())
user_input()

