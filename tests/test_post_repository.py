from lib.post_repository import *
from lib.post import *
    
def test_find_by_tag(db_connection):
    db_connection.seed("seeds/blog_posts_tags.sql")
    repo = PostRepository(db_connection)
    posts = repo.find_by_tag('coding')
    assert posts == [
        Post(1, 'How to use Git'),
        Post(2, 'Fun classes'),
        Post(3, 'Using a REPL'),
        Post(7, 'SQL basics')
    ]