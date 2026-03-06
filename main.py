import random
import fnmatch
from get_from_github import get_wordle_answers, get_wordle_guesses

wordle_answers = get_wordle_answers()
wordle_guesses = get_wordle_guesses()
wordle_all = wordle_answers + wordle_guesses

def get_wordle_staircase(wordle_word):
    if wordle_word not in wordle_answers:
        return None

    wildcard_char = "?"

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

    def clean_results(results):
        seen = set()
        for idx in range(len(results) - 1, -1, -1):
            cleaned = [w for w in results[idx] if w not in seen]
            seen.update(results[idx])
            results[idx] = cleaned
        return results

    left_result = clean_results(left_result)
    right_result = clean_results(right_result)

    if all(right_result):
        output = [random.choice(sublist) for sublist in right_result]
        output.append(wordle_word)
        return output, 1
    if all(left_result):
        output = [random.choice(sublist) for sublist in left_result]
        output.append(wordle_word)
        return output, 0

    return None