import requests  # request library to make API calls from python on internet
from countries import countries  # list of countries from file its a local api

print('-----------------------------------------------')

# input fix
user_country = input("Enter country name: ").strip().title()  # user input for country name and fromat and remove the space and tilte the first letter of each word

# check in your file
if user_country not in countries:
    print("Country not found in your file ❌")
else:
    try:
        # exact match API
        url = f"https://restcountries.com/v3.1/name/{user_country}?fullText=true"  # fetch the data from restcountries API using the country name and fullText=true for exact match
        response = requests.get(url) # make a GET request to the API and store the response in a variable

        if response.status_code != 200:
            print("Country not found on server ❌") # check the status code of the response if its not 200 then print country not found on server
        else:
            data = response.json() # parse the response as JSON and store it in a variable data is a list of dictionaries and we need to get the capital from the first dictionary and if capital is not available then we will print Not Available

            capital = data[0].get('capital', ["Not Available"])[0] # get the capital from the first dictionary and if capital is not available then we will print Not Available

            print(f"Capital of {user_country} is {capital}") # print the capital of the country using f-string

    except Exception as e:
        print("Error:", e)