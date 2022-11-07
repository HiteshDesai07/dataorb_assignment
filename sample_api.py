import requests
import json

# set up the request parameters
params = {
  'api_key': '4330846B067D4B47BD6766504EC78928',
  'type': 'reviews',
  'amazon_domain': 'amazon.com',
  'asin': 'B073JYC4XM',
  'review_stars': 'all_stars',
  'sort_by': 'most_recent',
  'page':2
}

# make the http GET request to Rainforest API
api_result = requests.get('https://api.rainforestapi.com/request', params)

# print the JSON response from Rainforest API
print(json.dumps(api_result.json()))