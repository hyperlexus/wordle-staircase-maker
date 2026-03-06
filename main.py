import random
from get_from_github import get_wordle_answers, get_wordle_guesses
import fnmatch

wordle_answers = get_wordle_answers()
wordle_guesses = get_wordle_guesses()
wordle_all = wordle_answers + wordle_guesses

wildcard_char = "?"

while True:
    wordle_word = "nurse"
    if wordle_word not in wordle_answers:
        print("you have reingeschissen, the word doesnt exist blud")
        continue
    break

def get_staircase_probabilities(word: str, left_side: bool):
    matched_staircase_words = []
    floors = (1, 2, 3, 4)
    target_letters = set(word)
    for floor in floors:
        current_matched_words = []
        current_floor = word[:floor:] if left_side else word[floor::]
        current_floor_full_string = f"{current_floor:{wildcard_char}<5}" if left_side else f"{current_floor:{wildcard_char}>5}"
        for allowed_word in wordle_all:
            if fnmatch.fnmatch(allowed_word, current_floor_full_string):
                is_valid = True
                for i in range(5):
                    if current_floor_full_string[i] == wildcard_char:
                        if allowed_word[i] in target_letters:
                            is_valid = False
                            break
                if is_valid:
                    current_matched_words.append(allowed_word)
        if word in current_matched_words:
            current_matched_words.pop(current_matched_words.index(word))
        matched_staircase_words.append(current_matched_words)
    return matched_staircase_words

left_result = get_staircase_probabilities(wordle_word, left_side=True)
right_result = list(reversed(get_staircase_probabilities(wordle_word, left_side=False)))

seen_left = set()
for idx in range(len(left_result) - 1, -1, -1):
    cleaned = [w for w in left_result[idx] if w not in seen_left]
    seen_left.update(left_result[idx])
    left_result[idx] = cleaned

seen_right = set()
for idx in range(len(right_result) - 1, -1, -1):
    cleaned = [w for w in right_result[idx] if w not in seen_right]
    seen_right.update(right_result[idx])
    right_result[idx] = cleaned

if all(left_result):
    output_staircase = []
    for sublist in left_result:
        output_staircase.append(random.choice(sublist))
    output_staircase.append(wordle_word)
    print(output_staircase)
else:
    print("didnt work left.")

if all(right_result):
    output_staircase = []
    for sublist in right_result:
        output_staircase.append(random.choice(sublist))
    output_staircase.append(wordle_word)
    print(output_staircase)
else:
    print("didnt work right.")