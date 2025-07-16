# import matplotlib.pyplot as plt
# import numpy as np
import random
from Champion import *
from Item import *
from items import *

dps_list = []
items_to_check = [berserkers_greaves, yun_tal_wildarrows, infinity_edge, lord_dominiks_regards, rapid_firecannon]

items_to_check.append('')
current_items = []

for i in items_to_check:
    caitlyn = Champion("Caitlyn", 18, current_items, 27, 4.7, 30, 1.3, 60, 3.8, 1.75, 0.681, 0.04, 0.625)

    ad = caitlyn.ad
    attack_speed = caitlyn.attack_speed
    crit_chance = caitlyn.crit_chance
    crit_damage = caitlyn.crit_damage

    def is_crit(crit_chance):
            if random.randrange(0, 100) < crit_chance:
                return True
            else: 
                return False
            

    def hit(ad, crit_chance, crit_damage):
        if is_crit(crit_chance):
            return ad * crit_damage
        else:
            return ad 

    def average_damage(ad, crit_chance, crit_damage, amount = 5000):
        full = 0

        for i in range(amount):
            full += hit(ad, crit_chance, crit_damage)

        output = full / amount

        return output

    dps = average_damage(ad, crit_chance, crit_damage) * attack_speed

    current_items.append(i)
    dps_list.append(round(dps))

print(dps_list)

# xpoints = np.array([1, 3, 1, 8])
# ypoints = np.array([3, 10, -2, 14])

# plt.plot(xpoints, ypoints)
# plt.show()