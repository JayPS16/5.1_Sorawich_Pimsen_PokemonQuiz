def check_answer(answer, correct):
    return answer.strip().lower() == correct.strip().lower()


def is_valid_input(text):
    return bool(text.strip())


def score_summary(correct, total):
    percentage = (correct / total * 100) if total else 0
    return f"{correct}/{total} ({percentage:.0f}%)"
