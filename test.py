def drow_field(fild, coord):
    mapping = {
        'Wall': '🔲',
        'Grass': '⬜️',
        'Ghost': '👻',
        'Key': '🗝',
        'Door': '🚪',
        'Trap': '💀',
    }

    cell = self.cell((i,j))
    obj = cell.get_obj()