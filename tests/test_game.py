from longest_word.game import Game
import string
import requests

class TestGame:
    def test_game_initialization(self):
        #setup
        new_game = Game()

        # exercise
        grid = new_game.grid

        # verify

        assert type(grid) == list
        assert len(grid) == 9
        for letter in grid:
            assert letter in string.ascii_uppercase


    def test_is_valid(self):
        # setup
        new_game = Game()
        test_grid = 'KWEUEAKRZ'
        test_word = 'EUREKA'
        # exercice
        new_game.grid = list(test_grid) # Force the grid to a test case
        # verify
        assert new_game.is_valid(test_word) is True
        # teardown
        assert new_game.grid == list(test_grid) # Make sure the grid remained untouched

    def test_is_invalid(self):
        # setup
        new_game = Game()
        test_grid = 'KWEUEAKRZ'
        test_word = 'SANDWICH'
        # exerice
        new_game.grid = list(test_grid) # Force the grid to a test case
        # verify
        assert new_game.is_valid(test_word) is False
        # teardown
        assert new_game.grid == list(test_grid) # Make sure the grid remained untouched

    def test_unknown_word_is_invalid(self):
        """A word that is in the english directory should be valid"""
        # setup
        new_game = Game()
        test_grid = 'TESTEROA'
        test_word = 'TOASTER'
        # exerice
        new_game.grid = list(test_grid) # Force the grid to a test case
        # verify
        assert new_game.check_api_dictionary(test_word) is True
