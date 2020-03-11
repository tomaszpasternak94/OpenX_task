import requests
import pytest
from project.produkcja_testy.constants import *

@pytest.fixture
def downloadDataF():

    dataPosts = requests.get(posts)
    dataUsers = requests.get(users)

    global listPosts
    global listUsers

    listPosts = list(dataPosts.json())
    listUsers = list(dataUsers.json())

    print(listPosts[:4])
    return listPosts, listUsers


def test_listPosts(downloadDataF):
	assert type(listPosts) is list


def test_listUsers(downloadDataF):
	assert type(listUsers) is list
