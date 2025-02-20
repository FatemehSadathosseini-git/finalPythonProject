"""
Author: AI Tutor
Date: 2023-10-27
Purpose: Contains functions to handle player commands.
"""
from feedback import feedback_session1, feedback_session2
import random

def start_grading(game_state, player):
    print("Starting the grading process...")
    game_state.transition_to("grading")

def inspect_report(game_state, player):
    print("\n--- Performance Overview ---")
    print("Energy:", player.energy)
    print("Evaluation Points:", player.evaluation)
    print("Student Grades:")
    for assignment, grades in player.grades.items():
        print(f"  Assignment {assignment}: {grades}")
    print("---")


def exit_game(game_state, player):
    print("Exiting the game.")
    exit()

def delay_grade(game_state, player):
    print("Skipping to feedback...")
    game_state.transition_to("feedback_1") # Adjust as needed for multiple feedback sessions.


def rest(game_state, player):
    player.energy += 5
    print("Rested. Energy increased by 5.")

def eat_chocolate(game_state, player):
    player.energy += 10
    print("Ate chocolate! Energy increased by 10.")

def give_feedback(game_state, player):
    if game_state.current_scene == "grading":
        assignment_num = int(game_state.current_scene[-1])
        if assignment_num == 1:
            feedback_session1(game_state, player)
        elif assignment_num == 2:
            feedback_session2(game_state, player)
        else:
            print("Invalid assignment number.")
    else:
        print("You must grade an assignment before giving feedback")

def get_evaluation(game_state, player):
    game_state.transition_to("evaluation")
    print("Course Evaluation:")
    print(f"Final Evaluation: {player.evaluation} points")

def play_again(game_state, player):
    # Re-initialize player and game state for a new game.
    player.__init__() # this assumes there is an init method in the Player class
    game_state.__init__()
    print("Starting a new game...")
