class Life:
    """Algorithms for Game of Life"""
    def __init__(self, cells, spawn_coordinates):
        self.alive, self.dead = True, False
        self.cells = cells
        self.world = self.generate_blank(spawn_coordinates)
        self.spawn = 3
        self.keep = [2, 3]

    def generate_blank(self):
        """Generates the blank stage"""
        world = {}
        for y in range(self.cells):
            for x in range(self.cells):
                world[(x, y)] = self.dead
        return world

    def spawn_specific(self, cell_pos):
        """Spawns in a specific cell"""
        self.world[cell_pos] = self.alive

    def next_generation(self):
        """Calculates the next positions of life"""
        updates = []
        for y in range(self.cells):
            for x in range(self.cells):
                surroundings = self.test_surroundings((x, y))
                if surroundings == self.spawn and not self.world[(x, y)]:
                    updates.append([(x, y), True])
                if surroundings < self.keep[0] or surroundings > self.keep[1]:
                    updates.append([(x, y), False])
        for update in updates:
            self.world[update[0]] = update[1]

    def test_surroundings(self, cell_position):
        """Counts the surrounding cells"""
        cell_count = 0
        for x_shift in range(3):
            for y_shift in range(3):
                try:
                    if self.world[(cell_position[0] + x_shift - 1, cell_position[1] + y_shift - 1)]:
                        if x_shift - 1 == 0 and y_shift - 1 == 0:
                            continue
                        cell_count += 1
                except KeyError:
                    continue
        return cell_count
