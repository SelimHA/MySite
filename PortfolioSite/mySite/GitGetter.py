import requests
import json
import pprint
def getDictionary():
        return json.loads(requests.get("https://api.github.com/users/SelimHA/repos").content)

def getLanguages(dictEl):
        return json.loads(requests.get(dictEl["languages_url"]).content)

def getTotalLanguages():
        cur_dict = getDictionary()
        toReturn = {}
        for i in cur_dict:
                curDictEl = getLanguages(i)
                for key, value in curDictEl.items():
                        if(key in toReturn.keys()):
                                toReturn[key]+=value
                        else:
                                toReturn[key]=value
        return toReturn
