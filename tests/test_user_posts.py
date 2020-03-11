import pytest
from project.produkcja_testy.tests.contentUsersPosts import listUsers, listPosts

@pytest.fixture
def userPostsF():
    global pairs

    pairs={}    # pairing - id and username
    counter=0
    while counter < len(listUsers):
        id = listUsers[counter]['id']
        name = listUsers[counter]['username']
        pairs.update({id:name})
        counter +=1

    amountPosts=[]   # posts counter  countUsers
    item = 0
    while item < len(listPosts):
        actually = listPosts[item]['userId']
        amountPosts.append(actually)
        item +=1

    # dictionary with a summary of the number of posts written by individual users
    idAndAmountPosts = dict([(x, amountPosts.count(x)) for x in amountPosts])

    # ID conversion to username
    ID = 1
    while ID <= len(listUsers):
        if ID in idAndAmountPosts:
            idAndAmountPosts[pairs[ID]] = idAndAmountPosts.pop(ID)
        else:
            pass
        ID += 1

    for user, posts in idAndAmountPosts.items():
        print('{} napisał(a) {} postów'.format(user,posts))

    return pairs

def test_typePairs(userPostsF):
	assert type(pairs) is dict

def test_keyIdPairs(userPostsF):
    for key in pairs.keys():
        assert type(key) is int
