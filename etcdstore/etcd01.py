#!/usr/bin/python3

import requests
import pprint

def main():

    # issue an HTTP PUT transaction to store our data within /keys/requests
    # in this case, PUT created a 'file' called '/requests', with a 'value' of 'http for humans'
    # r is the response code resulting from the PUT
    r = requests.put("http://127.0.0.1:2379/v2/keys/requests", data={'value': 'http for humans'})
    print(f"Status Code - {r.status_code}") # return the status code associated with object r
    # pretty print the json in the response
    pprint.pprint(r.json())

    print('******')

    # issue an HTTP PUT transaction to store our data within /keys/requests
    # in this case, PUT updated a 'file' called '/requests', with a 'value' of 'http for humans'
    # r is the response code resulting from the PUT
    r = requests.put("http://127.0.0.1:2379/v2/keys/requests", data={'value': 'http for humans, version 2'})
    print(f"Status Code - {r.status_code}") # return the status code associated with object r
    # pretty print the json in the response
    pprint.pprint(r.json())

    print('******')

    # issue an HTTP GET to our keys/requests
    r = requests.get("http://127.0.0.1:2379/v2/keys/requests")
    print(f"Status Code - {r.status_code}") # return the status code associated with object r
    # pretty print the json in the response
    pprint.pprint(r.json())

if __name__ == "__main__":
    main()

