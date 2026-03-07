"""
This is the File for the logic of the programm
"""
from wonderwords import RandomWord
import design

def random_word():
    """
    This is to choose a random word from the English dictionary
    :return:
    """
    rw = RandomWord()
    word = rw.word(word_max_length=10)
    return word

guessed_letters = [] # List of Letters that are typen
correct_letters = [] # List of letters that are correct
def check_for_input(pressed_key, word):  # This function appends input to the list "guessed_letters"
    """
    :param pressed_key: The pressed button (for example "a")
    :param word: The word that we have to guess correctly
    :return:
    """
    guessed_letters.append(pressed_key)
    print(pressed_key)
    for char in word:
        if char in guessed_letters:
            icon = f"[\u2714]"
            correct_letters.append(char)
        else:
            icon = f"[\u2718]"
        print(f"'{char}'{icon}")