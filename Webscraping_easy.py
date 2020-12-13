#Webscraping einfache Variante

import requests
from bs4 import BeautifulSoup
import csv

from requests_html import HTMLSession

dict_of_cities = { "Freiburg": r"https://www.corona-in-zahlen.de/landkreise/sk%20freiburg%20i.breisgau/"
, "Kulmbach": r"https://www.corona-in-zahlen.de/landkreise/lk%20kulmbach/"
, "Hamburg": r"https://www.corona-in-zahlen.de/landkreise/sk%20hamburg/"
, "Sigmaringen": r"https://www.corona-in-zahlen.de/landkreise/lk%20sigmaringen/" }

list_of_cities = ["Freiburg", "Kulmbach", "Hamburg", "Sigmaringen"]



#choose the city you want the numbers

def choose_city():
    print(list_of_cities)
    print("Choose one of the cities mentioned above" )
    print("Answer in number 1-4")

    city_number = int(input())-1

    return(list_of_cities[city_number])

answered_city = choose_city()

print("You choose " + answered_city)
get_the_document()

#open the url and scrape for the 7-days-incidenc
def ():
    url = dict_of_cities[answered_city]
    session = HTMLSession()
    url_session = session.get(url)
    
    if url_session.html.find("p.card-text") == "Neuinfektionen (7-Tage-Inzidenz) ":
        Neuinfektionen = url_session.html.find()

#beautifulsoup find all 