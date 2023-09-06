from enum import Enum
from typing import Type


class Coordinate:
    def __init__(self, x: int, y: int):
        if not 0 <= x <= 8 and 0 <= y <= 8:
            raise ValueError('Координата выходит за пределы доски')
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))



class Color(Enum):
    BLACK = 0
    WHITE = 1



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


class Board:
    def __init__(self):
        self.dict_figures = {}

    def add_figure(self, coord: Coordinate, figure: Figure):
        if coord in self.dict_figures:
            raise ValueError("На этом месте уже есть фигура")
        else:
            self.dict_figures[coord] = figure

    def del_figure(self, coord: Coordinate):
        if coord in self.dict_figures:
            self.dict_figures.pop(coord)
        else:
            raise ValueError("На этом месте нет фигуры")

    def presence_figure(self, coord: Coordinate):
        return coord in self.dict_figures




class Pawn(Figure):
    def __init__(self, coordinate: Coordinate, color: Color, board: Board):
        super().__init__(coordinate, color)
        self.board = board
        if not self.board.presence_figure(coordinate):
            self.board.add_figure(coordinate, self)
        else:
            raise ValueError("На этой позиции уже есть фигура")
    def valid_move(self, new_coord):
        x_new = new_coord.x - self.coordinate.x
        y_new = new_coord.y - self.coordinate.y

        if self.color == Color.BLACK:
            if x_new == 1 and y_new == 0 and not self.board.presence_figure(new_coord):
                self.board.del_figure(self.coordinate)
                self.board.add_figure(new_coord, self)
                return True
        elif self.color == Color.WHITE:
            if x_new == 1 and y_new == 0 and not self.board.presence_figure(new_coord):
                self.board.del_figure(self.coordinate)
                self.board.add_figure(new_coord, self)
                return True
        else:
            return False

board = Board()
Pawn1 = Pawn(Coordinate(2,2), Color.WHITE, board)
Pawn2 = Pawn(Coordinate(3,2), Color.WHITE, board)
print(Pawn1)
print(Pawn2)

Pawn2.move(Coordinate(4, 2))
Pawn1.move(Coordinate(3, 2))

print(Pawn1)
print(Pawn2)
print(board.dict_figures)