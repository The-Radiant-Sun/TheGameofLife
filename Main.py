from Algorithm import Environment
from Display import Interface
from time import sleep


class GameOfLife:
    """Three dimensional game of life with the z axis as time"""
    def __init__(self):
        self.world_size = (self.get_input("World width: ", int), self.get_input("World height: ", int))
        self.generation_delay = self.get_input("Generation delay: ", float)
        self.generations = self.get_input("Number of generations: ", int)
        self.magnification = self.get_input("Magnification of cells: ", int)
        self.not_bordered = self.get_input("Bordered? Y/N: ", bool)
        self.file_use = self.get_input("Use previous save? Y/N: ", bool)
        self.use_file = [self.file_use, self.get_input("Generation of save: ", int) if self.file_use else 0]

    @staticmethod
    def get_input(question_1, answer_type_1):
        def request(question_2, answer_type_2):
            ans = input(question_2).lower()
            try:
                if answer_type_2 == bool:
                    if ans == 'y':
                        ans = True
                    else:
                        ans = False
                if answer_type_2 == list:
                    ans.split(', ')
                    ans[0] = int(ans[0])
                    ans[1] = int(ans[1])
                else:
                    ans = answer_type_2(ans)
            except ValueError:
                ans = request(question_2, answer_type_2)
            return ans
        return request(question_1, answer_type_1)

    def run(self):
        """Run the Game of Life according to inputted values using the environment and interface classes"""
        environment = Environment(self.world_size, self.not_bordered, self.use_file)
        interface = Interface(environment.world_size, self.magnification)
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
        # Update files with the start state
        environment.files.update_world_history(environment.world_size, environment.world)
        for generation in range(self.generations):
            environment.next_generation()  # Get the next generation according to the algorithms
            sleep(self.generation_delay)
            interface.generate_update(environment.world, environment.end)  # Update the interface


GameOfLife().run()  # Start the game of life according to inputted values
