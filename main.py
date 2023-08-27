from enum import Enum
from typing import Type


class Coordinate:
    def __init__(self, x: int, y: int):
        if not 0 <= x <= 8 and 0 <= y <= 8:
            raise ValueError('Координата выходит за пределы доски')
        self.x = x
        self.y = y



class Color(Enum):
    BLACK = 0
    WHITE = 1


class Board:
    def __init__(self):
        self.piece = []

class Figure:
    def __init__(self, coordinate: Coordinate, color: Color):
        self.coordinate = coordinate
        self.color = color

    def valid_move(self, new_coord: Coordinate):
        pass

    def move(self, new_coord: Coordinate):
        if self.valid_move(new_coord):
            self.coordinate = new_coord
        else:
            raise ValueError("Неверный ход для фигуры")

    def __str__(self):
        return f'X = {self.coordinate.x}, Y = {self.coordinate.y}'


class Pawn(Figure):
    def valid_move(self, new_coord):
        x_new = new_coord.x - self.coordinate.x
        y_new = new_coord.y - self.coordinate.y

        if self.color == Color.BLACK:
            if x_new == 1 and y_new == 0:
                return True
        elif self.color == Color.WHITE:
            if x_new == 1 and y_new == 0:
                return True
        else:
            return False


# Pawn1 = Pawn(Coordinate(2,2), Color.WHITE)
# Pawn1.move(Coordinate(3, 2))
#
# print(Pawn1)
#
# Pawn1.move(Coordinate(4, 2))
#
# print(Pawn1)