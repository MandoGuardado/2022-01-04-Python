#!/usr/bin/env python3
"""Alta3 Research
   Star Wars API HTTP response parsing"""

# pprint makes dictionaries a lot more human readable
from pprint import pprint

# requests is used to send HTTP requests (get it?)
import requests

#URL = "https://swapi.dev/luke/force"      # Comment out this line
URL= "https://swapi.dev/api/people/4/"     # Uncomment this line
URL2 = "https://swapi.dev/api/films/1/"
URL3 = "https://swapi.dev/api/starships/13/"

def main():
    """sending GET request, checking response"""

    # SWAPI response is stored in "resp" object
    resp= requests.get(URL)
    resp2 = requests.get(URL2)
    resp3 = requests.get(URL3)
    # check to see if the status is anything other than what we want, a 200 OK
    if resp.status_code == 200 and resp2.status_code == 200 and resp3.status_code == 200:
        # convert the JSON content of the response into a python dictionary
        vader= resp.json()
        data2 = resp2.json()
        data3 = resp3.json()
       # pprint(vader)
        print(f'{vader["name"]} was born in the year {vader["birth_year"]}. His eyes are now {vader["eye_color"]} and his hair color is {vader["hair_color"]}.')
        print(f'He first appeared in the movie {data2["title"]} and could be found flying around in his {data3["name"]}.')

    else:
        print("That is not a valid URL.")

if __name__ == "__main__":
    main()

