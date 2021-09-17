# Creer une fonction sans arguments qui affiche les noms des produits téléchargés 
# avec les paramètres par défaut depuis l'API de recherche avancé de openfoodfacts, 
# ainsi que le nombe de produits téléchargés.


import requests
from requests.models import Response
import json
# from pprint import pprint


# r = requests.get("https://world.openfoodfacts.org/cgi/search.pl?search_terms=banania&search_simple=1&action=process&json=1&page_size=20&page_size=1")
# print(r.json())

def liste_of_products():

     
    r = requests.get("http://world.openfoodfacts.org/cgi/search.pl",  params={
        "action":"process",
        "page":"1",
        "page_size":"20",
        "json":True
        } )

    
    # data = json.loads(r.text)
    # print(type(data))
    
    data = r.json()
    print(data)

liste_of_products()
