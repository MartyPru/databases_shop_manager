from lib.account import *
"""
When initiated with title, release_year, artist_id
Has attributes for each of those values
"""
def test_initial_attributes():
    account = Account(1, 'TestUser', 'testuser@network.com')
    assert account.username == 'TestUser'
    assert account.email_address == 'testuser@network.com'

"""
When two accounts with same information are created
They are equal
"""
def test_equality():
    account_1 = Account(1, 'TestUser', 'testuser@network.com')
    account_2 = Account(1, 'TestUser', 'testuser@network.com')
    assert account_1 == account_2

"""
When formatted into a string
Shows easy-to-read string
"""
def test_str_formatting():
    account_1 = Account(1, 'TestUser', 'testuser@network.com')
    assert str(account_1) == "Account(id=1, username='TestUser', email_address='testuser@network.com')"