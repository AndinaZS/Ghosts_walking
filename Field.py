from Terrain import *

class Field:
    def __init__(self, field, unit, cols, rows):
        self.field = field
        self.unit = unit
        self.cols = cols
        self.rows = rows

    def cell(self, coords):
        return self.field[coords[0]][coords[1]]

    def is_walc(self, coords):
        cell = self.cell(coords)
        obj = cell.get_obj()
        return obj.is_walkable()

    def change_hero(self, coords):
        cell = self.cell(coords)
        obj = cell.get_obj()
        obj.step_on(self.unit)

    def move_unit_right(self):
        x, y = self.unit.get_position()
        if y + 1 == self.get_cals() or not self.is_walc((x, y + 1)):
            print('No path')
        else:
            self.successful_step((x, y), (x, y + 1))

    def move_unit_left(self):
        x, y = self.unit.get_position()
        if y - 1 < 0 or not self.is_walc((x, y - 1)):
            print('No path')
        else:
            self.successful_step((x, y), (x, y - 1))

    def move_unit_down(self):
        x, y = self.unit.get_position()
        if x + 1 == self.get_rows() or not self.is_walc((x + 1, y)):
            print('No path')
        else:
            self.successful_step((x, y), (x + 1, y))

    def move_unit_up(self):
        x, y = self.unit.get_position()
        if x - 1 < 0 or not self.is_walc((x - 1, y)):
            print('No path')
        else:
            self.successful_step((x, y), (x - 1, y))

    # def is_door(self, coord):
    #     current = Grass()
    #     cell = self.cell(coords)
    #     obj = cell.get_obj()
    #     if type(obj) == Door:
    #         next = Door()


    def successful_step(self, old_coord, new_coord):
        self.change_hero(new_coord)
        self.unit.set_position(new_coord)
        self.set_cell(old_coord, Grass())
        self.set_cell(new_coord, self.unit)

    def set_cell(self, coord, obj):
        self.field[coord[0]][coord[1]] = Cell(obj)

    def get_field(self):
        return self.field

    def get_cals(self):
        return self.cols

    def get_rows(self):
        return self.rows

    def field_print(self):
        for el in self.field:
            for e in el:
                print(e.get_obj(), end=' ')
            print()
