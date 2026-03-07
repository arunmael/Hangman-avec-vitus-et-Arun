"""
This is the File for the logic of the programm
"""
from wonderwords import RandomWord


def random_word():
    """
    This is to choose a random word from the English dictionary
    :return:
    """
    rw = RandomWord()
    word = rw.word(word_max_length=10)
    return word