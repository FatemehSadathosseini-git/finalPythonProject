"""
Author: Fatemeh Sadat Hosseini
Date: 2025-02-04
Purpose: Processes player commands based on the current game state.
"""

def start_grading(game_state, player):
    print("Starting the grading process...")
    game_state.transition_to("grading")

def show_report(game_state, player):
    print("Displaying the report...")
    # Add logic to display the actual report here.  This would likely involve accessing
    # data from the game_state object.
    pass

def delay_grade(game_state, player):
    print("Delaying the grade...")
    # Add logic to implement delaying the grade. This might involve setting a timer or flag
    # within the game_state.
    pass

def exit_game(game_state, player):
    print("Exiting the game. Goodbye!")
    exit()

def rest(game_state, player):
    print("Taking a rest...")
    # Add logic for resting, possibly affecting player stats or game state.
    pass

def eat_chocolate(game_state, player):
    print("Eating chocolate...")
    # Add logic for eating chocolate, maybe improving player stats.
    pass

def start_feedback(game_state, player):
    print("Starting the feedback process...")
    game_state.transition_to("feedback_1")

def get_evaluation(game_state, player):
    print("Getting the evaluation...")
    game_state.transition_to("evaluation")

def restart_game(game_state, player):
    print("Restarting the game...")
    game_state.transition_to("start") # or any appropriate starting state


command_handlers = {
    "start": {
        "start grading": start_grading,
        "inspect report": show_report,
        "exit": exit_game,
        "delay grade": delay_grade
    },
    "grading": {
        "rest": rest,
        "eat chocolate": eat_chocolate,
        "give feedback": start_feedback,
        "inspect report": show_report,
        "exit": exit_game
    },
    "feedback_1": {
        "grade": start_grading,
        "inspect report": show_report,
        "exit": exit_game,
        "delay grade": delay_grade
    },
    "feedback_2": {
        "get evaluation": get_evaluation,
        "inspect report": show_report,
        "exit": exit_game
    },
    "evaluation": {
        "play again": restart_game,
        "inspect report": show_report,
        "exit": exit_game
    }
}



# # Example usage
# game_state = GameState()
# player = Player()

# # Process a command.  This would need to be integrated into a larger game loop.
# command = "start grading"
# if game_state.current_state in command_handlers and command.split()[0] in command_handlers[game_state.current_state]:
#     command_handlers[game_state.current_state][command](game_state, player)
# else:
#     print("Invalid command.")

