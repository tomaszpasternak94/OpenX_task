import download_data
from download_data import listUsers, listPosts

def titlesF():
    global titlesAll
    titlesAll = []
    countTitle = 0
    while countTitle < len(listPosts):
        actually = listPosts[countTitle]['title']
        titlesAll.append(actually.upper()) # normalization of letter size
        countTitle +=1

    return titlesAll

titlesF()
