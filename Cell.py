class Cell:
    """Storing the information that comprises each cell"""
    def __init__(self):
        """Sets up the initial variables"""
        self.cell_status = False  # Whether the cell is alive or dead
        self.cell_history = [[False, 0]]  # The history of the cell

    def update_history(self, next_gen):
        """Updating the history of the cell"""
        if self.cell_status != next_gen:  # If the cell status is not what it is destined to be
            self.cell_status = next_gen  # Change the cell status
            self.cell_history.append([True, 0] if self.cell_status else [False, 0])  # Wire new cell status into history

        else:  # If the cell status is still what it is destined to be
            self.cell_history[-1][1] += 1  # Add one onto the last history value input
