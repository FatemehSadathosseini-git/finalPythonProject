"""
Author: Fatemeh Sadat Hosseini
Date: 2025-02-04
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
        self.chocolate_used = {1: False, 2: False}
    
    def enter_grade(self, assignment, student, grade):
        # Implement grade entry and energy deduction
        pass