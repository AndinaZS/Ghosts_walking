from Unit import *
from Field import *
from Terrain import *

class Controller:
    def __init__(self, field, unit, map_print, ghost_image):
        self.game_on = True
        self.field = field
        self.unit = unit
        self.map_print = map_print
        self.ghost_image = ghost_image

    def play(self):
        self.field.field_drow(self.map_print, self.ghost_image)
        while self.game_on and self.unit.is_alive() and not self.unit.has_escaped():
            command = input('Введите команду ')
            if command == 'stop':
                self.game_on = False
            elif command == 'w':
                self.field.move_unit_up()
                self.field.field_drow(self.map_print, self.ghost_image)
            elif command == 's':
                self.field.move_unit_down()
                self.field.field_drow(self.map_print, self.ghost_image)
            elif command == 'a':
                self.field.move_unit_left()
                self.field.field_drow(self.map_print, self.ghost_image)
            elif command == 'd':
                self.field.move_unit_right()
                self.field.field_drow(self.map_print, self.ghost_image)

class Made_field():
    mapping = {
        'W': [Wall, '||'],
        'g': [Grass, '* '],
        'G': [Ghost, 'BU'],
        'K': [Key, '! '],
        'D': [Door, '[]'],
        'T': [Trap, '# ']
    }
    def __init__(self, maps: str, cols: int, rows: int):
        self.maps = maps
        self.cols = cols
        self.rows = rows
        self.field_cell = []
        self.field_print = []

    def create_field(self):
        for i in range(self.rows):
            elems_cell = [Cell(self.mapping[self.maps[i*self.cols+j]][0]()) for j in range(self.cols)]
            elems_print = [self.mapping[self.maps[i * self.cols + j]][1] for j in range(self.cols)]
            self.field_cell.append(elems_cell)
            self.field_print.append(elems_print)
        return self.field_cell

    def get_field_print(self):
        return self.field_print

    def get_cols(self):
        return self.cols

    def get_rows(self):
        return self.rows

    def Ghost_img(self):
        return self.mapping['G'][1]

class Main():
    def __init__(self):
        self.made_field = Made_field('WWWWgWWWWWWggggggggWWgTTTggDgWWKggggTggWWWWWWWWWWW', 10, 5)
        self.unit = Ghost('Ghost', (1, 1), 10)
        self.field = Field(self.made_field.create_field(), self.unit, self.made_field.get_cols(), self.made_field.get_rows())
        self.controller = Controller(self.field, self.unit, self.made_field.get_field_print(), self.made_field.Ghost_img())
        self.controller.play()

