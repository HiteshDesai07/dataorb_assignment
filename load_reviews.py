import requests


class Load_Reviews:
    reviews = []
    api_key = ''
    asin = ''
    page_no = ''
    
    def __init__(self, api_key, asin, page_no) -> None:
        self.api_key = api_key
        self.asin = asin
        self.page_no = page_no
        self.reviews = []

    def load_reviews(self):
        for page in range(1,self.page_no+1):
            params = {
            'api_key': self.api_key,
            'type': 'reviews',
            'amazon_domain': 'amazon.com',
            'asin': self.asin,
            'review_stars': 'all_stars',
            'sort_by': 'most_recent',
            'page':page
            }
            print(self.asin +'->'+str(page))
            print(params)
            
            # make the http GET request to Rainforest API
            api_result = requests.get('https://api.rainforestapi.com/request', params).json()

            for review in api_result['reviews']:
                this_data = [self.asin, review['id'], review['title'], review['body'], review['link'], review['rating'], review['date']['utc']]
                self.reviews.append(this_data)
