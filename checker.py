#!/usr/bin/env python3

import json
import os 
from time import sleep
import urllib
import urllib.request
import random




while True:
    contents = urllib.request.urlopen("https://ttp.cbp.dhs.gov/schedulerapi/slot-availability?locationId=5020").read()
    contents_string = contents.decode("utf-8")
    contents_json = json.loads(contents_string)
    print(contents_json)
    
    if len(contents_json["availableSlots"]) > 0:
        os.system('say availbilities')
        break
    # be a good citizen
    random_number = random.randint(1, 5)
    sleep(random_number)
