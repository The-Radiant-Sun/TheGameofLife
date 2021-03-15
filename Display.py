from graphics import *


class Interface:
    """The visuals for the Game of Life"""
    def __init__(self, cell_number, multiplier):
        self.cell_number = cell_number
        self.multiply = lambda x: x * multiplier
        self.win = GraphWin("Display", self.multiply(self.cell_number), self.multiply(self.cell_number))

    def generate_update(self, life):
        """Updating the current window with the next generation"""
        for x in range(self.cell_number):
            for y in range(self.cell_number):
                cell = Rectangle(
                    Point(self.multiply(x), self.multiply(y)),
                    Point(self.multiply(x + 1), self.multiply(y + 1))
                )
                fill_colour = 'blue' if life.world[(x, y)] else 'red'
                cell.setFill(fill_colour)
                cell.draw(self.win)
                cell_number = Text(Point(self.multiply(x + 0.5), self.multiply(y + 0.5)), "({}, {})".format(x, y))
                cell_number.draw(self.win)
        life.next_generation()

    def click_pos(self):
        """Returns the cell in which was clicked"""
        mouse_coordinates = self.win.getMouse() / self.multiply(1)
        for cell_x in range(self.cell_number):
            if mouse_coordinates[0] < cell_x:
                for cell_y in range(self.cell_number):
                    if mouse_coordinates[1] < cell_y:
                        cell = (cell_x, cell_y)
                        return cell
