# Creer une fonction sans arguments qui retourne dans une liste les dictionnaires 
# représentant les produits téléchargés depuis 
# l'API de recherche avancé de openfoodfacts, par ordre de popularité.

import json
import requests

def liste_fr_products():

    liste_fr_products =[]

    parametres = {
        "action" : "process",
        "tagtype_0":"categories",
        "tag_contains_0":"contains",
        "tag_0":"pizza",
        "fields" : "product_name,stores",
        # "unique_scans_n": "top-country-fr-scans-2020",
        "page" : 1,
        "page_size":50,
        "json": True
        }

    r = requests.get("https://fr.openfoodfacts.org/cgi/search.pl", params=parametres)

    data = r.json()
    
    # dict_keys(['count', 'page', 'page_count', 'page_size', 'products', 'skip'])

    a = data["products"]
    print(a)

liste_fr_products()