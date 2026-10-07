import extract
import transform
import json

listaFilm = extract.lista_film("/movie/popular",20)
listaGeneri = extract.lista_generi("/genre/movie/list")

dictFilm = transform.transformaFilm(listaFilm,listaGeneri)

print(json.dumps(dictFilm,ensure_ascii=False,indent=4))
