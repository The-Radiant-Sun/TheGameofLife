class Files:
    def __init__(self, use_file):
        self.user_world_history = None  # Empty world history for user to view
        self.world_history = None  # Begins with empty world history to use in files
        self.starter_history = None
        self.attempt_file_creation(use_file)  # Creates new file if one does not exist

    def attempt_file_creation(self, use_file):
        """Save world_history as a file if it already exists, otherwise make a new one"""
        try:  # Allows for reading and writing of files text
            self.world_history = open("World History.txt", 'x')
            self.user_world_history = open("User World History.txt", 'x')
        except FileExistsError:  # If the cell already exists open it to read and write
            self.starter_history = open("World History.txt", 'r').readline() if use_file else None
            print(self.starter_history)
            self.world_history = open("World History.txt", 'w+')
            self.user_world_history = open("User World History.txt", 'w+')

    def update_world_history(self, world_size, world):
        self.world_history.write("{},{}".format(world_size[0], world_size[1]))
        for y in range(world_size[1]):
            for x in range(world_size[0]):
                self.world_history.write(world[x][y].converted_data())
                self.user_world_history.write('0 ' if world[x][y].is_alive() else '* ')
            self.user_world_history.write('\n')
        self.world_history.write('\n')
        self.user_world_history.write('\n')

    def implement_world_history(self):
        variants = [[]]
        world_size = (0, 0)
        if self.starter_history is not None:
            for count, state in enumerate(self.starter_history.split("/")):
                if count == 0:
                    world_size = tuple(int(value) for value in state.split(','))
                if count - 1 == world_size:
                    variants.append([])
                variants[-1].append(True if state == 't' else False)
        return world_size, variants
