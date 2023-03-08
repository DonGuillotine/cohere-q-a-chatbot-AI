import cohere
from secrets import secrets;

api_key = secrets.get('API_KEY')
print(api_key)
# class CoHere:
#     def __init__(self, api_key):
#         self.co = cohere.Client('API_KEY', '2021-11-08')