# Creer une fonction sans arguments qui retourne dans une liste les noms des produits téléchargés 
# avec les paramètres par défaut depuis l'API de recherche avancé de openfoodfacts.

import json
import requests

def liste_nom_products():

    products_name_list = []

    parametres = {
        "action":"process",
        "json": True,
        "nutrition_grade": "A",
        "page": 1,
        "page_size": 20
                
    }
    r = requests.get("https://world.openfoodfacts.org/cgi/search.pl", params=parametres)

    # data = json.loads(r.text)
    # print(data)
    data = r.json()
    print(data)

liste_nom_products()