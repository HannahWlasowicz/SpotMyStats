import json
import urllib.request
# userid 22tacmly46bov5lciv4dwew4y?si=SZU-y7RIRCeRMA7l95xL9Q

def getUsersSong(url):
    response = urllib.request.urlopen(url)
    content_string = response.read().decode()
    content = json.loads(content_string)
    retVal = []
    #process data
    return json.dumps(retVal)
