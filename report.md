# Computational Linguistics Tutor Game - Final Exam Report

## Introduction:

This report details the development of a CLI-based game for my Python final exam, simulating the challenges faced by a Computational Linguistics (CL) tutor named Jane.  The game focuses on balancing grading, student interaction, personal well-being (time off and chocolate!), and ultimately achieving a good evaluation.

## Game Concept and Design:

The core gameplay revolves around managing Jane's energy levels and time effectively. The game progresses through distinct states: Start, Grading 1 & 2, Time Off, Chocolate, Feedback 1 & 2, Evaluation, Defeat, and Exit.  Each state presents different challenges and opportunities.

* **Grading:**  Jane needs to grade two assignments for eight students each. Grading consumes energy and time.
* **Time Off:**  Taking time off replenishes energy but consumes time.
* **Chocolate:**  Chocolate provides a quick energy boost but is a limited resource.
* **Feedback Sessions:**  Two feedback sessions (after grading each assignment) require Jane to solve riddles to "prepare."  Failing a riddle results in lost energy and potentially a lower evaluation.
* **Evaluation:** The final evaluation depends on Jane's energy level, the quality of feedback given (related to riddle success), and whether all grading is complete.
* **Defeat:**  Jane loses if her energy drops to zero or if she fails both riddles.

## Development Approach:

1. **State Management:** I used a simple state variable to track the game's progress and control which actions are available to the player.
2. **Data Structures:** Dictionaries were used to store student grades for each assignment.  This made it easy to access and update individual grades.
3. **Functions:**  Each action (grading, time off, chocolate, feedback, etc.) was implemented as a separate function. This modular design improved code organization and readability.
4. **User Input and Output:** The `input()` function was used for player interaction, and `print()` statements provided feedback and game updates.
5. **Randomness:** The `random` module was employed to introduce some variability, such as the energy consumed during grading or the difficulty of riddles.
6. **Riddle Implementation:** I incorporated a simple riddle system.  Riddles are presented to the player, and their answers are checked for correctness.
7. **Game Loop:** A `while` loop controlled the main game flow, allowing the player to make choices until the game ends (either through success, defeat, or exit).

## Difficulties Encountered:

* **Balancing Gameplay:** The initial version of the game was either too easy or too difficult. I had to adjust energy consumption rates, riddle difficulty, and the rewards for different actions to create a more balanced and engaging experience.
* **Riddle Design:**  Creating interesting and challenging riddles was surprisingly time-consuming.
* **CLI Design:**  Making the CLI interface user-friendly and intuitive was a challenge. I spent time refining the prompts and output messages to make the game easier to understand and play.
* **Debugging:**  Tracking down and fixing bugs, especially related to state management and data handling, required careful testing and debugging.

## Game Code (Simplified Example):

```python
import random

def grade_assignment(energy):
    grades = {}
    for student in range(1, 9):
        grades[student] = random.randint(60, 100) # Random grades for demonstration
    energy -= random.randint(5, 10) # Energy consumed
    print("Grading complete.")
    return grades, energy

# ... other functions (time_off, chocolate, feedback, etc.)

energy = 50
assignment1_grades = {}
assignment2_grades = {}
state = "Start"

while state != "Exit" and energy > 0:
    print("\nJane's Energy:", energy)
    print("Current State:", state)

    if state == "Start":
        print("1. Grade Assignment 1")
        print("2. Take Time Off")
        # ... other options
        choice = input("> ")

        if choice == "1":
            assignment1_grades, energy = grade_assignment(energy)
            state = "Grading1"
        # ... handle other choices

    elif state == "Grading1":
        # ... handle grading 1 completion and transition to feedback 1

    # ... handle other states

# ... game end conditions and evaluation
```

## Further Improvements:

* **More Complex Riddles:**  Implement a wider variety of riddles with varying difficulty levels.
* **Enhanced CLI:**  Use libraries like `rich` or `curses` to create a more visually appealing and interactive CLI.
* **Saving and Loading:**  Implement the ability to save and load game progress.
* **More Game States/Events:** Add more events and challenges to make the game more dynamic and replayable.
* **Difficulty Levels:**  Allow the player to choose a difficulty level, affecting energy consumption, riddle difficulty, etc.

## Conclusion:

Developing this game was a valuable learning experience. I gained practical experience in state management, data structures, functions, and user interaction in Python.  While I faced some challenges along the way, I was able to overcome them and create a functional and engaging game.  This project has solidified my understanding of Python programming and game development principles.

**(Note: The zipped game file would be submitted along with this report in a real exam scenario.)**
