from Files import Files  # Add a full file-relevant method to minimise init space
from Cell import Cell
import random


class Environment:
    """Algorithms for Game of Life"""
    def __init__(self, world_size, not_bordered, use_file):
        """Sets up the critical variables and actions"""
        self.files = Files()
        self.spawn = 3  # The number of surrounding cells that alive cells spawn at
        self.goldilocks = [2, 3]  # The lower and upper bounds for life to stay living
        self.not_bordered = not_bordered
        self.world_size = world_size
        self.end = False  # Whether or not the world will end
        self.world = self.generate_world()  # Create cell objects for each position within the world
        self.file_conversion(use_file)  # Change the variables if the files are meant to be used

    def generate_world(self):
        """Create cell objects for each position within the world"""
        return [[Cell() for y in range(self.world_size[1])] for x in range(self.world_size[0])]

    def change_specific(self, cell_pos):
        """Switches a specific cells value"""
        cell = self.world[cell_pos[0]][cell_pos[1]]  # Selects the object stored in the selected position
        cell.update_history(True)  # Changes selected cell to its opposite
        cell.wipe_history()  # Ensures that the cell history remains clean even after multiple switches

    def spawn_random(self):
        """Changes all cell values randomly"""
        for x in range(self.world_size[0]):  # For each cell in the world
            for y in range(self.world_size[1]):
                if random.choice([True, False]):
                    self.change_specific((x, y))  # Change cell value to its opposite based on random chance

    def next_generation(self):
        """Calculates the next positions of life"""
        updates = []  # Updates to implement

        for x in range(self.world_size[0]):  # For every coordinate in the cell range
            for y in range(self.world_size[1]):
                cell = self.world[x][y]  # Set cell to the object stored in that coordinate
                surroundings = self.test_surroundings((x, y))  # Store the number of alive cells around the chosen cell
                # If the cell is under the conditions to spawn or die
                if (surroundings == self.spawn and not cell.is_alive()) or\
                        ((surroundings < self.goldilocks[0] or surroundings > self.goldilocks[1]) and cell.is_alive()):
                    updates.append(cell)  # Add cell to list recording changes to implement

        for x in range(self.world_size[0]):  # For all coordinates in the cell range
            for y in range(self.world_size[1]):
                cell = self.world[x][y]  # Set cell to the object stored in that coordinate
                # Updates cell history based on whether they are in the updates list
                if cell in updates:
                    cell.update_history(True)
                else:
                    cell.increment_history()

        self.files.update_world_history(self.world_size, self.world)
        # If the end count is equal to the total number of cells
        if not updates:
            self.end = True  # The end becomes true

    def test_surroundings(self, cell_position):
        """Returns the number of alive surrounding cells"""
        cell_count = 0  # The number of cells surrounding the origin cell
        for x_shift in range(3):  # For every coordinate in the surroundings
            for y_shift in range(3):
                try:  # Attempt the following unless it returns a IndexError
                    scan_x = cell_position[0] + x_shift - 1  # The x_coordinate for the cell to scan
                    scan_y = cell_position[1] + y_shift - 1  # The y_coordinate for the cell to scan

                    if self.not_bordered:  # If the game is not bordered
                        scan_x = scan_x % self.world_size[0]  # Loop the scanned positions
                        scan_y = scan_y % self.world_size[1]

                    if scan_x == -1 or scan_y == -1 or (x_shift - 1 == 0 and y_shift - 1 == 0):
                        continue  # Continue if the selected cell is off the screen or the original cell
                    if self.world[scan_x][scan_y].is_alive():  # If the selected cell is alive
                        cell_count += 1

                except IndexError:
                    continue

        # Return the number of cells surrounding cell that are alive
        return cell_count

    def file_conversion(self, use_file):
        if use_file[0]:
            history = self.files.return_world_history(use_file[1])
            self.world_size = history[0]  # Sets the world size according to file data
            self.world = self.generate_world()
            for x in range(self.world_size[0]):  # For all coordinates in the cell range
                for y in range(self.world_size[1]):
                    filed_cell = history[1][x][y]  # Set filed_cell to the stored data at that point
                    if filed_cell[0]:
                        self.change_specific((x, y))  # If cell is recorded as alive, then make it so
                    if filed_cell[1]:
                        if not filed_cell[0]:
                            self.change_specific((x, y))
                            self.world[x][y].update_history(True)  # List cell as dead if it is recorded
                        else:
                            self.world[x][y].increment_history()  # Add history if it is recorded
