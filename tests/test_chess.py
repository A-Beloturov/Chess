import pytest
from main import Coordinate, Color, Figure, Board, Pawn


def test_valid_move_pawn(board_and_pawns):
    board, pawn1, pawn2 = board_and_pawns
    assert pawn1.valid_move(Coordinate(2, 3)) == True
    assert pawn2.valid_move(Coordinate(3, 4)) == True


@pytest.mark.parametrize("x, y, expected", [(2, 2, False), (2, 4, False), (2, 1, False), (3, 2, False), (1, 2, False)])
def test_invalid_move_pawn(board_and_pawns, x, y, expected):
    board, pawn1, pawn2 = board_and_pawns
    assert pawn1.valid_move(Coordinate(x, y)) == expected



def test_pawn_diagonally(board_and_pawns):
    board, pawn1, pawn2 = board_and_pawns
    assert pawn1.valid_move(Coordinate(3,3))

def test_add_figure(board_and_pawns):
    board, pawn1, pawn2 = board_and_pawns
    board.add_figure(Coordinate(1,1), pawn1)
    with pytest.raises(ValueError):
        board.add_figure(Coordinate(1, 1), pawn2)






