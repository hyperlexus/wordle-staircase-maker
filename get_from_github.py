allowed_answers_file = "wordle-answers-alphabetical.txt"
allowed_guesses_file = "wordle-allowed-guesses.txt"

def get_wordle_answers():
    with open(allowed_answers_file) as f:
        return f.read().splitlines()

def get_wordle_guesses():
    with open(allowed_guesses_file) as f:
        return f.read().splitlines()