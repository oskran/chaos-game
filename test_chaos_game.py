from chaos_game import ChaosGame
import pytest


def test_n_is_int():
    """
    Tests that an exception is raised if n is not int
    """
    with pytest.raises(Exception):
        game1 = ChaosGame(5.6, 1 / 2)
        game2 = ChaosGame(10.123, 1 / 2)


def test_n_larger_than_3():
    """
    Tests than an exception is raised if n is not larger than 3
    """
    with pytest.raises(Exception):
        game1 = ChaosGame(2, 1 / 2)
        game2 = ChaosGame(-5, 1 / 2)


def test_r_float_and_between_0_and_1():
    """
    Tests than an exception is raised if r is not a float variable / is not
    between 0 and 1.
    """
    with pytest.raises(Exception):
        game1 = ChaosGame(5, -6)
        game2 = ChaosGame(5, 5)


def test_file_is_png():
    """
    Tests than an exception is raised if the filename extention anything other
    than .png
    """
    with pytest.raises(Exception):
        game = ChaosGame(3, 1 / 2)
        game.iterate(1000)

        game.savepng("filename.jpeg")

