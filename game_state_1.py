"""
Author: Fatemeh Sadat Hosseini
Date: 2025-02-04
Purpose: Manages the game state and transitions between scenes.
"""
from commands import *

class GameState:
    def __init__(self):
        self.current_scene = "start"
        self.command_handler = command_handlers
    
    def get_command_handler(self, command):
        handlers = self.command_handlers.get(self.current_scene, {})
        return handlers.get(command, None)
    
    def transition_to(self, new_scene):
        self.current_scene = new_scene
    
    def handle_defeat(self):
        self.transition_to("defeat")
        print("You have run out of energy. Game Over!")