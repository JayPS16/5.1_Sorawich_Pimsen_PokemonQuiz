# Implementation plan

## Steps
1. Create cards.py with a small deck of about 10 Pokémon mapped to their type (data only).
2. Create quiz.py with check_answer(answer, correct) for R1, which ignores case and extra spaces.
3. Add is_valid_input(text) to quiz.py for R3 (reject blank input) and score_summary(correct, total) for R2 (correct/total and percentage).
4. Turn C1, C2 and a new score check C3 into unittest tests in test_quiz.py; run them with `python -m unittest -v`.
5. Create main.py: shuffle the cards, ask each one, re-ask on blank input without changing the score, then print the final score.
6. Play one full round of the quiz to judge whether it is useful.

## Later changes, if any
None