from lib.post import Post
from lib.comment import Comment

class PostRepository():
    def __init__(self, connection):
        self.connection = connection

    def find_with_comments(self, post_id):
        rows = self.connection.execute("SELECT comments.id AS comment_id, comments.content AS comment_content, comments.post_id, posts.id, posts.title, posts.content FROM comments JOIN posts ON post_id = posts.id WHERE post_id = 1;")
        comments = []
        for row in rows:
            comment = Comment(row['comment_id'], row['comment_content'], row['post_id'])
            comments.append(comment)
        return Post(rows[0]['id'], rows[0]['title'], rows[0]['content'], comments)
    