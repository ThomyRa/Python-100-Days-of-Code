class Post:

    def __init__(self, post):
        self.title = post["title"]
        self.subtitle = post["subtitle"]
        self.body = post["body"]
        self.author = post["author"]
        self.date = post["date"]
        self.image = post["image"]
