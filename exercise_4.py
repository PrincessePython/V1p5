# Creer une fonction sans arguments qui retourne dans une liste les dictionnaires 
# représentant les produits téléchargés depuis 
# l'API de recherche avancé de openfoodfacts, par ordre de popularité.

import json
import requests

def liste_fr_products():

    liste_fr_products =[]

    parametres = {
        "action" : "process",
        "tagtype_0":"nutrition_grades",
        "tag_contains_0": "contains",
        "tag_0": "a",
        "sort_by":"unique_scans_n",
        "fields" : "product_name,stores",
        "page" : 1,
        "page_size":1000,
        "json": True
        }

    r = requests.get("https://fr.openfoodfacts.org/cgi/search.pl", params=parametres)

    data = r.json()
    
    data = data["products"]
    liste_fr_products.append(data)
    liste_fr_products = liste_fr_products[0]
    print(liste_fr_products)


        
liste_fr_products()

