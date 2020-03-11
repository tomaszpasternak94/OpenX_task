import requests
import constants
from constants import posts, users

def downloadDataF():

    dataPosts = requests.get(posts)
    dataUsers = requests.get(users)

    global listPosts
    global listUsers

    listPosts = list(dataPosts.json())
    listUsers = list(dataUsers.json())

    return listPosts, listUsers

downloadDataF()
