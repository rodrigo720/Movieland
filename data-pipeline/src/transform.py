
from datetime import datetime

def transformaFilm(film,listageneri):
    
    dictGeneri = transformaGeneri(listageneri)

    filmTrasformati = [
        {
            "nome" : movie.get("title"),
            "anno" : prendiAnno(movie.get("release_date")),
            "genere" : prendiGeneri(movie.get("genre_ids"),dictGeneri)
        } for movie in film
    ]
    return filmTrasformati
  
def prendiAnno(data):
    conversioneData = datetime.strptime(data, "%Y-%m-%d")
    return conversioneData.year

def transformaGeneri(listaGeneri):
    generiList = {
    generi["id"] : generi["name"] for generi in listaGeneri 
    }

    return generiList

def prendiGeneri(listaIdGeneri,dictGeneri):
    generi = [
        dictGeneri[scorriLista] for scorriLista in listaIdGeneri 
    ]
    return generi
