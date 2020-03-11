import download_data
from download_data import listUsers, listPosts

def userPostsF():
    global pairs

    pairs={}    # pairing - id and username
    counter=0
    while counter < len(listUsers):
        id = listUsers[counter]['id']
        name = listUsers[counter]['username']
        pairs.update({id:name})
        counter +=1

    amountPosts=[]   # posts counter
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

userPostsF()
