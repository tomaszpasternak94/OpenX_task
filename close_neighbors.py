import math
import download_data
from download_data import listUsers
import user_posts
from user_posts import pairs

def whoIsCloserF(): #distance between users
    pairsGEO={}
    counterGEO=0
    while counterGEO < len(listUsers):
        id = listUsers[counterGEO]['id']
        geo = listUsers[counterGEO]['address']['geo']
        pairsGEO.update({id:geo})
        counterGEO +=1

    for pg in pairsGEO:
        score_board = []
        first = float('inf')
        second = float('inf')

        latitude = float(pairsGEO[pg]['lat'])
        longitude = float(pairsGEO[pg]['lng'])

        for pg2 in pairsGEO:
            latitude2 = float(pairsGEO[pg2]['lat'])
            longitude2 = float(pairsGEO[pg2]['lng'])
            wynik = math.sqrt((latitude2 - latitude)**2 + (longitude2 - longitude)**2)
            score_board.append(wynik)

        # searching for the shortest distance
        for number in score_board:
            if number < first:
                second = first
                first = number
            elif number > first and number < second:
                second = number

        print('dla użytkownika {} najblizszym sasiadem jest {}'.format(pairs[pg],pairs[score_board.index(second)+1]))

    return(pairs[pg],pairs[score_board.index(second)+1], second)
