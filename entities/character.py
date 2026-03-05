import json
from datetime import datetime

# Archive containing all information about the player
class Character:

    def __init__(self, name, character_class, healthpool, attack, defense, aps, level=1):
        self.name = name
        self.character_class = character_class
        self.healthpool = healthpool
        self.attack =  attack
        self.defense = defense
        self.aps = aps
        self.level = level

    def to_dict(self):
        return {
            "name": self.name,
            "class": self.character_class,
            "level": self.level,
            "hp": self.healthpool,
            "attack": self.attack,
            "defense": self.defense,
            "aps": self.aps
        }

    def save(self):
        now = datetime.now()
        filename = now.strftime("save/save%d%m%Y_%H%M.json")

        with open(filename, "w") as f:
            json.dump(self.to_dict(), f, indent=4)