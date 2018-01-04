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

completed_quests = []
incomplete_quests = []
# the intent is for the player to never see the total_quests list, otherwise they would know which quests they have to get. The only reason
# total_quests is a list is for coding transitioning quests from the total_quests list to the incomplete_quests list to the completed_quests
#list
total_quests = []

class Quest():
    def __init__(self, title, description, objective):
        self.title = title
        self.description = description
        self.objective = objective
        total_quests.append(self.title)

    def read(self):
        print(f"{self.title}\n{self.description}\nObjective : {self.objective}\n")
        self.quest_status()

    def quest_status(self):
        if self.title in completed_quests:
            status = 'complete'
        if self.title in incomplete_quests:
            status = 'incomplete'
        if self.title in total_quests:
            status = 'You do not have that quest'
        else:
            status = 'That is not a quest'
        print(status)

character = Eagle()

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

Learning_to_Fly = Quest("Learning to Fly", "fly North", "learn how to move")

skills = []



