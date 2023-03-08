import cohere
from decouple import config


# Writing a prompt for my model
def myPrompt(question):
    return 'You are a chatbot that answers questions:'


# Providing API Key Credentials
class CoHere:
    def __init__(self, api_key):
        api_key = config('API_KEY')
        self.co = cohere.Client(api_key)


# A method to generate a text
    def cohere(self, question):
        return self.co.generate(
            model='medium',
            prompt=myPrompt(question),
            max_tokens=50,
            temperature=1
        ).generations[0].text
