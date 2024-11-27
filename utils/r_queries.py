from requests import get


class RQueries():
    def __init__(self, link: str):
        self.link = link

    # limit is 25 by default up to 100
    def get_after(self, meme_name: str, limit=25):
        response = get(self.link + "/new.json",
                       params={"after": meme_name, "limit": limit}, timeout=2)
        response.content
        return response.content

    def get_before(self, meme_name: str, limit=25):
        response = get(self.link + "/new.json",
                       params={"before": meme_name, "limit": limit}, timeout=2)
        response.content
        return response

    def get_best(self, limit=25):
        response = get(self.link + "/best.json",
                       params={"limit": limit}, timeout=2)
        response.content
        return response

    def get_new(self, limit=25):
        response = get(self.link + "/new.json",
                       params={"limit": limit}, timeout=2)
        response.content
        return response

    def get_hot(self, limit=25):
        response = get(self.link + "/hot.json",
                       params={"limit": limit}, timeout=2)
        response.content
        return response

    def get_random(self):
        response = get(self.link + "/random.json",
                       timeout=2, allow_redirects=True)
        response.content
        return response

    def get_search(self, prompt: str):
        response = get("http://reddit.com/api/search_reddit_names.json",
                       params={"query": prompt, "exact": False}, timeout=2)
        response.content
        return response
