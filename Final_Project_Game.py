import random
import math

game_map = {0:['hills0'], 1:['hills1'], 2:['hills2'], 3:['town3'], 4:['town4'], 5:['hills5'], 6:['ocean6'], 7:['ocean7'], 8:['ocean8'], 9:['ocean9'], 10:['hills10'], 11:['hills11'], 12:['hills12'], 13:['hills13'], 14:['hills14'], 15:['hills15'], 16:['hills16'], 17:['trees17'], 18:['river18'], 19:['trees19'], 20:['hills20'], 21:['hills21'], 22:['hills22'], 23:['hills23'], 24:['hills24'], 25:['hills25'], 26:['hills26'], 27:['river27'], 28:['river28'], 29:['trees29'], 30:['hills30'], 31:['hills31'], 32:['hills32'], 33:['hills33'], 34:['hills34'], 35:['hills35'], 36:['hills36'], 37:['river37'], 38:['trees38', 'Pat'], 39:['hills39'], 40:['hills40'], 41:['hills41'], 42:['hills42'], 43:['hills43'], 44:['hills44'], 45:['cliffs45'], 46:['hills46'], 47:['river47'], 48:['hills48'], 49:['hills49'], 50:['hills50'], 51:['cliffs51'], 52:['hills52'], 53:['hills53'], 54:['hills54'], 55:['hills55'], 56:['river56'], 57:['river57'], 58:['hills58'], 59:['hills59'], 60:['hills60'], 61:['hills61'], 62:['hills62'], 63:['lake63'], 64:['lake64'], 65:['river65'], 66:['river66'], 67:['hills67'], 68:['hills68'], 69:['hills69'], 70:['hills70'], 71:['hills71'], 72:['hills72'], 73:['lake73'], 74:['lake74'], 75:['hills75'], 76:['hills76'], 77:['hills77'], 78:['hills78'], 79:['hills79'], 80:['hills80'], 81:['hills81'], 82:['hills82'], 83:['lake83'], 84:['lake84'], 85:['hills85'], 86:['hills86'], 87:['cliffs87'], 88:['hills88'], 89:['hills89'], 90:['cliifs90'], 91:['hills91'], 92:['hills92'], 93:['hills93'], 94:['hills94'], 95:['hills95'], 96:['hills96'], 97:['hills97'], 98:['hills98'], 99:['hills99']}
def location(v):
    if 'hills' in v:
        return 'hills'
    elif 'town' in v:
        return 'town'
    elif 'ocean' in v:
        return 'ocean'
    elif 'trees' in v:
        return 'trees'
    elif 'river' in v:
        return 'river'
    elif 'cliffs' in v:
        return 'cliffs'
    elif 'lake' in v:
        return 'lake'
def get_key(b):
    for k, v in game_map.items():
        if v[0] == b:
            return k

class Eagle():
    def __init__ (self, name = 'Hey you!', faction = 'faction', level = 0, location = 'location', skill_number = 0):
        self.name = name
        self.faction = faction
        self.level = level
        self.location = location
        self.skill_number = skill_number

    def determine_name(self):
        self.name = input("\nWhat is your name? > ")

    def determine_faction(self):
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
        if self.faction == 'cliff-soarer':
            self.location = game_map[51][0]
            for item in game_map[51]:
                acceptable_inputs.append(f'{item}'+'.talk()')
            acceptable_inputs.remove(f'{game_map[51][0]}'+'.talk()')
        elif self.faction == 'tree-eagle':
            self.location = game_map[38][0]
            for item in game_map[38]:
                acceptable_inputs.append(f'{item}'+'.talk()')
            acceptable_inputs.remove(f'{game_map[38][0]}'+'.talk()')

    def level_up(self):
        # if self.level == math.sqrt(len(completed_quests) - 2) - 1: (for use only if content gets really big)
        if self.level == math.sqrt(len(completed_quests)-1):
            self.level += 1
            self.skill_number += 1
            print(f"You leveled up! Level {self.level}")

    def where(self):
        print(self.location)

    def move(self, direction):
        z = get_key(self.location)
        if direction == 'north':
            if list(str(z))[-1] == '9':
                print('To the North lies the cold tundra. There is no reason to go there')
            else:
                z += 1
                self.location = game_map[z][0]
                print(f'Flying over the {location(self.location)}')
        if direction == 'south':
            if list(str(z))[-1] == '0':
                print('To the South lies the arid Sonoran Desert. No reason to go there.')
            else:
                z -= 1
                self.location = game_map[z][0]
                print(f'Flying over the {location(self.location)}')
        if direction == 'east':
            if list(str(z))[0] == '9':
                print('Man has ventured so far East that he now has towns and farms in the plains on the Eastern side of the Rockies. To go there would be suicide')
            else:
                z += 10
                self.location = game_map[z][0]
                print(f'Flying over the {location(self.location)}')
        if direction == 'west':
            if len(list(str(z))) == 1:
                print('Any farther West and you would be over the Pacific Ocean. No reason to go there.')
            else:
                z -= 10
                self.location = game_map[z][0]
                print(f'Flying over the {location(self.location)}')
        if len(game_map[z]) > 1:
            for accept in acceptable_inputs:
                if '.talk()' in accept:
                    acceptable_inputs.remove(accept)
            for item in game_map[z]:
                acceptable_inputs.append(f'{item}'+'.talk()')
            acceptable_inputs.remove(f'{game_map[z][0]}'+'.talk()')
        # function here pointing to a new function structured as follows: if self.location == 'hills': % chance to generate animal MOB and ask user if they want to fight    if self.location == 'cliffs': you can find x NPC

