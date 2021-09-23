# Creer une fonction sans arguments qui retourne dans une liste les noms des produits téléchargés 
# avec les paramètres par défaut depuis l'API de recherche avancé de openfoodfacts.

import json
import requests

def liste_nom_products():

    products_name_list = []

    parametres = {
        "action":"process",
        "tagtype_0":"categories",
        "tag_contains_1":"contains",
        "nutrition_grade": "A",
        # "additive":"without",
        # "tagtype_0":"stores",
        # "tagtype_1":"categorie",
        "fields":"product_name",
        "page": 1,
        # "page":2,
        # "page":3,
        # "page":4,
        # "page":5,
        "page_size": 1000,
         "json": True,
                
    }
    r = requests.get("https://world.openfoodfacts.org/cgi/search.pl", params=parametres)

    data = r.json()

    # dict_keys(['count', 'page', 'page_count', 'page_size', 'products', 'skip'])

    # Get a list of dicts for 1000 products
    list_of_products = data["products"][0:-1]
    print(list_of_products)
   
  
liste_nom_products()