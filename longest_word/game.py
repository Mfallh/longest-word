import random
import string
from collections import Counter
import requests
import json

class Game:
    def __init__(self) -> list:
        """Attribute a random grid to size 9"""
        self.grid = random.choices(string.ascii_uppercase, k=9)



    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""

        letters = self.grid.copy()
        counter_list = Counter(letters)
        counter_word = Counter(word)
        bool_list = []
        bool_list.append(len(word) <= 9)
        bool_list.append(type(word) == str)
        for letter in word:
            bool_list.append(letter not in string.digits)
        for letter in set(word):
            bool_list.append(letter in letters)
        for letter in set(word):
            counter_word[letter] <= counter_list[letter]

        if all(bool_list):
            return self.__check_dictionary(word)
        else:
            return False


    def check_api_dictionary(self, word):
        response = requests.get(f"https://wagon-dictionary.herokuapp.com/{word}")
        json_response = response.json()
        return json_response['found']
