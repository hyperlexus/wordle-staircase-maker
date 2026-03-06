from main import get_wordle_staircase
from main import wordle_answers

amount_possible = 0
amount_left = 0
amount_right = 0
for i in wordle_answers:
    dingens = get_wordle_staircase(i)
    if dingens:
        amount_possible += 1

print(amount_possible + len(wordle_answers))

print(amount_left + amount_possible)
print(amount_right + amount_possible)

