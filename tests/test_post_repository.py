from lib.post_repository import *
from lib.post import *
from lib.comment import *

"""
When calling #all on instance of repository
returns a list of all posts
"""
def test_find_with_comment(db_connection):
    db_connection.seed("seeds/blog_tables.sql")
    repo = PostRepository(db_connection)
    post = repo.find_with_comments(1)
    assert post == Post(1, 'Title 1', 'Content 1', [
            Comment(1, 'Comment 1', 1),
            Comment(2, 'Comment 2', 1),
            Comment(3, 'Comment 3', 1),
            Comment(4, 'Comment 4', 1)
        ])