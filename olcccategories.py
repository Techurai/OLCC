import requests
from bs4 import BeautifulSoup
import pandas as pd

bottles= []


WelcomeController = 'http://www.oregonliquorsearch.com/servlet/WelcomeController?selMonth=3&selDay=10&selYear=1981&btnSubmit=Enter+Site'
Scotch = 'http://www.oregonliquorsearch.com/servlet/FrontController?view=browsecategoriesallsubcategories&action=select&category=SCOTCH'


#Establish Session
s = requests.Session()
r = s.get(WelcomeController)

#Retrieve Category Results
r = s.get(Scotch)

soup = BeautifulSoup(r.content, features="lxml")




table = soup.find('table', {'class':'list'})

# --Works--
each_item = [item for item in table.find_all('tr') if item.find('td')]
for child in each_item:
    li = [each.text for each in child.find_all('td') if each.text]
    bottles.append(li)

for bottle in bottles:
    print(bottle)
