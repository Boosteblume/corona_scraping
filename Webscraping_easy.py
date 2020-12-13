#Webscraping einfache Variante

import requests
import csv

from requests_html import HTMLSession

dict_of_cities = { "Freiburg": "https://www.corona-in-zahlen.de/landkreise/sk%20freiburg%20i.breisgau/"
, "Kulmbach": "https://www.corona-in-zahlen.de/landkreise/lk%20kulmbach/"
, "Hamburg": "https://www.corona-in-zahlen.de/landkreise/sk%20hamburg/"
, "Sigmaringen": "https://www.corona-in-zahlen.de/landkreise/lk%20sigmaringen/" }

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

#now lets open the choosen url in a file
def get_the_document():
    url = dict_of_cities[answered_city]
    session = HTMLSession()
    url_variable = session.get(url)