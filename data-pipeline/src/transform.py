
from datetime import datetime

def transformaFilm(film):
    
    filmTrasformati = [
        {
            "nome" : movie.get("title"),
            "anno" : prendiAnno(movie.get("release_date")),
            "genere" : movie.get("genre_ids")
        } for movie in film
    ]
    return filmTrasformati
  
def prendiAnno(data):
    conversioneData = datetime.strptime(data, "%Y-%m-%d")
    return conversioneData.year

def transformaGeneri(listaDictGeneri):
    
    nuovalista = [{ "id" : scorri["id"], "nome" : scorri["name"]} for scorri in listaDictGeneri]
    
    return nuovalista