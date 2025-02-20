import random

def grade_assignment(energy, assignment_num):
    grades = {}
    for student in range(1, 9):
        grades[student] = random.randint(60, 100)
    energy -= random.randint(8, 12)  # Increased energy cost
    print(f"Grading Assignment {assignment_num} complete.")
    return grades, energy

def take_time_off(energy):
    energy += random.randint(15, 25)
    print("Time off taken. Energy replenished.")
    return energy

def eat_chocolate(energy):
    energy += random.randint(20, 30)  # Increased chocolate boost
    print("Chocolate eaten. Energy boosted!")
    return energy

def feedback_session(energy, riddle_num):
    print(f"\nFeedback Session {riddle_num} - Riddle Time!")
    riddles = {
        1: ("What has an eye, but cannot see?", "needle"),
        2: ("What is full of holes but still holds water?", "sponge"),
        # Add more riddles here
    }
    riddle, answer = riddles.get(riddle_num, ("No riddle available.", ""))  # Handle missing riddles
    print(riddle)
    user_answer = input("Your answer: ").lower()

    if user_answer == answer:
        print("Correct!")
        return energy
    else:
        print("Incorrect. Energy lost.")
        energy -= random.randint(10, 15)
        return energy

def calculate_evaluation(energy, assignment1_grades, assignment2_grades, feedback1_success, feedback2_success):
    if energy <= 0:
        return "Defeat (Out of Energy!)"

    if not assignment1_grades or not assignment2_grades:  # Check for incomplete grading
      return "Defeat (Incomplete Grading)"

    evaluation_score = 0
    if energy > 50:
        evaluation_score += 50
    else:
        evaluation_score += energy

    if feedback1_success:
        evaluation_score += 25
    if feedback2_success:
        evaluation_score += 25

    if evaluation_score >= 80:
        return "Excellent Evaluation!"
    elif evaluation_score >= 60:
        return "Good Evaluation."
    else:
        return "Needs Improvement."


# Game Initialization
energy = 75  # Starting energy
assignment1_grades = {}
assignment2_grades = {}
state = "Start"
feedback1_success = False
feedback2_success = False

while state != "Exit" and energy > 0:
    print("\n--- Jane's Energy:", energy, "---")
    print("Current State:", state)

    if state == "Start":
        print("1. Grade Assignment 1")
        print("2. Take Time Off")
        print("3. Eat Chocolate")
        print("4. Exit")
        choice = input("> ")

        if choice == "1":
            assignment1_grades, energy = grade_assignment(energy, 1)
            state = "Grading1"
        elif choice == "2":
            energy = take_time_off(energy)
        elif choice == "3":
            energy = eat_chocolate(energy)
        elif choice == "4":
            state = "Exit"
        else:
            print("Invalid choice.")

    elif state == "Grading1":
        print("1. Feedback Session 1")
        print("2. Grade Assignment 2")
        choice = input("> ")
        if choice == "1":
            energy = feedback_session(energy, 1)
            if energy > 0:  # Only proceed if energy allows
              feedback1_success = True # Assume success for now, can add logic later
              state = "Grading2"
        elif choice == "2":
            assignment2_grades, energy = grade_assignment(energy, 2)
            state = "Grading2"
        else:
            print("Invalid choice.")

    elif state == "Grading2":
        print("1. Feedback Session 2")
        print("2. Evaluation")
        choice = input("> ")
        if choice == "1":
          energy = feedback_session(energy, 2)
          if energy > 0:
            feedback2_success = True
            state = "Evaluation"
        elif choice == "2":
          state = "Evaluation"
        else:
          print("Invalid choice.")

    elif state == "Evaluation":
        evaluation_result = calculate_evaluation(energy, assignment1_grades, assignment2_grades, feedback1_success, feedback2_success)
        print("\n--- Evaluation ---")
        print(evaluation_result)
        state = "Exit" # End the game after evaluation

    else:
        print("Invalid state.")

if state == "Exit":
    print("Game Over.")
elif energy <= 0:
    print("Game Over. Jane is exhausted!")