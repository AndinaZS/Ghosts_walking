from Unit import *
from Field import *

class Controller:
    def __init__(self, field, unit):
        self.game_on = True
        self.field = field
        self.unit = unit
        self.field.set_cell(self.unit.get_position(), self.unit)

    def play(self):
        self.field.field_print()
        while self.game_on and self.unit.is_alive() and not self.unit.has_escaped():
            command = input('Введите команду ')
            if command == 'stop':
                self.game_on = False
            elif command == 'w':
                self.field.move_unit_up()
                self.field.field_print()
            elif command == 's':
                self.field.move_unit_down()
                self.field.field_print()
            elif command == 'a':
                self.field.move_unit_left()
                self.field.field_print()
            elif command == 'd':
                self.field.move_unit_right()
                self.field.field_print()

class Made_field():
    mapping = {
        'W': Wall,
        'g': Grass,
        'G': Ghost,
        'K': Key,
        'D': Door,
        'T': Trap
    }
    def __init__(self, maps: str, cols: int, rows: int):
        self.maps = maps
        self.cols = cols
        self.rows = rows
        self.field_cell = []

    def create_field(self):
        for i in range(self.rows):
            elems = [Cell(self.mapping[self.maps[i*self.cols+j]]()) for j in range(self.cols)]
            self.field_cell.append(elems)
        return self.field_cell

    def get_cols(self):
        return self.cols

    def get_rows(self):
        return self.rows

class Main():
    def __init__(self):
        self.made_field = Made_field('WWWWWWWWWWWggggggggWWgTTTggDgWWKggggTggWWWWWWWWWWW', 10, 5)
        self.unit = Ghost('Ghost', (1, 1), 10)
        self.field = Field(self.made_field.create_field(), self.unit, self.made_field.get_cols(), self.made_field.get_rows())
        self.controller = Controller(self.field, self.unit)
        self.controller.play()
        self.field.field_print()
