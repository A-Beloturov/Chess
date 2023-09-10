import pytest
from main import Coordinate, Color, Figure, Board, Pawn


@pytest.fixture
def board_and_pawns():
    board = Board()
    pawn1 = Pawn(Coordinate(2, 2), Color.WHITE, board)
    pawn2 = Pawn(Coordinate(3, 3), Color.WHITE, board)
    return board, pawn1, pawn2
