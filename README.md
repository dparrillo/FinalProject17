THE GAME MAP (AND SOME OF MY THOUGHTS WHILE MAKING THE GAME)
https://docs.google.com/document/d/1O7KGxD_YjQGqC-1ESo04zVlwlkrOQ4CzLmQeE2t-ZZ8/edit?usp=sharing

How to Play:
where am i = tells you where you are on the map
fly('direction') = when direction is a cardinal direction, flies you in that direction
log = shows you your questlog
Quest.read() = reads the named Quest
NPC.talk() = talks to the named NPC
actions = shows what you can do
i = show inventory

Players will play as either a Bald Eagle or a Golden Eagle.
The game is played by accepting and completing quests.
Quests will both teach the player how to play the game and progress the plot.
Some quests will have to be first found by interacting with other programmed characters and then accepted.
The player motivation is to make their character better as the plot unfolds by making their skill number and level higher.
Quests do not have to be accepted, but some skills are only rewarded for completing quests, so the most rewarding game experience is to complete all quests.
Skills belong under two categories: Experience skills and Quest Skills:
    Experience skills are acquired by completing x quests. ...if len(completed_quests)<=x:  skills+= 'expskill'
    Quest skills are acquired by completing specific quests. ...if 'questname' in completed_quests: skills+= 'questskill'
Players do not win in the sense that 'You Win!' appears, but rather in the sense that 'The End' appears.


Sources:

These sources helped me get a sense of the behavior of eagles - what they eat, how much they can carry, their behavior, how they fight and hunt
- https://www.eagles.org/what-we-do/educate/learn-about-eagles/bald-eagles-current-dangers/#toggle-id-8
- http://www.munseysbearcamp.com/eagle.html
- http://www.baldeagleinfo.com/eagle/eagle7.html
- https://kimmiddleton.com/blog/35990/bald-eagles-vs-golden-eagles
- https://www.nationaleaglecenter.org/learn/faq/

Indispensable to my project was 'stack overflow python', essentially the yahoo answers of pyhton. Would never have been able to do what I did without it.
Most of the things I learned during this project I learned in stack overflow, it would be impossible to paste all the links to each thread.

the Google Classroom : for reminders on classes, functions, lists

Presentation:
https://docs.google.com/presentation/d/1nbIkB8WnAKJFRIhkoUAF3NKD9vmIHAhFjY3_-zGee8M/edit?usp=sharing

Flow Chart:
https://drive.google.com/file/d/1hBXVIAMiARVJBh1yeWMmshZqgtMY2ZyB/view?usp=sharing

