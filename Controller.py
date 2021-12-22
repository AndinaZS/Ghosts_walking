from Unit import *
from Field import *

class Controller:
    def __init__(self):
        self.mapping={
        'W': Wall,
        'g': Grass,
        'G': Ghost,
        'K': Key,
        'D': Door,
        'T': Trap
        }
        self.game_on = True
        self.hero = None
        self.fild = None

    def make_field(self, levelinfo='WWWWWWWWWWWggggggggWWgTTTggDgWWKggggTggWWWWWWWWWWW', col=10, row=5):
        field_cell = []
        self.col = col
        self.row = row
        for i in range(self.row):
            elems = [Cell(self.mapping[levelinfo[i*self.col+j]]()) for j in range(self.col)]
            field_cell.append(elems)
        self.field = Field(field_cell, self.hero, self.col, self.row)

    def play(self):
        self.hero = Ghost('Ghost', (1, 1), 10)
        self.make_field()
        self.field.set_cell(self.hero.get_position(), self.hero)
        self.field.field_print()


        while self.game_on and self.hero.is_alive() and not self.hero.has_escaped():
            command = input('Введите команду ')
            if command == 'stop':
                self.game_on = False
            elif command == 'w':
                self.fild.move_unit_up()
                self.fild.fild_print()
            elif command == 's':
                self.fild.move_unit_down()
                self.fild.fild_print()
            elif command == 'a':
                self.fild.move_unit_left()
                self.fild.fild_print()
            elif command == 'd':
                self.fild.move_unit_right()
                self.fild.fild_print()
