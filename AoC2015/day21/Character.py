class Character:

    def __init__(self, hp: int, damage: int, armor: int):
        self.hp = hp
        self.damage = damage
        self.armor = armor

    def __repr__(self):
        return '[' + str(self.hp) + ', ' + str(self.damage) + ', ' + str(self.armor) + ']'

    def __eq__(self, other):
        return self.hp == other.hp and self.damage == other.damage and self.armor == other.armor
