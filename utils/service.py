from utils.meme_parser import MemeParser
from utils.r_queries import RQueries
from random import randrange
from json import loads
from json.decoder import JSONDecodeError
from utils.subreddit_list import MEME_S, RU_MEME_S


class Service():
    exc_photo = "https://cdn.businessinsider.nl/wp-content/uploads/2021/02/602f006e97cf0.png"

    def __init__(self, sr=""):
        self.query = RQueries("http://www.reddit.com/r/" + sr)

    def get_best_memes(self, limit=25):
        response = self.query.get_best(limit)
        try:
            memes = loads(response.content)
            children = memes["data"]["children"]
            return MemeParser(children)
        except JSONDecodeError:
            return Service.exc_photo
        except:
            return self.get_best_memes(limit)

    def get_hot_memes(self, limit=25):
        response = self.query.get_hot(limit)
        try:
            memes = loads(response.content)
            children = memes["data"]["children"]
            return MemeParser(children)
        except JSONDecodeError:
            return Service.exc_photo
        except:
            return self.get_hot_memes(limit)

    def get_new_memes(self, limit=25):
        response = self.query.get_new(limit)
        try:
            memes = loads(response.content)
            children = memes["data"]["children"]
            return MemeParser(children)
        except JSONDecodeError:
            return Service.exc_photo
        except:
            return self.get_new_memes(limit)

    def get_random_meme(self):
        response = self.query.get_random()
        try:
            memes = loads(response.content)
            children = memes[0]["data"]["children"]
            meme_data = MemeParser(children)[0]
            return meme_data
        except JSONDecodeError:
            return Service.exc_photo
        except:
            return self.get_random_meme()

    def get_search(self, prompt: str):
        try:
            search_result = loads(self.query.get_search(prompt).text)
            results = search_result["names"]
            return results
        except JSONDecodeError:
            return Service.exc_photo
        except:
            return self.get_search(prompt)

    @staticmethod
    def get_totally_random_meme():
        query = RQueries("http://reddit.com/r/" +
                         MEME_S[randrange(0, len(MEME_S))])
        response = query.get_random()
        try:
            memes = loads(response.content)
            children = memes[0]["data"]["children"]
            meme_data = MemeParser(children)[0]
            return meme_data
        except JSONDecodeError:
            return Service.exc_photo
        except:
            return Service.get_totally_random_meme()

    @staticmethod
    def get_random_russian_meme():
        query = RQueries("http://reddit.com/r/" +
                         RU_MEME_S[randrange(0, len(RU_MEME_S))])
        response = query.get_random()
        try:
            memes = loads(response.content)
            children = memes[0]["data"]["children"]
            meme_data = MemeParser(children)[0]
            return meme_data
        except JSONDecodeError:
            return Service.exc_photo
        except:
            return Service.get_random_russian_meme()
