import extract
import transform
import json

listaFilm = extract.lista_film("/movie/popular",20)
film = transform.transformaFilm(listaFilm)
listaGeneri = extract.lista_generi("/genre/movie/list")
nuovaListaGeneri = transform.transformaGeneri(listaGeneri)

#print(json.dumps(film,ensure_ascii=False,indent=4))
print(json.dumps(nuovaListaGeneri,ensure_ascii=False,indent=4))
