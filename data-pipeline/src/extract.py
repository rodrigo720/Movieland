import os
import requests
import json
import transform
from dotenv import load_dotenv

    
def estrazioneFileJson(endpoint,params=None,session=None):

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
    client = session if session is not None else requests #utilissa sessione gia esistente oppure singola request

    response = client.get(
    URL,
    headers=headers,
    params=params,
    timeout=(5, 15)#5 connect timeout , 15 read timeout
    )

    if response.status_code == 200:
        return response.json()

    raise Exception(f"errore: {response.raise_for_status()}")

    

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

#totale_id = {movie["id"] for movie in lista_film("/movie/popular",20)}#uso un set comprehension con{}
#print(f"il numero di id sono : {len(totale_id)}")
#print(len(lista_film("/movie/popular",20)))
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

#ATTORI ESTAZIONE
#https://api.themoviedb.org/3/movie/{movie_id}/credits

"""
ATTORI ESTAZIONE
https://api.themoviedb.org/3/movie/{movie_id}/credits
uso i metodi dela trasformazione dei film per ricavarmi la set di ID e poi mi ricavo gli attori

"""
def lista_attori(idFilm):
    lista = []

    for id in idFilm:
        risultato = estrazioneFileJson(f"/movie/{id}/credits")
        lista.append(risultato)

    return lista

#ANNO DI NASCITA DEGLI ATTORI:
#GET https://api.themoviedb.org/3/person/{person_id}
def infoAttori(idAttori):
    dettagliAttore = []
    with requests.Session() as session:
        for personId in idAttori:
            dettagli = estrazioneFileJson(f"/person/{personId}",session=session)
            dettagliAttore.append(dettagli)
    return dettagliAttore


