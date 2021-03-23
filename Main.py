from Algorithim import Life
from Display import Interface
from time import sleep


class GameOfLife:
    """Add comments"""
    """Holds the Game of Life"""

    @staticmethod
    def run(cell_numbers, generations, generation_delay, size):
        """Run the Game of Life"""
        display = Interface(cell_numbers, size)
        life = Life(cell_numbers)
        display.generate_update(life.world, life.end)
        click = display.click_pos(display.win_c)

        while click == (1, 0) or click == (2, 0):
            if click == (1, 0):
                click_coord = display.click_pos(display.win_s)
                life.change_specific(click_coord)

            if click == (2, 0):
                life.spawn_random()

            display.generate_update(life.world, life.end)
            click = display.click_pos(display.win_c)

        for generation in range(generations):
            life.next_generation()
            display.generate_update(life.world, life.end)
            sleep(generation_delay)


GameOfLife.run((20, 10), 25, 0.5, 50)
