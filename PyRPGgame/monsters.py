import random


def goblin(self):
    self.name = 'Goblin'
    self.desc = 'Somewhat low level monster, they\'re quite easy to beat unless you\'re really weak. Also They\'re green.'
    self.maxhealth = 90
    self.health = self.maxhealth
    self.attack = 8
    self.gold_get = 2
    self.level = random.randint(1, 3)
    self.exp = int(self.level * 1.5)

def skeleton(self):
    self.name = 'Skeleton'
    self.desc = 'The mob least suitable for stealth missions due to the rattling noise they make whenever they move.'
    self.maxhealth = 100
    self.health = self.maxhealth
    self.attack = 10
    self.gold_get = 4
    self.level = random.randint(1, 3)
    self.exp = int(self.level * 1.5)
