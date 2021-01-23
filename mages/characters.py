# AUTOGENERATED! DO NOT EDIT! File to edit: 00_characters.ipynb (unless otherwise specified).

__all__ = ['Ability', 'Character', 'Mage', 'Demon']

# Cell
import random

# Cell
class Ability:
    ability_types = ["fire", "water"]

    def __init__(self, damage, damage_type):
        self.damage = damage
        self.damage_type = damage_type

    def __str__(self):
        if self.damage_type == "fire":
            return "a jet of fire shot towards"
        elif self.damage_type == "water":
            return "ice cold water is flung towards"

# Cell
class Character:
    def __init__(self, name, max_health, ability):
        self.name = name
        self.max_health = max_health
        self.current_health = max_health
        self.ability = ability
        self.level = 1

    def __str__(self):
        return f"""\
        {self.name}'s Current Health: {self.current_health}
        {self.name}'s Max Health: {self.max_health}
        {self.name}'s Ability Damage: {self.ability.damage}
        {self.name}'s Ability Type: {self.ability.damage_type}
        """

# Cell
class Mage(Character):
    def __init__(self, name, max_health, ability):
        super().__init__(name, max_health, ability)

    def attack(self, target):
        print(f"From {self.name}'s wand, {self.ability} {target.name}.")
        target.current_health -= self.ability.damage

    def level_up(self):
        self.level += 1
        self.max_health = self.max_health * self.level
        self.current_health = self.max_health
        self.ability.damage = self.ability.damage * self.level

# Cell
class Demon(Character):
    def __init__(self, name, max_health):
        super().__init__(name, max_health, Ability(10, "fire"))

    def attack(self, target):
        print(f"From {self.name}'s wand, {self.ability} {target.name}.")
        target.current_health -= self.ability.damage