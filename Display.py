from graphics import *


class Interface:
    """The visuals for the Game of Life"""
    def __init__(self, cell_numbers, multiplier):
        self.cell_numbers = cell_numbers
        self.multiply = lambda x: x * multiplier
        self.win_c = GraphWin("Display", self.multiply(3), self.multiply(1))
        self.win_s = GraphWin("Display", self.multiply(self.cell_numbers[0]), self.multiply(self.cell_numbers[1]))

    def generate_update(self, world):
        """Updating the current window with the next generation"""
        for x in range(self.cell_numbers[0]):
            for y in range(self.cell_numbers[1]):
                cell = Rectangle(
                    Point(self.multiply(x), self.multiply(y)),
                    Point(self.multiply(x + 1), self.multiply(y + 1))
                )
                fill_colour = 'blue' if world[(x, y)] else 'red'
                cell.setFill(fill_colour)
                cell.draw(self.win_s)
                cell_number = Text(Point(self.multiply(x + 0.5), self.multiply(y + 0.5)), "({}, {})".format(x, y))
                cell_number.draw(self.win_s)

    def click_pos(self):
        """Returns the cell in which was clicked"""
        mouse_coordinates = self.win_s.getMouse()
        for cell_x in range(self.cell_numbers[0]):
            if mouse_coordinates.getX() / self.multiply(1) < cell_x + 1:
                for cell_y in range(self.cell_numbers[1]):
                    if mouse_coordinates.getY() / self.multiply(1) < cell_y + 1:
                        cell = (cell_x, cell_y)
                        return cell
