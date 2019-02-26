import json
import urllib.request

def getUsersSong(url):
    response = urllib.request.urlopen(url)
    content_string = response.read().decode()
    content = json.loads(content_string)
    retVal = []
    #process data
    return json.dumps(retVal)
