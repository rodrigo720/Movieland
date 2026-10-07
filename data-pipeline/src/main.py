import extract
import transform
import load
import json

listaFilm = extract.lista_film("/movie/popular",20)
film = transform.transformaFilm(listaFilm)
listaGeneri = extract.lista_generi("/genre/movie/list")
nuovaListaGeneri = transform.transformaGeneri(listaGeneri)
load.caricaGeneri(nuovaListaGeneri)

#print(json.dumps(film,ensure_ascii=False,indent=4))
#print(json.dumps(nuovaListaGeneri,ensure_ascii=False,indent=4))
