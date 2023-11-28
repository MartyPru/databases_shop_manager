from lib.post import Post

class PostRepository():
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute("SELECT * FROM posts;")
        posts = []
        for row in rows:
            post = Post(row['id'], row['title'], row['content'], row['views'], row['account_id'])
            posts.append(post)
        return posts
    
    def find(self, post_id):
        match = self.connection.execute("SELECT * FROM posts WHERE id = %s", [post_id])[0]
        post = Post(match['id'], match['title'], match['content'], match['views'], match['account_id'])
        return post
    
    def create_post(self, post):
        self.connection.execute("INSERT INTO posts (title, content, views, account_id) VALUES (%s, %s, %s, %s)",
                                [post.title, post.content, post.views, post.account_id])