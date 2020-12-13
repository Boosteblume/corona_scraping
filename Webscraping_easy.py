#Webscraping einfache Variante

import requests_html

dict_of_cities= { "Freiburg": "https://www.corona-in-zahlen.de/landkreise/sk%20freiburg%20i.breisgau/"
, "Kulmbach": "https://www.corona-in-zahlen.de/landkreise/lk%20kulmbach/"
, "Hamburg": "https://www.corona-in-zahlen.de/landkreise/sk%20hamburg/"
, "Sigmaringen": "https://www.corona-in-zahlen.de/landkreise/lk%20sigmaringen/" }

list_of_cities=["Freiburg", "Kulmbach", "Hamburg", "Sigmaringen"]

#choose the city you want the numbers

def choose_city():
    print(list_of_cities)
    print("Choose one of the cities mentioned above" )
    print("Answer in number 1-4")
    answered_city=int(input())-1
    print("You choose " + list_of_cities[answered_city])
    return(list_of_cities[answered_city])

#open the right url for the choosen city and make it scrapable

#def open_url():
 #   target_url= session.get()


choose_city()

print(dict_of_cities[])