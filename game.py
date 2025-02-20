# Author: Bard
# Date: October 26, 2023
# Purpose: Main game loop and command handling

import random
from nltk.corpus import names, reuters
import re
from modules.grading import grading_session
from modules.feedback import feedback_session1, feedback_session2
from modules.utils import (generate_random_student_names, 
                           preprocess_sentence, check_code_phrase)

# ... (Import other necessary modules and functions) ...

def main():
    """Main game loop."""
    # Initialize game state (energy, evaluation points, student grades, etc.)
    energy = 10
    eval_points = 0
    student_names = generate_random_student_names(8)
    grades = {name: None for name in student_names}  # Initialize grades to None


    game_state = "Start"  # Start state

    while game_state != "Exit" and energy > 0:
        # Display current scene description (read from file)
        print(f"Current Game State: {game_state}") # change the print
        # Display current game state summary

        command = input("Enter command: ").lower()

        if game_state == "Start":
            if command == "grade":
                game_state = "Grading 1"
            elif command == "inspect report":
                # Display report (energy, eval points, grades)
                pass
            elif command == "exit":
                game_state = "Exit"
            else:
                print("Invalid command.")

        elif game_state.startswith("Grading"):
            # ... (Implement grading session using grading_session function) ...

        elif game_state == "Feedback 1":
            # ... (Implement feedback session 1 using feedback_session1 function) ...

        elif game_state == "Feedback 2":
            # ... (Implement feedback session 2 using feedback_session2 function) ...

        # ... (Implement other game states (Time off, Chocolate, Evaluation, Defeat)...) ...

    # Game over - Display final report
    print("Game Over!")
    # ... (Handle game over state) ...

if __name__ == "__main__":
    main()
