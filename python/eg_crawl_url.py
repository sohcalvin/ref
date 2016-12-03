import requests
from bs4 import BeautifulSoup
from urllib.request import HTTPError, urlopen, Request
url = "http://www.bbc.com/news/business/markets/asiapacific/tsenik_tokn"
r = requests.get(url)
root = BeautifulSoup(r.content, "lxml")
# print(root)

# mydivs = root.findAll("div", {"class" : "update__body" })
mydivs = root.findAll("div", {"class" : "update__inner" })


for d in mydivs :
    print("-----------")
    update_body = d.findAll("div", {"class" : "update__body" })

    print(update_body)

# print(mydivs)

# def getUrlContent(url):
#     request = Request(url)
#     request.add_header('User-Agent', USER_AGENT)
#     try:
#         response = urlopen(request)
#         print ("start reading")
#         document = response.read().decode("utf-8", "ignore")
#         print ("done reading")
#         return document
#     except HTTPError as e:
#         logging.warn('HTTP Error {e.code}: {e}'.format(e=e))
