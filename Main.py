from Algorithm import Environment
from Display import Interface
from time import sleep


class GameOfLife:
    """Three dimensional game of life with the z axis as time"""

    @staticmethod
    def run(cell_numbers, generation_delay, generations, size, not_bordered):
        """Run the Game of Life according to inputted values using the environment and interface classes"""
        interface = Interface(cell_numbers, size)
        environment = Environment(cell_numbers, not_bordered)
        interface.generate_update(environment.world, environment.end)  # Update the interface with the parameters
        click = interface.click_pos(interface.win_c)  # Wait for a click from the user on the generated console

        while click == (1, 0) or click == (2, 0):  # While the interaction buttons are being clicked on, take actions
            if click == (1, 0):
                environment.change_specific(interface.click_pos(interface.win_s))  # Switch the clicked on cell's value
            elif click == (2, 0):
                environment.spawn_random()  # Switch all cell values randomly
            else:
                continue  # Placeholder for start button

            interface.generate_update(environment.world, environment.end)
            click = interface.click_pos(interface.win_c)  # Wait for another click and save the position

        for generation in range(generations):
            environment.next_generation()  # Get the next generation according to the algorithms
            environment.update_world_history()  # Update the storage files with the history changes
            sleep(generation_delay)
            interface.generate_update(environment.world, environment.end)  # Update the interface


GameOfLife.run((12, 12), 0.1, 100, 50, False)  # Start the game of life according to inputted values
