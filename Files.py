class Files:
    def __init__(self, use_file):
        self.user_world_history = None  # Empty world history for user to view
        self.world_history = None  # Begins with empty world history to use in files
        self.file_data = None
        self.attempt_file_creation()  # Creates new file if one does not exist

    def attempt_file_creation(self):
        """Save world_history as a file if it already exists, otherwise make a new one"""
        try:  # Allows for reading and writing of files text
            self.world_history = open("World History.txt", 'x')
            self.user_world_history = open("User World History.txt", 'x')
        except FileExistsError:  # If the cell already exists open it to read and write
            self.world_history = open("World History.txt", 'r')
            self.file_data = [line for line in self.world_history.readlines()]
            self.world_history = open("World History.txt", 'w+')
            self.user_world_history = open("User World History.txt", 'w+')

    def update_world_history(self, world_size, world):
        self.world_history.write("{}|{}/".format(world_size[0], world_size[1]))
        for y in range(world_size[1]):
            for x in range(world_size[0]):
                self.world_history.write(world[x][y].converted_data())
                self.user_world_history.write('0 ' if world[x][y].is_alive() else '* ')
            self.user_world_history.write('\n')
        self.world_history.write('\n')
        self.user_world_history.write('\n')

    def return_world_history(self, generation):
        variants = [[]]
        state = self.file_data[generation].split('/')
        world_size = state[0].split('|')
        world_size = (int(world_size[0]), int(world_size[1]))
        for count, sub_state in enumerate(state[1]):
            if count % (world_size[1]) == 0 and count != 0:
                variants.append([])
            alive = True if sub_state == '+' or sub_state == '=' else False
            old = True if sub_state == '+' or sub_state == '-' else False
            variants[-1].append([True if alive else False, True if old else False])
        return [world_size, variants]
