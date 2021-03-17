from Cell import Cell
import random


class Life:
    """Algorithms for Game of Life"""
    def __init__(self, cells):
        self.alive, self.dead = True, False
        self.cells = cells
        self.world = [[Cell((x, y)) for y in range(self.cells[1])] for x in range(self.cells[0])]
        self.spawn = 3
        self.goldilocks = [2, 3]

    def change_specific(self, cell_pos):
        """Spawns a specific cell"""
        cell = self.world[cell_pos[0]][cell_pos[1]]
        cell.update_history(not cell.cell_history[-1][0])

    def spawn_random(self):
        for x in range(self.cells[0]):
            for y in range(self.cells[1]):
                if random.choice([True, False]):
                    self.change_specific((x, y))

    def next_generation(self):
        """Calculates the next positions of life"""
        updates = []
        for x in range(self.cells[0]):
            for y in range(self.cells[1]):
                cell = self.world[x][y]
                surroundings = self.test_surroundings((x, y))

                if surroundings == self.spawn and not cell.cell_status:
                    updates.append(cell)
                if (surroundings < self.goldilocks[0] or surroundings > self.goldilocks[1]) and cell.cell_status:
                    updates.append(cell)

        for x in range(self.cells[0]):
            for y in range(self.cells[1]):
                cell = self.world[x][y]
                change = cell.cell_status if cell not in updates else not cell.cell_status
                cell.update_history(change)

    def test_surroundings(self, cell_position):
        """Counts the surrounding cells"""
        cell_count = 0
        for x_shift in range(3):
            for y_shift in range(3):

                try:
                    if self.world[cell_position[0] + x_shift - 1][cell_position[1] + y_shift - 1].cell_status:
                        if x_shift - 1 == 0 and y_shift - 1 == 0:
                            continue
                        cell_count += 1

                except IndexError:
                    continue

        return cell_count
