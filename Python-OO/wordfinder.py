"""Word Finder: finds random words from a dictionary."""


import random

class WordFinder:
    def __init__(self, filepath):
        """Reads a file and creates a list of words."""
        self.words = self.read_words(filepath)
        print(f"{len(self.words)} words read")

    def read_words(self, filepath):
        """Reads words from the file and removes newline characters."""
        with open(filepath, 'r') as file:
            words = [line.strip() for line in file]  # Strip newline characters
        return words

    def random(self):
        """Returns a random word from the list of words."""
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    """Special Word Finder that excludes blank lines and comments."""
    
    def read_words(self, filepath):
        """Reads words, ignoring blank lines and comments."""
        with open(filepath, 'r') as file:
            words = [line.strip() for line in file if line.strip() and not line.startswith('#')]
        return words