# Checks and decisions

## Concrete checks
Write the first two expectations before implementation. Fill in actual results after running them.

| Check / requirement | Given | When | Expected result | Actual result / pass or fail |
|---|---|---|---|---|
| C1 / R1 — normal case | Card: Pikachu, correct type "electric" | Answer is "  Electric " | Marked correct | Pass. Quiz printed "Correct!" and the unit test passed |
| C2 / R3 — boundary or failure case | Card: Charmander, score is 0 correct out of 0 | Answer is "   " (blank) | Rejected, same card asked again, score stays 0/0 | Pass. Quiz printed "Please enter an answer." and asked the same card again; unit test passed |
| C3 / R2 — score | 5 cards answered, 4 correct | Final score is calculated | Shows "4/5 (80%)" | Pass. Unit test passed; a full 10-card round ended with "Final score: x/10 (y%)" |

## Two review decisions
- Plan decision: Changed Copilot's plan, which assumed existing code to inspect. I rewrote it for a new project with named files and functions (cards.py, quiz.py, main.py, test_quiz.py) so each step maps to R1-R3.
- Code decision: Changed the deck in cards.py. Copilot's version had dual-type Pokémon (Bulbasaur, Jigglypuff, Geodude, Gastly, Pidgey), so a correct answer like "poison" could be marked wrong. I swapped them for single-type Pokémon (Chikorita, Clefairy, Sudowoodo, Misdreavus, Eevee) to keep the quiz simple and fair. I accepted quiz.py and main.py as proposed because they matched my checks and kept input/print out of quiz.py.

## Automated tests
- Test file and behaviour checked: test_quiz.py. check_answer ignores case and spaces (C1), is_valid_input rejects blank input (C2), score_summary returns "4/5 (80%)" (C3).
- Command I ran: `python -m unittest -v`
- Final result: 3 tests ran, all passed (OK).
- Correction and rerun, if needed: None needed for the code. The only fix was the deck in cards.py, before the tests were run.

## Realistic use and final judgment
- Task I tried: Played a full round of all 10 cards with normal answers, a wrong answer, and a blank answer.
- Outcome: It worked as expected and showed the right type after a mistake, so it is useful for quick revision.
- Judgment: Done. R1-R3 each have a passing check and the full round matched what I expected.
- Remaining limitation or unfinished work: The blank-input retry loop in main.py is only checked by hand, not by an automated test.