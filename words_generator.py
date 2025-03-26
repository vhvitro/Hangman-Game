import random

def generate_word()->list:
    """Returns a list with a random word and the general context in which it's inserted"""
    with open("words.txt", "r") as file:
        word_context = random.choice(file.read().splitlines()).split(" ")
    return word_context

def create_word_sep(wrd:list)->list:
    """Returns the blank spaces that represent the word to be guessed as a list"""
    word_sep = ('_')*len(wrd)
    return list(word_sep)

STATES = [
    """
    |========|
    |        |
    |
    |
    |
    |
    |
    """,
    """
    |========|
    |        |
    |        0
    |
    |
    |
    |
    """,
    """
    |========|
    |        |
    |        0
    |        |
    |
    |
    |
    """,
    """
    |========|
    |        |
    |        0
    |       /|
    |
    |
    |
    """,
    """
    |========|
    |        |
    |        0
    |       /|\\
    |
    |
    |
    """,
    """
    |========|
    |        |
    |        0
    |       /|\\
    |       /
    |
    |
    """,
    """
    |========|
    |        |
    |        0
    |       /|\\
    |       / \\
    |
    |
    """
]