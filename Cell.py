class Cell:
    """Storing the information that comprises each cell"""
    def __init__(self, pos):
        self.cell_status = False
        self.cell_pos = pos
        self.cell_history = [[False, 0]]

    def update_history(self, next_gen):
        """Updating the history of the cell"""
        if self.cell_status != next_gen:
            self.cell_status = next_gen

            new_history = [True, 0] if self.cell_status else [False, 0]
            self.cell_history.append(new_history)

        else:
            self.cell_history[-1][1] += 1
