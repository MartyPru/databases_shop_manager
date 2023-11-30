from lib.post import Post
from lib.tag import Tag

class PostRepository():
    def __init__(self, connection):
        self.connection = connection
 
    def find_by_tag(self, tag):
        rows = self.connection.execute("SELECT posts.id, posts.title \
                                       FROM posts \
                                       JOIN posts_tags \
                                       ON posts_tags.post_id = posts.id \
                                       JOIN tags \
                                       ON posts_tags.tag_id = tags.id \
                                       WHERE tags.name = %s", [tag])
        posts = []
        for row in rows:
            post = Post(row['id'], row['title'])
            posts.append(post)
        return posts