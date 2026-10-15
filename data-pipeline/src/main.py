import extract
import transform
import load
import json
from collections import Counter




listaFilm = extract.lista_film("/movie/popular",20)
#print(f"prima della transform{len({movie["id"] for movie in listaFilm})}")

film = transform.transformaFilm(listaFilm)

conteggio = Counter(movie["id"] for movie in film)
duplicati={
    id_film: numero for id_film,numero in conteggio.items() if numero>1
}
#print(duplicati)
id

listaGeneri = extract.lista_generi("/genre/movie/list")
nuovaListaGeneri = transform.transformaGeneri(listaGeneri)

idFilm = {movie["id"] for movie in film}
credits = extract.lista_attori(idFilm)


attori,associazioni = transform.transformaAttori(credits)
print(attori[0])
#print(associazioni)#associazioni sono dei dict
print(type(attori))
print(type(associazioni))
print(type(transform.transformaAttori(credits)))

print(f"prima del load:{len({movie["id"] for movie in film})}")
#load.caricaGeneri(nuovaListaGeneri)
#load.caricaFilm(film)

