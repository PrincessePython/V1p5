# Creer une fonction prenant en arguments une liste de produits obtenus depuis 
# openfoodfacts et qui retourne une liste de laquelle on a éliminé les produits n'ayant pas 
# de nom, de magasins, de catégorie ou de nutriscore.

import json
import requests

def cleaned_data():

    liste_fr_products = []
    mixed_data = []

    parametres = {
        "action" : "process",
        "tagtype_0":"nutrition_grades",
        "tag_contains_0": "contains",
        "tag_0": "a",
        "fields" : "product_name,stores",
        "page" : 1,
        "page_size":10,
        "json": True
        }
    r = requests.get("https://fr.openfoodfacts.org/cgi/search.pl", params=parametres)

    data = r.json()
    
    # dict_keys(['count', 'page', 'page_count', 'page_size', 'products', 'skip'])


    data = data["products"]
    liste_fr_products.append(data)
    liste_fr_products = liste_fr_products[0]
    print(liste_fr_products)

    for index in liste_fr_products:
        # extract each dictionnairy 
        # separate product name and stores 
        # save stores in a list (?)
        # remove products with no name, no store, no catégory, no nutriscore

cleaned_data()
