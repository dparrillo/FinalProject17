import random

class Eagle():
    def __init__ (self, name = 'Hey you!', faction = 'faction'):
        self.name = name
        self.faction = faction

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
                break
            else:
                print(error_message)

acceptable_inputs = []
completed_quests = []
incomplete_quests = []
# the intent is for the player to never see the total_quests list, otherwise they would know which quests they have to get. The only reason
# total_quests is a list is for coding transitioning quests from the total_quests list to the incomplete_quests list to the completed_quests
# list
innate_quests = []
total_quests = []

error_message = 'Not recognizable. Possible problems: spelling, capitalization, bad input'
def user_input():
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

    def complete_quest(self):
        if self.title in innate_quests:
            innate_quests.remove(self.title)
            incomplete_quests.remove(self.title)
            completed_quests.append(self.title)
        else:
            incomplete_quests.remove(self.title)
            completed_quests.append(self.title)

character = Eagle()

Learning_to_Fly = Quest("Learning_to_Fly", 'learn to fly', 'fly', 'innate')

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
user_input()
print("""Wow! Look at that! You only have one thing left to do, although that probably won't last very long. Remember, you can always check your
to-do list by typing log(). I wonder what 'Learning to Fly' means? Let's read that mental list of yours.""")