# Author: Bard
# Date: October 26, 2023
# Purpose: Utility functions for the game
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
    """Returns a list"""
    num_students = random.randint(5, 20)
    return [random.choice(names.words()) for _ in range(num_students)]