# dataorb_assignment

1. # How to run
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

