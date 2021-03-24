from Cell import Cell  # Use the cell class from cell
import random  # Use the random module


class Life:
    """Algorithms for Game of Life"""
    def __init__(self, cells):
        """Sets up the critical variables"""
        self.cells = cells  # The cell area to work within
        self.world = [[Cell() for y in range(self.cells[1])] for x in range(self.cells[0])]
        # The above line creates cell objects for each position within the world
        self.spawn = 3  # The number of surrounding cells that alive cells spawn at
        self.goldilocks = [2, 3]  # The lower and upper bounds for life to live
        self.end = False  # Whether or not the world will end
        self.world_history = None
        self.attempt_file_creation()
        self.update_world_history()

    def change_specific(self, cell_pos):
        """Switches a specific cells value"""
        cell = self.world[cell_pos[0]][cell_pos[1]]  # Selects the object stored in the selected position
        cell.update_history(not cell.cell_history[-1][0])  # Changes selected cell to its opposite

    def spawn_random(self):
        """Changes all cell values randomly"""
        # For each cell in the cell range
        for x in range(self.cells[0]):
            for y in range(self.cells[1]):
                if random.choice([True, False]):
                    self.change_specific((x, y))  # Change cell value to its opposite based on random chance

    def next_generation(self):
        """Calculates the next positions of life"""
        updates = []  # Updates to implement
        end_count = 0  # How close to the end the world is
        # For every coordinate in the cell range
        for x in range(self.cells[0]):
            for y in range(self.cells[1]):
                cell = self.world[x][y]  # Set cell to the object stored in that coordinate
                surroundings = self.test_surroundings((x, y))  # Store the number of alive cells around the chosen cell
                # If the cell is under the conditions to spawn or die
                if (surroundings == self.spawn and not cell.cell_status) or\
                        ((surroundings < self.goldilocks[0] or surroundings > self.goldilocks[1]) and cell.cell_status):
                    updates.append(cell)  # Add cell to list recording changes to implement
                # If cell is not alive
                if not cell.cell_status:
                    end_count += 1  # Add one to the end count
        # For all coordinates in the cell range
        for x in range(self.cells[0]):
            for y in range(self.cells[1]):
                cell = self.world[x][y]  # Set cell to the object stored in that coordinate
                cell.update_history(cell.cell_status if cell not in updates else not cell.cell_status)
                # The above line updates cell history based on whether they are in the updates list
        # If the end count is equal to the total number of cells
        if end_count == self.cells[0] * self.cells[1]:
            self.end = True  # The end becomes true

    def test_surroundings(self, cell_position):
        """Counts the surrounding cells"""
        cell_count = 0  # The number of cells surrounding cells
        # For every coordinate in the surroundings
        for x_shift in range(3):
            for y_shift in range(3):
                try:  # Attempt the following unless it returns a IndexError
                    scan_x = cell_position[0] + x_shift - 1  # The x_coordinate for the cell to scan
                    scan_y = cell_position[1] + y_shift - 1  # The y_coordinate for the cell to scan
                    # If the selected cell is off the screen or the original cell
                    if scan_x == -1 or scan_y == -1 or (x_shift - 1 == 0 and y_shift - 1 == 0):
                        continue
                    # If the selected cell is alive
                    if self.world[scan_x][scan_y].cell_status:
                        cell_count += 1  # Add one to the cell count

                except IndexError:
                    continue
        # Return the number of cells surrounding cell that are alive
        return cell_count

    def attempt_file_creation(self):
        try:
            self.world_history = open("World History", 'x')  # Allows for reading and writing of world history text
        except FileExistsError:
            self.world_history = open("World History", 'r+')

    def update_world_history(self):
        self.world_history.write(str(self.world))
