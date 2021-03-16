class Cell:
    def __init__(self, pos):
        self.cell_status = False
        self.new_status = False
        self.cell_pos = pos
        self.cell_history = [['Dead', 0]]

    def update_history(self):
        if self.cell_status != self.new_status:
            new_history = ['Alive', 0] if self.cell_status else ['Dead', 0]
            self.cell_history.append(new_history)
            self.cell_status = self.new_status
        else:
            self.cell_history[1] += 1
