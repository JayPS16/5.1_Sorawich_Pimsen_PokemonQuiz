import unittest

from quiz import check_answer, is_valid_input, score_summary


class QuizTests(unittest.TestCase):
    def test_c1_normalized_answer_is_correct(self):
        self.assertTrue(check_answer("  Electric ", "electric"))

    def test_c2_blank_input_is_rejected_and_zero_score_is_unchanged(self):
        self.assertFalse(is_valid_input("   "))
        self.assertEqual(score_summary(0, 0), "0/0 (0%)")

    def test_c3_score_summary_shows_correct_total_and_percentage(self):
        self.assertEqual(score_summary(4, 5), "4/5 (80%)")


if __name__ == "__main__":
    unittest.main()
