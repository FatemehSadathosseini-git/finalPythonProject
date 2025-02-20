"""
Author: AI Tutor
Date: 2023-10-27
Purpose: Manages the game state and transitions between scenes.
"""
from commands import *

class GameState:
    def __init__(self):
        self.current_scene = "start"
        self.command_handlers = {
            "start": {
                "grade": start_grading,
                "inspect report": inspect_report,
                "exit": exit_game,
                "delay grade": delay_grade
            },
            "grading": {
                "rest": rest,
                "eat chocolate": eat_chocolate,
                "give feedback": give_feedback,
                "inspect report": inspect_report,
                "exit": exit_game
            },
            "feedback_1": {
                "grade": start_grading,
                "inspect report": inspect_report,
                "exit": exit_game,
                "delay grade": delay_grade
            },
            "feedback_2": {
                "get eval": get_evaluation,
                "inspect report": inspect_report,
                "exit": exit_game
            },
            "evaluation": {
                "play again": play_again,
                "inspect report": inspect_report,
                "exit": exit_game
            },
            "defeat": {
                "play again": play_again,
                "inspect report": inspect_report,
                "exit": exit_game
            }
            # Add other scenes as needed.  Refer to question.md for required scenes
        }

    def get_command_handler(self, command):
        handlers = self.command_handlers.get(self.current_scene, {})
        return handlers.get(command, None)

    def transition_to(self, new_scene):
        self.current_scene = new_scene

    def handle_defeat(self):
        self.transition_to("defeat")
        print("You have run out of energy. Game Over!")