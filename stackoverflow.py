import pandas as pd
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

myurl = 'https://stackoverflow.com/users/696257/dkulkarni'

# opering up the connection and grabbing the page
uStack = uReq(myurl)
page_html = uStack.read()
uStack.close()

# html parsing
page_soup = soup(page_html, "html.parser")

# get user info
container = page_soup.findAll("div", {"class":"mt24 user-card"})

container=container[0]
name_container = name = container.findAll("div",{"class":"grid--cell fw-bold"})
name = name_container[0].text.strip()

gold_container = container.findAll("div",{"class":"grid ai-center badge1-alternate"})
gold = gold_container[0].text.strip()

silver_container = container.findAll("div",{"class":"grid ai-center badge2-alternate"})
silver = silver_container[0].text.strip()

bronze_container = container.findAll("div",{"class":"grid ai-center badge3-alternate"})
bronze = bronze_container[0].text.strip()

repulation_container = container.findAll("div",{"class":"grid--cell fs-title fc-dark"})
repulation = repulation_container[0].text.strip()

top_container = container.findAll("span",{"class":"js-rank-badge grid--cell s-badge s-badge__votes fs-fine bc-blue-3 fc-blue-700"})
top = top_container[0].text.strip()

answer_container = container.findAll("div",{"class":"grid--cell fs-body3 fc-dark fw-bold"})
answer = answer_container[0].text.strip()

question_container = container.findAll("div",{"class":"grid--cell fs-body3 fc-dark fw-bold"})
question = question_container[1].text.strip()

reached_container = container.findAll("div",{"class":"grid--cell fs-body3 fc-dark fw-bold"})
reached = reached_container[2].text.strip()


stackuser  = pd.DataFrame(
    {
        'Name': [name],
        'Gold': [gold],
        'Silver': [silver],
        'Bronze': [bronze],
        'Repulation': [repulation],
        'Answers': [answer],
        'Questions': [question],
        'Reached': [reached],
        'Ranking': [top]
    }    
)
print(stackuser)

stackuser.to_csv('UserStackoverflow.csv')