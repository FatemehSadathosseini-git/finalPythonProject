"""
Author: AI Tutor
Date: 2023-10-27
Purpose: Helper functions for the game.
"""
import random
from nltk.corpus import names
import os

def load_scene_description(scene_name):
    try:
        with open(f"scenes/{scene_name}.txt", "r") as file:
            return file.read()
    except FileNotFoundError:
        return "Scene description not found."

def get_students():
    """Returns a list of random student names."""
    num_students = 8 # Changed to 8 students as specified in question.md
    return [random.choice(names.words()) for _ in range(num_students)]