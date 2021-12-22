class Unit:
    def __init__(self, coord, hp):
        self.coord = coord
        self.hp = hp
        self.got_key = False
        self.escaped = False

    def get_position(self):
        return self.coord

    def set_position(self, coords):
        self.coord = (coords[0], coords[1])

    def get_hp(self):
        return self.hp

    def set_hp(self, new_value):
        self.hp = new_value

    def get_damage(self, set_value):
        self.hp -= set_value
        print(f'Вы получили урон {set_value}. Осталось {self.get_hp()}hp')
        if not self.is_alive():
            print('Игра закончена, персонаж умер')

    def has_key(self):
        return self.got_key

    def set_key(self):
        self.got_key = True
        print('Вы получили ключ, осталось найти дверь.')

    def has_escaped(self):
        return self.escaped

    def set_escaped(self):
        self.escaped = True

    def is_alive(self):
        if self.hp > 0:
            return True

class Ghost(Unit):
    def __init__(self, name, coord, hp):
        super().__init__(coord, hp)
        self.name = name
        self.hp = hp

    def __str__(self):
        return 'Bu'


