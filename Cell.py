class Cell:
    def __init__(self, pos):
        self.cell_status = False
        self.new_status = False
        self.cell_pos = pos
        self.cell_history = ['Dead', 0]

    def update_history(self):
        if self.cell_status != self.new_status:
            self.cell_history[0] = 'Alive' if self.cell_status else 'Dead'
            self.cell_history[1] = 0
            self.cell_status = self.new_status
        else:
            self.cell_history[1] += 1
