import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','PortfolioSite.settings')
django.setup()

import requests
import json
import pprint
from mySite.models import repoContent, contributors, Languages

# creates a requests session
def gitConnect():
        with open('git.key') as f:
            github_token = f.read().strip()
        session = requests.session()
        session.auth = ('SelimHA', github_token)
        return session

def getDictionary():
        return json.loads(requests.get("https://api.github.com/users/SelimHA/repos").content)

def getLanguages(dictEl):
        return json.loads(session.get(dictEl["languages_url"]).content)

def getTotalLanguages():
        for i in repoDict:
                curDictEl = getLanguages(i)
                for key, value in curDictEl.items():
                        curLang = Languages.objects.get_or_create(language = key)[0]
                        print(curLang)
                        curLang.usage =  curLang.usage  + value
                        curLang.save()

def getContributors(urlAddress):
        tempList = json.loads(session.get(urlAddress).content)
        contributorList =[]
        for el in tempList:
                curDict = {"Name":el["login"],"Contribution":el["contributions"]}
                contributorList.append(curDict)
        return contributorList

def getIcon(languageName):
        if(languageName=="Java"):
                return "fab fa-java"
        elif(languageName=="Python"):
                return "fab fa-python"
        elif(languageName=="HTML"):
                 return "fab fa-html5"
        elif(languageName=="Kotlin"):
                return "fab fa-android"
        elif(languageName=="Swift"):
                return "fas fa-apple-alt"
        elif(languageName=="C" or languageName=="C++" or languageName=="C#"):
                return "fab fa-cuttlefish"
        else:
                return "fas fa-file"

def getAllProjectDetails():
        repoContent.objects.all().delete()
        contributors.objects.all().delete()
        for el in repoDict:
                title = el["full_name"]
                contributor_list = getContributors(el["contributors_url"])
                pprint.pprint(contributor_list)
                description = el["description"]
                link = el["html_url"]
                language = el["language"]
                curRepo = repoContent.objects.get_or_create(title=title,language=language, link=link, description=description, date_created="")[0]
                for contrib in contributor_list:
                        contributors.objects.get_or_create(title=curRepo, contribName = contrib["Name"], commits = str(contrib["Contribution"]))[0]
#Get session
session=gitConnect()
#Get dictionary
repoDict = getDictionary()
pprint.pprint(repoDict)
getAllProjectDetails()
getTotalLanguages()