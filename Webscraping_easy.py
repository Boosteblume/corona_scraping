#Webscraping einfache Variante

import requests
from bs4 import BeautifulSoup

dict_of_cities = { "Freiburg": r"https://www.corona-in-zahlen.de/landkreise/sk%20freiburg%20i.breisgau/"
, "Kulmbach": r"https://www.corona-in-zahlen.de/landkreise/lk%20kulmbach/"
, "Hamburg": r"https://www.corona-in-zahlen.de/landkreise/sk%20hamburg/"
, "Sigmaringen": r"https://www.corona-in-zahlen.de/landkreise/lk%20sigmaringen/" }

list_of_cities = ["Freiburg", "Kulmbach", "Hamburg", "Sigmaringen"]


#choose the city you want the numbers
def choose_city():
    print(list_of_cities)
    print("Choose one of the cities mentioned above" )
    print("Answer in numbers 1-4")

    city_number = int(input())-1

    return (list_of_cities[city_number])

answered_city = choose_city()

print("You choose " + answered_city)
print("")
print(dict_of_cities[answered_city])
print("")

#open the url and scrape for the 7-days-incidenc
def newinfections():
    url = dict_of_cities[answered_city]
    url_content = requests.get(url).text
    soup = BeautifulSoup(url_content, "html.parser")

    #returns a list of all card-title of the website and i want value no.4
    list_of_numbers = soup.find_all("p", class_="card-title")[3].text
    return list_of_numbers

print("The current 7-day incidence value is "+ newinfections())
print("")


#here is the scrapping for the total infections
def totalinfections():
    url = dict_of_cities[answered_city]
    url_content = requests.get(url).text
    soup = BeautifulSoup(url_content, "html.parser")
    #returns a list of all card-title of the website and i want value no.2
    list_of_numbers = soup.find_all("p", class_="card-title")[1].text
    return list_of_numbers


print("The total amount of infections is " + totalinfections())
print("")