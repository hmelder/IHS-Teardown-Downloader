#!/usr/bin/python3 env
from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib.request
import re
import json

query = input("Enter your search term: ").replace(" ", "%20")
downloadPath = input("Select a download path (i.e /tmp/): ")
pages = input("Modify Search Query (Pages are cycled through) Enter = Default: ")

if pages == "":
	pages = 2	#Default Cycle

deviceList = []
titleList = []
pagesUrl = 1

for i in range(int(pages)):
    html = urlopen("https://benchmarking.ihsmarkit.com/teardowns?q="+ str(query) +"&pageNumber="+ str(pagesUrl) +"&o=") # Extraction URL
    bsObj = BeautifulSoup(html.read(), "html.parser")

    for link in bsObj.find_all('a', href=re.compile('^/Teardowns/detail/')): # Lists all internal teardown links and splits the Query IDs
        getLinks = link.get('href').split("=")
        otherID = (getLinks[1][:6]) #Purpose unknown
        deviceID = (getLinks[1][7:15])
        deviceList.append(deviceID)

    for title in bsObj.find_all('div',attrs={"class" : "galleryText"}): # Extract all titles from the search result
        result = (title.text).strip()
        titleList.append(result)
    pagesUrl = pagesUrl+1

 #   if usrResponse in  titleList:
#JSON Extractor
photoList = []
labelList = []
phototitleList = []
deviceID = 2869
listPosition = 0

def retrieveUrl(positionReturn):
    array = 0
    response = urlopen("https://benchmarking.ihsmarkit.com/Teardowns/binary/devices/"+ str(deviceList[positionReturn]) +"/photos/")
    data = json.load(response)
    for item in data:
        json_str = json.dumps(data[int(array)])
        resp = json.loads(json_str)
        photoList.append(resp['PhotoID'])
        labelList.append(resp["FileName"])
        phototitleList.append(resp["Label"].replace("/", ""))
        array = array+1

def downloadUrl(position):
    counter = 0
    for item in photoList: #Downloading Photos with information from backend
        url = "https://benchmarking.ihsmarkit.com/Teardowns/binary/devices/"+ str(deviceList[int(position-1)]) +"/photos/"+ str(photoList[counter]) +"/binary" #Downloading
        urllib.request.urlretrieve(url, str(downloadPath)+ "/" + str(phototitleList[counter]) +".jpg") #Download path
        counter = counter+1