
from datetime import datetime

def transformaFilm(film):
    filmTrasformati = [
        {
            "nome" : movie.get("title"),
            "data" : prendiAnno(movie.get("release_date")),
            "genere" : prendiGeneri(movie.get("genre_ids"))
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


