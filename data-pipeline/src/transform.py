
from datetime import datetime

def transformaFilm(film):
    
    filmTrasformati = [
        {
            "id"   : movie["id"],  #valore non è opzionale , esiste al 100%
            "nome" : movie.get("title"),    #valore di dubbia esistenza, potrebbe non esistere
            "anno" : prendiAnno(movie.get("release_date")),
            "genere" : movie.get("genre_ids")
        } for movie in film
    ]
    return filmTrasformati


  
def prendiAnno(data):
    if not data:
        return None
    conversioneData = datetime.strptime(data, "%Y-%m-%d")
    return conversioneData.year

def transformaGeneri(listaDictGeneri):
    
    nuovalista = [{ "id" : scorri["id"], "nome" : scorri["name"]} for scorri in listaDictGeneri]
    
    return nuovalista


def transformaAttori(credits):
    attori = {}
    associazioni = set()

    for film in credits:
        idFilm = film["id"]

        for attore in film["cast"]:
            idAttore = attore["id"]

            attori[idAttore] = {
                "id": idAttore,
                "nome": attore["name"]
            }

            associazioni.add((idFilm, idAttore))

    return list(attori.values()), associazioni

def compleannoAttore(infoAttore):
    lista = {attore["id"]:attore.get("birthday") for attore in infoAttore}
    return lista


def listaAttori(attore,compleanno):
    listaAttore=[]
    for scorriAttore in attore:
        idAttore = scorriAttore["id"]

        listaAttore.append(
            {
                "id" : idAttore,
                "nome" : scorriAttore["nome"],
                "compleaano" : compleanno.get(idAttore)
            }
        )
    return listaAttore