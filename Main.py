from Algorithm import Life  # Use the life class from algorithm
from Display import Interface  # Use the interface class from display


class GameOfLife:
    """Holds the Game of Life"""

    @staticmethod
    def run(cell_numbers, generations, size):
        """Run the Game of Life"""
        display = Interface(cell_numbers, size)  # Create the display object according to parameters
        life = Life(cell_numbers)  # Create the life object according to parameters
        display.generate_update(life.world, life.end)  # Update the display with the world and end from the life object
        click = display.click_pos(display.win_c)  # Wait for a click from the user on the generated console
        # While the click is on the pre-run buttons
        while click == (1, 0) or click == (2, 0):
            if click == (1, 0):  # If the first button is clicked
                life.change_specific(display.click_pos(display.win_s))  # Switch the clicked on cell's value

            if click == (2, 0):  # If the second button is clicked
                life.spawn_random()  # Switch all cell values randomly

            display.generate_update(life.world, life.end)  # Update the display
            click = display.click_pos(display.win_c)  # Wait for another click
        # For every generation in the inputted generation range
        for generation in range(generations):
            life.next_generation()  # Get the next generation according to the algorithms
            display.generate_update(life.world, life.end)  # Update the display


GameOfLife.run((40, 20), 100, 50)  # The inputted values to run the game of life
