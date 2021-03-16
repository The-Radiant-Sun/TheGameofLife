from graphics import *


class Interface:
    """The visuals for the Game of Life"""
    def __init__(self, cell_numbers, multiplier):
        self.cell_numbers = cell_numbers
        self.multiply = lambda x: x * multiplier
        self.win_c = GraphWin("Console", self.multiply(3), self.multiply(1))
        self.generate_console()
        self.win_s = GraphWin("Screen", self.multiply(self.cell_numbers[0]), self.multiply(self.cell_numbers[1]))

    def point_gen(self, xy):
        point = Point(self.multiply(xy[0]), self.multiply(xy[1]))
        return point

    def generate_update(self, world):
        """Updating the current window with the next generation"""
        for x in range(self.cell_numbers[0]):
            for y in range(self.cell_numbers[1]):
                if world[x][y].cell_history[-1][1] == 0:
                    cell = Rectangle(self.point_gen((x, y)), self.point_gen((x + 1, y + 1)))
                    fill_colour = 'green' if world[x][y].cell_status else 'red'
                    cell.setFill(fill_colour)
                    cell.draw(self.win_s)

    def click_pos(self, window):
        """Returns the cell in which was clicked"""
        mouse_coordinates = window.getMouse()
        for cell_x in range(self.cell_numbers[0]):
            if mouse_coordinates.getX() / self.multiply(1) < cell_x + 1:
                for cell_y in range(self.cell_numbers[1]):
                    if mouse_coordinates.getY() / self.multiply(1) < cell_y + 1:
                        cell = (cell_x, cell_y)
                        return cell

    def generate_console(self):
        def triangle_gen(p1, p2, p3):
            return [self.point_gen(p1), self.point_gen(p2), self.point_gen(p3)]

        left_arrow = Polygon(triangle_gen((0, 0.5), (1, 0), (1, 1)))
        left_arrow.setFill("blue")
        left_arrow.draw(self.win_c)
        center_circle = Circle(self.point_gen((1.5, 0.5)), self.multiply(0.5))
        center_circle.setFill("red")
        center_circle.draw(self.win_c)
        right_arrow = Polygon(triangle_gen((3, 0.5), (2, 0), (2, 1)))
        right_arrow.setFill("blue")
        right_arrow.draw(self.win_c)
