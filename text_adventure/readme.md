# Tutor's Journey - Text Adventure Game

## Overview
A text-based adventure game where you play as a tutor managing grading and feedback sessions.

## Installation
1. Install Python 3.x.
2. Install required packages:
   ```bash
   pip install nltk
   ```
3. Download NLTK corpora:
   ```python
   import nltk
   nltk.download('names')
   nltk.download('reuters')
   ```

## How to Run
Execute the main script:
```bash
python main.py
```

## Commands
- `grade`: Start grading assignments.
- `inspect report`: View current performance.
- `rest`: Recover energy points.
- `exit`: Quit the game.
- `delay grade`: Skip to the next feedback session.  (Secret!)
- `give feedback`: Proceed to the feedback session
- `get eval`: get the evaluation at the end of the game
- `play again`: restart the game
