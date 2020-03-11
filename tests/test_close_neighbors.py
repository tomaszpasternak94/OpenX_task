import math
from project.produkcja_testy.tests.contentUsersPosts import listUsers, pairs
import pytest

@pytest.fixture
def whoIsCloserF(): #distance between users
    pairsGEO={}
    counterGEO=0
    while counterGEO < len(listUsers):
        id = listUsers[counterGEO]['id']
        geo = listUsers[counterGEO]['address']['geo']
        pairsGEO.update({id:geo})
        counterGEO +=1

    for pg in pairsGEO:
        global score_board
        score_board = []

        latitude = float(pairsGEO[pg]['lat'])
        longitude = float(pairsGEO[pg]['lng'])

        for pg2 in pairsGEO:
            latitude2 = float(pairsGEO[pg2]['lat'])
            longitude2 = float(pairsGEO[pg2]['lng'])
            wynik = math.sqrt((latitude2 - latitude)**2 + (longitude2 - longitude)**2)
            score_board.append(wynik)

        return score_board

@pytest.fixture
def shortestDistance():
    # searching for the shortest distance
    global first
    global second
    first = float('inf')
    second = float('inf')
    for number in score_board:
        if number < first:
            second = first
            first = number
        elif number > first and number < second:

            second = number
    return second

def test_typeScoreBoard(whoIsCloserF):
    assert type(score_board) is list

def test_isIntInScoreBoard(whoIsCloserF):
    for score in score_board:
        assert type(score) is float

def test_isNonNegative(shortestDistance):
    assert second == 19.411752269179626
