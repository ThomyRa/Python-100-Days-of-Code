import requests
import pdb


class Post:

    def __init__(self, post):
        self.title = post["title"]
        self.subtitle = post["subtitle"]
        self.body = post["body"]