acceptable_inputs = []
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

def where_am_i():
    character.where()
def fly(direction):
    character.move(direction)
    if location(character.location) == 'hills':
        mob = Mob()
        mob.fight_instance()
cardinal = ['north', 'south', 'east', 'west']
def fly_to_acceptable():
    for item in cardinal:
        acceptable_inputs.append('fly(\''+f"{item}"+'\')')
def user_input_tutor():
    while True:
        a = input()
        if a == acceptable_inputs[-1]:
            eval(a)
            break
        elif a in acceptable_inputs:
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
            incomplete_quests.append(innate_quests[-1])

    def complete(self):
        if self.title in innate_quests:
            innate_quests.remove(self.title)
            incomplete_quests.remove(self.title)
            completed_quests.append(self.title)
            character.level_up()
        else:
            incomplete_quests.remove(self.title)
            completed_quests.append(self.title)
            character.level_up()

class Mob():
    def __init__(self, animal = 'placeholder', level = 0, skill_number = 0):
        self.animal = animal
        self.level = level
        self.skill_number = skill_number
        self.animal_level()
        self.animal_name()

    def animal_level(self):
        self.level = random.randint(character.level-2, character.level+2)
        while self.level < 0:
            self.animal_level()
        self.skill_number == self.level

    def fight_instance(self):
        fight = input(f"""You see a {self.animal} in the hills below. It appears to have a skill level of {self.skill_number}. Your skill
level is {character.skill_number}. Do you go for it? y/n """)
        if fight == 'y':
            if character.skill_number == self.skill_number:
                if random.randint(0,100) < 50:
                    print(f"You caught the {self.animal}.")
                else:
                    print(f"The {self.animal} got away.")
                    character.skill_number -=1
            elif character.skill_number == self.skill_number + 1:
                if random.randint(0,100) < 84:
                    print(f"You caught the {self.animal}.")
                else:
                    print(f"The {self.animal} got away.")
                    character.skill_number-= 1
            elif character.skill_number == self.skill_number + 2:
                if random.randint(0,100) < 97:
                    print(f"You caught the {self.animal}.")
                else:
                    print(f"The {self.animal} got away.")
                    character.skill_number -= 1
            elif character.skill_number == self.skill_number + 3:
                if random.randint(0,100) < 99:
                    print(f"You caught the {self.animal}.")
                else:
                    print(f"The {self.animal} got away.")
                    character.skill_number -= 1
            elif character.skill_number > self.skill_number + 3:
                print(f"You caught the {self.animal}.")
            elif character.skill_number == self.skill_number - 1:
                if random.randint(0,100) < 16:
                    print(f"You caught the {self.animal}.")
                else:
                    print(f"The {self.animal} got away.")
                    character.skill_number -= 1
            elif character.skill_number == self.skill_number - 2:
                if random.randint(0,100) < 3:
                    print(f"You caught the {self.animal}.")
                else:
                    print(f"The {self.animal} got away.")
                    character.skill_number -= 1
            elif character.skill_number == self.skill_number - 3:
                if random.randint(0,100) < 1:
                    print(f"You caught the {self.animal}.")
                else:
                    print(f"The {self.animal} got away.")
                    character.skill__number -= 1
            elif character.skill_number < self.skill_number - 3:
                print(f"The {self.animal} got away.")
                character.skill_number -= 1
        elif fight == 'n':
            print('He got away.')
        else:
            print(error_message)

    def animal_name(self):
        if self.level <= 5:
            self.animal = random.choice(["rabbit", "groundhog", "squirrel", "mouse"])
        elif self.level > 5 and self.level <= 10:
            self.animal = random.choice(["snake", "deer", "pheasant", "fox"])

