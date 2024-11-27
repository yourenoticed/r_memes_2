class MemeParser():
    def __new__(self, sr_children):
        return self.get_memes(self, sr_children)

    def get_memes(self, sr_children) -> list:
        return [child["data"]["url"] for child in sr_children]
