"""
Author: AI Tutor
Date: 2023-10-27
Purpose: Defines the Player class and manages the player's state.
"""
import random
from nltk.corpus import names

class Player:
    def __init__(self):
        self.energy = 10
        self.evaluation = 0
        self.students = random.sample(names.words(), 8)
        self.grades = {1: {}, 2: {}}