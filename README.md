# DataOrb Assignment

# 1. How to run
    - Clone git repository into your local and run below commands
        - git clone https://github.com/HiteshDesai07/dataorb_assignment.git
    - Repository data are now available in your local, now run
        - cd dataorb_assignment
        - python assignment_code.py
            - This command will run with importing the default property value added in the 'data/application.properties', where I've added 2 properties
            - This property file data explained below.

    - The output is easily readed in console with the proper print statements reffered from the assignment file.

# 2. Load Review file
    1. This python file can directly access the asin number and page number with the API key and returned the list of reviews in one go.
    2. Here we have passed the to_page = 3, because we want only 30 reviews per product. Here RainForest api's are returning 10 reviews per call, so if we need 100 reviews per product the need to pass to_page = 10.


# 3. Property loader from external file
    1. Have added the Propery loader from saperate file, so we can easily changed the file data and run accordingly.
    2. There are two property added. below is its description
        1. api_key - For the security purpose I've added API_KEY here, so the properties.py file can manage such secure data and process directly
        2. load_review_from_file - default value is false, this will be changed after first attempt, so user can run application without running rainforest api everytime

# Explanation for each Problem Statement and its Solutions
Note - Have changed the input json(provided in the assignment description) as simple as possible with input only string array of ASIN Ids of each product
#   1. Create a sample account in rainforest (https://www.rainforestapi.com/) and use review API to fetch reviews
    - Have created the account with my details and explore the rainforest API
    - Have changed the API according with 'How too get review data for each ASIN Id.
    
#   2. Get recent 30 reviews for the product Ids passed in an input file (Content of input file is given below)
    - As described above, one api request will got the 10 review. Have added the to+_age value as 3

#   3. Store reviews of all the products in a single dataframe
    - Have stored all the API call response converted to the required data structure and stored in single Dataframe.

#   4. Get the product Id which has maximum average review among the products
    - used groupBy function with the ASIN id and get the all the review's rating and get average out of it using max(mean()) combination will give the output.

#   5. Get product wise average review
    - As described in above step, Have used groupBy function with the ASIN id and get the all the review's rating and get average out of it using only mean() function

#   6. Get product wise longest review based on length of the “body” field
    - As easily describe here, we have already used GroupBy, Having, OrderBy and the Limit from the SQL database, here we have used assign with Lambda expression over with sort and group by with head(1) as limit 1. This will create the new DataFrame with dropping null values from body column applying the sort over lenght of the body, group by ASIN and head limit as 1.