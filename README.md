Players will play as either a Bald Eagle or a Golden Eagle, and will experience a war for control of the Rocky Mountains.

The game is played by accepting and completing objectives (quests).

Objectives will both teach the player how to play the game and progress the plot.

Some objectives will have to be first found by interacting with other programmed characters and then accepted.

Other objectives will be automatically accepted when the player begins the game, and unlocked as the previous innate quest is completed.

There is a story to the game that will develop as innate objectives are completed (regardless of whether or not the player accepts and completes objectives).

The player motivation then is not to affect the plot, but to make their own character better as the plot unfolds by acquiring new skills.

Objectives do not have to be accepted, but skills are only rewarded for completing objectives, so the most rewarding game experience is to complete all objectives.

Skills belong under two categories: Experience skills and Quest Skills:
    Experience skills are acquired by completing x objectives. ...if len(completed_quests)<=x:  skills+= 'expskill'
    Quest skills are acquired by completing specific objectives. ...if 'questname' in completed_quests: skills+= 'questskill'

Players do not win in the sense that 'You Win!' appears, but rather in the sense that 'The End' appears.


Document with initial and progressing thoughts as well as the technicalities of the level up and skills system, also sample code for the skills class which I have not added to the code yet because I haven't yet convinced myself that skills need a class:
https://docs.google.com/document/d/1O7KGxD_YjQGqC-1ESo04zVlwlkrOQ4CzLmQeE2t-ZZ8/edit?usp=sharing