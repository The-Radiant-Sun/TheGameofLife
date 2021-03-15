from Algorithim import Life
from Display import Interface
from time import sleep


class GameOfLife:
    """Holds the Game of Life"""
    @staticmethod
    def run(cell_number, generations, generation_delay, size):
        """Run the Game of Life"""
        spawn_coordinates = []
        graphical_display = Interface(cell_number, size)
        life = Life(cell_number, spawn_coordinates)
        x = 0
        while x != 5:
            x += 1
            click_coord = graphical_display.click_pos()
            spawn_coordinates.append(click_coord)

        for generation in range(generations):
            graphical_display.generate_update(life)
            sleep(generation_delay)


GameOfLife.run(10, 10, 1, 50)
