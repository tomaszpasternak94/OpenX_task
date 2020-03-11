import pytest
from project.produkcja_testy.tests.contentUsersPosts import listUsers, listPosts

@pytest.fixture
def titlesF():
    global titlesAll
    titlesAll = []
    countTitle = 0
    while countTitle < len(listPosts):
        actually = listPosts[countTitle]['title']
        titlesAll.append(actually.upper()) # normalization of letter size
        countTitle +=1
    return titlesAll


def test_normalizeTitles(titlesF):
    for title in titlesAll:
        assert title.isupper()
