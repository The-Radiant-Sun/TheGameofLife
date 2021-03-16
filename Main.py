from Algorithim import Life
from Display import Interface
from time import sleep


class GameOfLife:
    """Holds the Game of Life"""

    @staticmethod
    def run(cell_numbers, generations, generation_delay, size):
        """Run the Game of Life"""
        display = Interface(cell_numbers, size)
        life = Life(cell_numbers)
        display.generate_update(life.world)
        while display.click_pos(display.win_c) == (1, 0):
            click_coord = display.click_pos(display.win_s)
            life.spawn_specific(click_coord)
            display.generate_update(life.world)

        for generation in range(generations):
            life.next_generation()
            display.generate_update(life.world)
            sleep(generation_delay)


GameOfLife.run((20, 10), 10, 0.1, 50)
