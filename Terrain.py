class Terrain:
    def __init__(self, terrain, walkable):
        self.terrain = terrain
        self.walkable = walkable

    def get_terrain(self):
        return self.terrain

    def is_walkable(self):
        return self.walkable

    def step_on(self, unit):
        pass

class Grass(Terrain):
    def __init__(self):
        super().__init__(terrain='grass', walkable=True)


class Wall(Terrain):
    def __init__(self):
        super().__init__(terrain='wall', walkable=False)


class Trap(Terrain):
    def __init__(self, damage=6):
        super().__init__(terrain='trap', walkable=True)
        self.damage = damage

    def step_on(self, unit):
        unit.get_damage(self.damage)

class Key(Terrain):
    def __init__(self):
        super().__init__(terrain='key', walkable=True)

    def step_on(self, unit):
        unit.set_key()


class Door(Terrain):
    def __init__(self):
        super().__init__(terrain='door', walkable=True)

    def step_on(self, unit):
        if unit.has_key():
            print('Игра окончена, побег удался')
            unit.set_escaped()
        else:
            print('Дверь - это хорошо, но нужен ключ')

class Cell:
    def __init__(self, obj):
        self.obj = obj

    def get_obj(self):
        return self.obj

    def set_obj(self, obj):
        self.obj = obj