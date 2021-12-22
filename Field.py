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
            print('Не пройти!')
        else:
            self.successful_step((x, y + 1))

    def move_unit_left(self):
        x, y = self.unit.get_position()
        if y - 1 < 0 or not self.is_walc((x, y - 1)):
            print('Не пройти!')
        else:
            self.successful_step((x, y - 1))

    def move_unit_down(self):
        x, y = self.unit.get_position()
        if x + 1 == self.get_rows() or not self.is_walc((x + 1, y)):
            print('Не пройти!')
        else:
            self.successful_step((x + 1, y))

    def move_unit_up(self):
        x, y = self.unit.get_position()
        if x - 1 < 0 or not self.is_walc((x - 1, y)):
            print('Не пройти!')
        else:
            self.successful_step((x - 1, y))

    def successful_step(self, new_coord):
        self.change_hero(new_coord)
        self.unit.set_position(new_coord)

    def get_field(self):
        return self.field

    def get_cals(self):
        return self.cols

    def get_rows(self):
        return self.rows

    def field_drow(self, map_print, ghost_img):
        x, y = self.unit.get_position()
        maps = list(map(list, map_print))
        maps[x][y] = ghost_img
        for el in maps:
            for e in el:
                print(e, end=' ')
            print()
        maps.clear()
