# import matplotlib.pyplot as plt
# import numpy as np
import random

ad = 100
attack_speed = 15
crit_chance = 50
crit_damage = 1.75  # 2.15 with IE 

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

dps = float(hit(ad, crit_chance, crit_damage)) * attack_speed

def average_damage(ad, crit_chance, crit_damage, amount = 5000):
    full = 0

    for i in range(amount):
        full += hit(ad, crit_chance, crit_damage)

    output = full / amount

    return output

print(average_damage(ad, crit_chance, crit_damage))


# xpoints = np.array([1, 3, 1, 8])
# ypoints = np.array([3, 10, -2, 14])

# plt.plot(xpoints, ypoints)
# plt.show()