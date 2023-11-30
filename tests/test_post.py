from lib.post import *
"""
When initiated with title, release_year, artist_id
Has attributes for each of those values
"""
def test_initial_attributes():
    post = Post(1, 'Title 1')
    assert post.title == 'Title 1'
"""
When two posts with same information are created
They are equal
"""
def test_equality():
    post_1 = Post(1, 'Title 1')
    post_2 = Post(1, 'Title 1')
    assert post_1 == post_2

"""
When formatted into a string
Shows easy-to-read string
"""
def test_str_formatting():
    post_1 = Post(1, 'Title 1')
    assert str(post_1) == "Post(1, Title 1)"