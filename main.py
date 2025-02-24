"""
Author: Fatemeh Sadat Hosseini
Date: 2025-02-04
Purpose: Main entry point for the text adventure game.
"""
from game_state_1 import GameState
from player import Player
from utils import load_scene_description

def main():
    print("Welcome to Tutor's Journey!\n")
    game_state = GameState()
    player = Player()
    
    while True:
        print(load_scene_description(game_state.current_scene))
        
        command = input("> ").strip().lower()
        if command == "exit":
            print("Exiting the game. Goodbye!")
            break
        
        handler = game_state.get_command_handler(command)
        if handler:
            handler(game_state, player)
            if player.energy < 0:
                game_state.handle_defeat()
        else:
            print(f"Invalid command: {command}. Type 'help' for available commands: {', '.join(game_state.get_current_scene().keys())}.")

if __name__ == "__main__":
    main()