class Files:
    def __init__(self):
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
        """Add the data to two files, one that is for the machine, one that is for the user"""
        self.world_history.write("{}|{}/".format(world_size[0], world_size[1]))
        for y in range(world_size[1]):
            for x in range(world_size[0]):
                self.world_history.write(world[x][y].converted_data())  # For every position store the converted data
                self.user_world_history.write('0 ' if world[x][y].is_alive() else '* ')  # Make a user-friendly version
            self.user_world_history.write('\n')
        self.world_history.write('\n')
        self.user_world_history.write('\n')

    def return_world_history(self, generation):
        """Read and return the stored data"""
        variants = [[]]  # Storage for x and y changes
        state = self.file_data[generation].split('/')  # The different data sides
        world_size = state[0].split('|')  # The stored world size
        world_size = (int(world_size[0]), int(world_size[1]))
        for count, sub_state in enumerate(state[1]):
            if count % (world_size[1]) == 0 and count != 0:
                variants.append([])  # Create the y positions
            alive = True if sub_state == '+' or sub_state == '=' else False  # Whether it is alive
            old = True if sub_state == '+' or sub_state == '-' else False  # Whether it is old
            variants[-1].append([True if alive else False, True if old else False])  # Add the data
        return [world_size, variants]
