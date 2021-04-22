from random import randint

def monty_hall_problem_check(choose_option: str, attempts: int) -> dict:

    win_if_keep = 0
    win_if_change = 0
    res = {}
    for i in range(attempts-1):
        player = randint(0, 2)
        car = randint(0, 2)
        if player == car:
            win_if_keep += 1
        else:
            win_if_change += 1

    if choose_option == "keep":
        res = {"wins": win_if_keep,
               "loose": attempts-win_if_keep}

    if choose_option == "change":
        res = {"wins": win_if_change,
               "loose": attempts - win_if_change}

    return res

