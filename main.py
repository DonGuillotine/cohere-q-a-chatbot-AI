import cohere
from secrets import secrets;


class CoHere:
    def __init__(self, api_key):
        self.co = cohere.Client('API_KEY', '2021-11-08')

    def cohere(self, question):
        return self.co.generate(
            model=&#39;medium&#39;,
        )