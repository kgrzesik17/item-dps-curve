class Item:
    def __init__(self, name = 0, price = 0, ad = 0, crit_chance = 0, crit_damage = 0, attack_speed = 0, armor = 0, mr = 0, armor_penetration_percentage = 0):
        self.name = name
        self.ad = ad
        self.crit_chance = crit_chance
        self.crit_damage = crit_damage
        self.attack_speed = attack_speed
        self.armor = armor
        self.mr = mr
        self.armor_penetration_percentage = armor_penetration_percentage
        self.price = price