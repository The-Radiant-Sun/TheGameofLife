from Cell import Cell  # Use the cell class from cell
import random  # Use the random module


class Environment:
    """Algorithms for Game of Life"""
    def __init__(self, world_size):
        """Sets up the critical variables and actions"""
        self.world_size = world_size
        # Create cell objects for each position within the world
        self.world = [[Cell() for y in range(self.world_size[1])] for x in range(self.world_size[0])]
        self.spawn = 3  # The number of surrounding cells that alive cells spawn at
        self.goldilocks = [2, 3]  # The lower and upper bounds for life to stay living
        self.end = False  # Whether or not the world will end
        """self.world_history = None  # Begins with empty world history to use in files
        self.attempt_file_creation()
        self.update_world_history()"""

    def change_specific(self, cell_pos):
        """Switches a specific cells value"""
        cell = self.world[cell_pos[0]][cell_pos[1]]  # Selects the object stored in the selected position
        cell.update_history(True)  # Changes selected cell to its opposite
        cell.wipe_history()

    def spawn_random(self):
        """Changes all cell values randomly"""
        for x in range(self.world_size[0]):  # For each cell in the world
            for y in range(self.world_size[1]):
                if random.choice([True, False]):
                    self.change_specific((x, y))  # Change cell value to its opposite based on random chance

    def next_generation(self):
        """Calculates the next positions of life"""
        updates = []  # Updates to implement
        end_count = 0  # How close to the end the world is

        for x in range(self.world_size[0]):  # For every coordinate in the cell range
            for y in range(self.world_size[1]):
                cell = self.world[x][y]  # Set cell to the object stored in that coordinate
                surroundings = self.test_surroundings((x, y))  # Store the number of alive cells around the chosen cell
                # If the cell is under the conditions to spawn or die
                if (surroundings == self.spawn and not cell.is_alive()) or\
                        ((surroundings < self.goldilocks[0] or surroundings > self.goldilocks[1]) and cell.is_alive()):
                    updates.append(cell)  # Add cell to list recording changes to implement
                # If cell is not alive
                if not cell.is_alive():
                    end_count += 1  # Add one to the end count

        for x in range(self.world_size[0]):  # For all coordinates in the cell range
            for y in range(self.world_size[1]):
                cell = self.world[x][y]  # Set cell to the object stored in that coordinate
                # Updates cell history based on whether they are in the updates list
                if cell in updates:
                    cell.update_history(True)
                else:
                    cell.update_history()
        # If the end count is equal to the total number of cells
        if end_count == self.world_size[0] * self.world_size[1]:
            self.end = True  # The end becomes true

    def test_surroundings(self, cell_position):
        """Counts the surrounding cells"""
        cell_count = 0  # The number of cells surrounding the origin cell
        for x_shift in range(3):  # For every coordinate in the surroundings
            for y_shift in range(3):
                try:  # Attempt the following unless it returns a IndexError
                    scan_x = cell_position[0] + x_shift - 1  # The x_coordinate for the cell to scan
                    scan_y = cell_position[1] + y_shift - 1  # The y_coordinate for the cell to scan

                    if scan_x == -1 or scan_y == -1 or (x_shift - 1 == 0 and y_shift - 1 == 0):
                        continue  # Continue if the selected cell is off the screen or the original cell
                    if self.world[scan_x][scan_y].is_alive():  # If the selected cell is alive
                        cell_count += 1

                except IndexError:
                    continue
        # Return the number of cells surrounding cell that are alive
        return cell_count

    """def attempt_file_creation(self):
        """"""Save world_history as a file if it already exists, otherwise make a new one""""""
        try:
            self.world_history = open("World History", 'x')  # Allows for reading and writing of world history text
        except FileExistsError:
            self.world_history = open("World History", 'r+')  # If the cell already exists open it to read and write

    def update_world_history(self):
        self.world_history.write(str(self.world))"""
