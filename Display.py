from graphics import *


class Interface:
    """The visuals for the Game of Life"""
    def __init__(self, cell_numbers, multiplier):
        self.cell_numbers = cell_numbers
        self.multiply = lambda x: x * multiplier
        self.win_c = GraphWin("Console", self.multiply(4), self.multiply(1))
        self.generate_console()
        self.win_s = GraphWin("Screen", self.multiply(self.cell_numbers[0]), self.multiply(self.cell_numbers[1]))

    @staticmethod
    def enact(colour, shape, window):
        n_gon = shape
        n_gon.setFill(colour)
        n_gon.draw(window)

    def point_gen(self, xy):
        """Generates a point based upon a set of multiplied x and y values"""
        return Point(self.multiply(xy[0]), self.multiply(xy[1]))

    def generate_update(self, world, end):
        """Updating the current window with the next generation or closing if no generation"""
        if end:
            self.win_c.close()
            self.win_s.close()
            sys.exit()

        for x in range(self.cell_numbers[0]):
            for y in range(self.cell_numbers[1]):
                cell = world[x][y]

                if cell.cell_history[-1][1] == 0 or (cell.cell_history[-1][1] == 1 and cell.cell_status):
                    cell_display = Rectangle(self.point_gen((x, y)), self.point_gen((x + 1, y + 1)))

                    if cell.cell_status:
                        fill_colour = 'lightgreen' if cell.cell_history[-1][1] == 0 else 'darkgreen'
                    else:
                        fill_colour = 'darkred'

                    cell_display.setFill(fill_colour)
                    cell_display.draw(self.win_s)

    def click_pos(self, window):
        """Returns the cell in which was clicked"""
        mouse_coordinates = window.getMouse()
        for cell_x in range(self.cell_numbers[0]):
            if mouse_coordinates.getX() / self.multiply(1) < cell_x + 1:

                for cell_y in range(self.cell_numbers[1]):
                    if mouse_coordinates.getY() / self.multiply(1) < cell_y + 1:
                        cell_pos = (cell_x, cell_y)
                        return cell_pos

    def generate_console(self):
        def triangle_gen(p1, p2, p3):
            return [self.point_gen(p1), self.point_gen(p2), self.point_gen(p3)]

        self.enact('blue', Polygon(triangle_gen((0, 0.5), (1, 0), (1, 1))), self.win_c)
        self.enact('red', Circle(self.point_gen((1.5, 0.5)), self.multiply(0.5)), self.win_c)
        self.enact('green', Circle(self.point_gen((2.5, 0.5)), self.multiply(0.5)), self.win_c)
        self.enact('blue', Polygon(triangle_gen((4, 0.5), (3, 0), (3, 1))), self.win_c)
