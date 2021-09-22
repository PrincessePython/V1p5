# Creer une fonction sans arguments qui affiche les noms des produits téléchargés
# avec les paramètres par défaut depuis l'API de recherche avancé de openfoodfacts, 
# ainsi que le nombe de produits téléchargés.


import requests
from requests.models import Response
import json
# from pprint import pprint


# r = requests.get("https://world.openfoodfacts.org/cgi/search.pl?search_terms=banania&search_simple=1&action=process&json=1&page_size=20&page_size=1")
# print(r.json())

def liste_nom_products():

    products_name_list = []

    parametres = {
        "action":"process",
        "json" : True,
        "nutrition_grade": "A",
        "page": 1,
        "page_size": 20
                
    }
    r = requests.get("https://world.openfoodfacts.org/cgi/search.pl", params=parametres)

    data = r.json()

    # dict_keys(['count', 'page', 'page_count', 'page_size', 'products', 'skip'])

    one_product = data["products"][1]['product_name_fr']
    print(one_product)

liste_nom_products()