import urllib.request
import re
import json
from pprint import pprint





while True:
    try:
        c_code = input("Please input the country code (enter 'quit' to quit): ")
        if(c_code =='quit'):
            break
        url="https://restcountries.eu/rest/v1/alpha/"+c_code
        page = urllib.request.urlopen(url)
    
        content=page.read()
        content_string = content.decode("utf-8")
        json_data=json.loads(content_string)
        print(json_data)
        pprint(json_data)
    except urllib.error.HTTPError:
        print("Cannot find this country, please try again.")
