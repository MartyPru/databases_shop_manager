from lib.account_repository import *
from lib.account import *
"""
When calling #all on instance of repository
returns a list of all accounts
"""
def test_returns_list_of_all_accounts(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repo = AccountRepository(db_connection)
    accounts = repo.all()
    assert accounts == [
        Account(1, 'user1', 'user1@network.com'),
        Account(2, 'user2', 'user2@network.com'),
        Account(3, 'user3', 'user3@network.com'),
        Account(4, 'user4', 'user4@network.com'),
    ]

"""
When calling #find with an item id on instance of repository
Returns result matching id
"""
def test_find_returns_matching_element(db_connection):
    db_connection.seed('seeds/social_network.sql')
    repo = AccountRepository(db_connection)
    matching_album = repo.find(1)
    assert matching_album == Account(1, 'user1', 'user1@network.com')