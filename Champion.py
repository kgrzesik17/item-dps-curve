import random

class Champion:
    def __init__(self, name, level, items, armor, armor_per_level, mr, mr_per_level, ad, ad_per_level, crit_damage, base_attack_speed, bonus_attack_speed, as_ratio):
       self.name = name
       self.level = level
       self.armor = armor + armor_per_level * (level - 1)
       self.mr = mr + mr_per_level * (level - 1)
       self.ad = ad + ad_per_level * (level - 1)
       self.crit_damage = crit_damage
       self.bonus_attack_speed = bonus_attack_speed * (self.level - 1)
       self.crit_chance = 0
       self.armor_penetration_percentage = 0
       
       for item in items:
           self.ad += item.ad
           self.bonus_attack_speed += item.attack_speed
           self.crit_damage += item.crit_damage 
           self.armor += item.armor
           self.mr += item.mr
           self.crit_chance += item.crit_chance
           self.armor_penetration_percentage += item.armor_penetration_percentage 

       self.attack_speed = as_ratio * self.bonus_attack_speed + base_attack_speed
       self.items = items

