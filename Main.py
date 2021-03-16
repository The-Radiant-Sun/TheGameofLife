from Algorithim import Life
from Display import Interface
from time import sleep


class GameOfLife:
    """Holds the Game of Life"""

    @staticmethod
    def run(cell_numbers, generations, generation_delay, size):
        """Run the Game of Life"""
        graphical_display = Interface(cell_numbers, size)
        life = Life(cell_numbers)
        graphical_display.generate_update(life.world)
        x = 0
        while x != 5:
            x += 1
            click_coord = graphical_display.click_pos()
            life.spawn_specific(click_coord)
            graphical_display.generate_update(life.world)

        for generation in range(generations):
            life.next_generation()
            graphical_display.generate_update(life.world)
            sleep(generation_delay)


GameOfLife.run((20, 10), 10, 0.25, 50)
