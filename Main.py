from Algorithim import Life
from Display import Interface
from time import sleep


class GameOfLife:
    """Holds the Game of Life"""
    @staticmethod
    def run(cell_number, spawn_coordinates, generations, generation_delay):
        """Run the Game of Life"""
        life = Life(cell_number, spawn_coordinates)
        graphical_display = Interface(cell_number, 50)
        for generation in range(generations):
            graphical_display.generate_update(life)
            sleep(generation_delay)


spawn_locations = [
    (1, 1),
    (1, 2),
    (1, 3),
    (5, 1),
    (5, 2),
    (6, 1),
    (5, 3)
]

GameOfLife.run(10, spawn_locations, 10, 1)
