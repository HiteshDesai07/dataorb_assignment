import json
from properties import Property
import pandas as pd
from load_reviews import Load_Reviews

property = Property()
property.load_properties()

df = None
input_file = 'data/input.json'
csv_datafile = 'data/amazon_reviews.csv'
if(property.load_review_from_file):
    df = pd.read_csv(csv_datafile, sep='\t')
else:
    f = open(input_file)
    data = json.load(f)
    f.close()

    df = pd.DataFrame(columns=["asin","review","title","body","link","rating","date"])

    for asin in data['ASIN']:
        # 1. Create a sample account in rainforest (https://www.rainforestapi.com/) and use review API to fetch reviews
        # 2. Get recent 30 reviews for the product Ids passed in an input file (Content of input file is given below)
        #Here to_page = 3 means 30 review, page wise 10 review, if you want 100 reviews then need to pass to_page = 10
        to_page = 3
        reviews_loader = Load_Reviews(property.api_key, asin, 3)
        reviews_loader.load_reviews()
        for row in reviews_loader.reviews:
            #3. Store reviews of all the products in a single dataframe
            df.loc[len(df)] = row
    df.to_csv(csv_datafile,sep='\t')

avg_product_review = df.groupby(['asin'])['rating'].mean().to_dict()
high_product_rating = max(avg_product_review, key = avg_product_review.get)
# 4. Get the product Id which has maximum average review among the products
print("4. Product Id which has maximum average review among the products -> " + high_product_rating)
# 5. Get product wise average review
print("5. Product wise average review -> \n" + str(avg_product_review))

product_wise_longest_review = (df.dropna(subset=['body'])
        .assign(something=lambda x: x['body'].str.len())
        .sort_values(['asin','something'], ascending=[True, False])
        .groupby('asin', as_index=False)
        .head(1))

# 6. Get product wise longest review based on length of the “body” field
print("6. Product wise longest review based on length of the “body” field -> \n" + str(product_wise_longest_review[['asin','body']]))