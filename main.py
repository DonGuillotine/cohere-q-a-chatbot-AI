import cohere
from secrets import secrets;


class CoHere:
    def __init__(self, api_key):
        self.co = cohere.Client('API_KEY', '2021-11-08')