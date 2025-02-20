# Author: Bard
# Date: October 26, 2023
# Purpose: Helper functions for the game.

import random
from nltk.corpus import names
import re

def generate_random_student_names(num_students):
    """Generates a list of random student names."""
    return random.sample(names.words(), num_students)

def preprocess_sentence(sentence, topic):
    """Preprocesses a sentence for the feedback session 1 riddle."""
    # Implement regex based preprocessing as described.
    pass

def check_code_phrase(phrase):
    """Recursively checks if a given phrase is a valid code phrase."""
    #Implement recursive check as described.
    pass