class NPC():
    def __init__(self, name, quest):
        self.name = name
        self.task = quest
        npcs.append(self.name)

    def talk(self):
        met_npcs[self.name] = self.task
        if self.task == 'none':
            print(f"I have nothing for you, {character.name}.")
        else:
            print(f"{character.name}, listen - I have a task for you.")
            for n,q in met_npcs.items():
                if self.name == n:
                    q.read()
                if input("Do you accept this quest? (y/n) ") == 'y':
                    incomplete_quests.append(self.task.title)
                    read_to_acceptable()
                break

character = Eagle()

Learning_to_Fly = Quest("Learning_to_Fly", 'If you want to play this game, you are going to have to know how to get around. For those of you who are uninformed, eagles fly. Type fly(\'direction\') where direction is a cardinal direction to go in that direction.', 'Learn how to fly', 'innate')
Hello = Quest('Hello', 'hi', 'hey', 'category')

Larry = NPC('Larry', Learning_to_Fly)
Pat = NPC('Pat', Hello)

print("""PROLOGUE :

In what became known as the Great War, the Great Elder eagle drove the humans away from the Rocky Mountains, but lost his life in the process.
His death triggered the structure of the eagle convocation to collapse, leading to the rise of two distinct convocations within the mountain range.""")

character.determine_name()

print("""
The strong, patient, and clever tree-eagles: the Regal Eagles, the Bald Eagles, who have made their nests in the boughs of tall pine trees,
live in the temperate North. Bald Eagles are excellent fighters.
They have made Varagoth, the Great Elder's daughter, their Queen.

In the South stand the fast, tactical, and aggressive cliff-soarers: the Lethal Eagles, the Golden Eagles, who have always dwelled at the highest
altitudes on rocky crags. Golden Eagles are expert hunters.
They rally under the Great Elder’s brother, Gaurkaross, and have named him their Chieftain.""")

character.determine_faction()

# In recent months, the smoke of human campfires have returned to the Rockies. Humans have always meant competition - for food, water, and shelter.
# Competition for resources could lead to another war against the humans - and with tensions as high as they are now, a war between
# cliff-soarers and tree-eagles is imminent.
# The tree-eagles and cliff-soarers have maintained a tense relationship, but so far, no blood has been shed.   <- Add this into the story somehow

print(f"\nTitle :\nThe {character.ally[0]} War for Rocky Top".upper())

# in the Class, each skill will be a function that will be associated with a specific quest. If the status of the quest is done, they are
# able to do the skill - Or just have skills unlocked after a certain number of quests completed

print("""You wake up. The sun has not yet risen over the western mountain peaks, although the sun would probably be in the sky if you were to fly to the
    western ridge of the mountain range. Something nags at the back of your mind. Oh, right, you had fallen asleep last night
    promising that you would remember to finally complete that mental list of things to do.
    Why don't you go ahead and recall your mental log by typing log()?""")
acceptable_inputs.append("log()")
user_input_tutor()
print("""Wow! Look at that! You only have one thing left to do, although that probably won't last very long. Remember, you can always check your
to-do list by typing log(). I wonder what 'Learning to Fly' means? Type Learning_to_Fly.read() to read your quest.""")
read_to_acceptable()
user_input_tutor()
print("Go ahead and try it out!")
fly_to_acceptable()
while True:
        a = input()
        if a == acceptable_inputs[-1] or a == acceptable_inputs[-2] or a == acceptable_inputs[-3] or a == acceptable_inputs[-4]:
            eval(a)
            Learning_to_Fly.complete()
            break
        elif a in acceptable_inputs:
            eval(a)
        else:
            print(error_message)
print(f"""Well, would you look at that? You, {character.name}, have leveled up! You will level up when you complete a number of quests.
It is easy to level up in the tutorial, but it will get harder later.""")


