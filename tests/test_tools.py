import pytest
import tools

def test_monty_hall_problem_check_if_keep():
    """
    Verification of winnings if choose `keep` options in percentage.
    """
    wins_if_keep = tools.monty_hall_problem_check("keep", 10000).get("wins")*100//10000
    assert wins_if_keep == 33

def test_monty_hall_problem_check_if_change():
    """
       Verification of winnings if choose `change` options in percentage.
    """
    wins_if_change = tools.monty_hall_problem_check("change", 10000).get("wins")*100//10000
    assert wins_if_change == 66

