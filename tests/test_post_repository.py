from lib.post_repository import *
from lib.post import *
"""
When calling #all on instance of repository
returns a list of all posts
"""
def test_returns_list_of_all_posts(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repo = PostRepository(db_connection)
    posts = repo.all()
    assert posts == [
        Post(1, 'Title 1', 'This is Content 1', 100, 1),
        Post(2, 'Title 2', 'This is Content 2', 200, 2),
        Post(3, 'Title 3', 'This is Content 3', 300, 3),
        Post(4, 'Title 4', 'This is Content 4', 100, 4),
        Post(5, 'Title 5', 'This is Content 5', 150, 2)
    ]

"""
When calling #find with an item id on instance of repository
Returns result matching id
"""
def test_find_returns_matching_element(db_connection):
    db_connection.seed('seeds/social_network.sql')
    repo = PostRepository(db_connection)
    matching_post = repo.find(1)
    assert matching_post == Post(1, 'Title 1', 'This is Content 1', 100, 1)


"""
When calling #create_post with relevant info on instance of repository
Successfully inserts a post in posts table
"""
def test_create_post_inserts_post_to_posts_table(db_connection):
    db_connection.seed('seeds/social_network.sql')
    repo = PostRepository(db_connection)
    new_post = Post(None, 'Title 6', 'This is Content 6', 100, 1)
    repo.create_post(new_post)
    posts = repo.all()
    assert posts == [
        Post(1, 'Title 1', 'This is Content 1', 100, 1),
        Post(2, 'Title 2', 'This is Content 2', 200, 2),
        Post(3, 'Title 3', 'This is Content 3', 300, 3),
        Post(4, 'Title 4', 'This is Content 4', 100, 4),
        Post(5, 'Title 5', 'This is Content 5', 150, 2),
        Post(6, 'Title 6', 'This is Content 6', 100, 1)
    ]