class Item:
    def __init__(self, name: str, cost: int, damage: int, armor: int):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.armor = armor

    def __repr__(self):
        return self.name + '(' + str(self.cost) + ', ' + str(self.damage) + ', ' + str(self.armor) + ')'
