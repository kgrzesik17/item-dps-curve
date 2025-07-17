import matplotlib.pyplot as plt
import numpy as np
import random
from Champion import *
from Item import *
from items import *

dps_list = []
price_list = [0]
items_to_check = [berserkers_greaves, yun_tal_wildarrows, infinity_edge, lord_dominiks_regards, rapid_firecannon, bloodthirster]

items_to_check.append('')
current_items = []
current_price = 0
level = 18

for i in items_to_check:
    champion = Champion("Sivir", level, current_items, 30, 4.45, 30, 1.3, 60, 2.5, 1.75, 0.625, 0.02, 0.625)
    enemy = Champion("Caitlyn", level, current_items, 30, 4.45, 30, 1.3, 60, 3.8, 1.75, 0.681, 0.04, 0.625)

    ad = champion.ad
    attack_speed = champion.attack_speed
    crit_chance = champion.crit_chance
    crit_damage = champion.crit_damage
    armor_penetration_percentage = champion.armor_penetration_percentage

    def is_crit(crit_chance):
            if random.randrange(0, 100) < crit_chance:
                return True
            else: 
                return False
            

    def hit(ad, crit_chance, crit_damage, armor, armor_penetration_percentage):
        armor = armor - (armor * armor_penetration_percentage)

        if(armor >= 0):
            physical_damage_multiplier = 100 / (100 + armor)
        else:
            physical_damage_multiplier = 2 - 100 / (100 - armor)

        if is_crit(crit_chance):
            return ad * crit_damage * physical_damage_multiplier
        else:
            return ad * physical_damage_multiplier

    def average_damage(ad, crit_chance, crit_damage, amount = 5000):
        full = 0

        for i in range(amount):
            full += hit(ad, crit_chance, crit_damage, enemy.armor, armor_penetration_percentage)

        output = full / amount

        return output

    dps = average_damage(ad, crit_chance, crit_damage) * attack_speed
    current_items.append(i)
    dps_list.append(round(dps))
    
for i in range(len(items_to_check) - 1):
    current_price += (items_to_check[i].price)
    price_list.append(current_price)

print(dps_list)
print(price_list)

xpoints = np.array(price_list)
ypoints = np.array(dps_list)

plt.plot(xpoints, ypoints)
plt.show()