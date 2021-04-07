class Cell:
    """Contains all information and methods regarding the cells"""
    def __init__(self):
        """Sets up the initial variables"""
        self.cell_history = [[False, 0]]  # The total history of the cell

    def is_alive(self):
        """Return whether the cell is alive or not"""
        return self.cell_history[-1][0]

    def length_of_state(self):
        """Return how long the cell has been in its current state"""
        return self.cell_history[-1][1]

    def wipe_history(self):
        """Remove the filler history and the age of the states"""
        self.cell_history = [[False, 0], [True, 0]] if self.cell_history[-1] == [True, 0] else [[False, 0]]

    def increment_history(self):
        """Adds one generation to the current history without changing"""
        self.update_history(False)

    def update_history(self, change):
        """Updating the history of the cell depending on whether they need to change or not"""
        if change:  # If the cell needs to change
            self.cell_history.append([False, 0] if self.is_alive() else [True, 0])  # Change cell state in history
        else:
            self.cell_history[-1][1] += 1  # Increase the generation count for the current cell state

    def converted_data(self):
        """Return the cell data in condensed text format"""
        old = True if self.length_of_state() != 0 else False  # Whether the cell has maintained a state or is new
        return '{}'.format(('+' if old else '=') if self.is_alive() else ('-' if old else '.'))  # The age and state
