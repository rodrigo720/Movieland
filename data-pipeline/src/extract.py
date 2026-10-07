import os
import requests
import json
from dotenv import load_dotenv

    
def estrazioneFileJson(endpoint,params=None):

    load_dotenv()

    token = os.getenv("TMDB_TOKEN")
    if not token:
        raise ValueError("Token non trovato")

    url_base= "https://api.themoviedb.org/3"

    URL = url_base + endpoint

    headers = {
    "Authorization" : f"Bearer {token}",
    "accept" : "application/json"
    }
    """
    params
    Con questo dict params , dopo aver dichiarato il request.get , mi costruisce url+params adattando il dict 
    come se fosse una query parameters, in questo modo interrogo il server con i dati desiderati
    NOTA: le richieste chiave del dict devono essere esistenti e corrispondenti a quello che si vuole cercare
    
    """

    if params is not None:

        response = requests.get(URL, headers= headers,params=params)    
    else:
        response = requests.get(URL, headers= headers)

    
    if response.status_code == 200:
        return response.json()

    return Exception(f"errore: {response.status_code}")

    

#print(json.dumps(estrazioneFileJson("/movie/popular"),ensure_ascii=False,indent=4))
#print(json.dumps(estrazioneFileJson("/genre/movie/list"),ensure_ascii=False,indent=4))

def lista_film(endpoint,pages) :
    films = []
    for i in range(1 , pages+1):
        params = {
            "page" : i
        }
        container = estrazioneFileJson(endpoint,params)
        result = container["results"]
        films.extend(result)
    return films
"""
TEST lista_film
lista = lista_film("/movie/popular",20)
#mi resituisce una lista di dict
print(type(lista))

print(json.dumps(lista[0],ensure_ascii=False,indent=4))
"""

def lista_generi(endpoint):
    params = {
        "language" : "it-IT"
    }
    container = estrazioneFileJson(endpoint,params)
    return container["genres"]

#print(json.dumps(lista_generi("/genre/movie/list"),ensure_ascii=False,indent=4))

