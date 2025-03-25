import random

def generate_word()->list:
    with open("words.txt", "r") as file:
        word_context = random.choice(file.read().splitlines()).split(" ")
    return word_context

def create_word_sep(wrd:list)->list:
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