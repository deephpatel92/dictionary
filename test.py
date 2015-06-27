import time
import datetime
import json
import unirest

# These code snippets use an open-source library.
response = unirest.get("https://montanaflynn-dictionary.p.mashape.com/define?word=hello",
    headers={
        "X-Mashape-Key": "j6rDcjfVcVmshxp0Y102O2cL6vDrp16mL1FjsnsgRqpcl6fC3L",
        "Accept": "application/json"
    }
)

print response