import cohere
from secrets import secrets;

# Providing API Key Credentials
class CoHere:
    def __init__(self, api_key):
        self.co = cohere.Client('API_KEY', '2021-11-08')

# A method to generate a text
    def cohere(self, question):
        return self.co.generate(
            model='medium',
            prompt=stevenQa(question),
            max_tokens=50,
            temperature=1
        ).generations[0].text