verbs = {
    "Сказать": ["say", "said", "said"],
    "Сделать": ["make", "made", "made"],
    "Спать": ["sleep", "slept", "slept"],
    "Писать или читать по буквам": ["spell", ["spelt", "spelled"], ["spell", "spelled"]],
}


ru_of_right_ans = []


def is_right(actual, expected):
    for actual_w, expected_w in zip(actual, expected):
        if isinstance(expected_w, list):
            if actual_w not in expected_w:
                return False
        
        if isinstance(expected_w, str):
            if actual_w != expected_w:
                return False
    
    return True


while len(verbs) != len(ru_of_right_ans):
    for ru, expected in verbs.items():
        if ru in ru_of_right_ans:
            continue

        actual = [w.lower() for w in input(ru + ": ").split()]
        if is_right(actual, expected):
            print("Верно!\n")
            ru_of_right_ans.append(ru)
        else:
            print("Неверно! Верно будет так:", expected, "\n")
