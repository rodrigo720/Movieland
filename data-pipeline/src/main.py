import extract
import transform
import load
import json
from collections import Counter

listaFilm = extract.lista_film("/movie/popular",5)
#print(f"prima della transform{len({movie["id"] for movie in listaFilm})}")

film = transform.transformaFilm(listaFilm)

conteggio = Counter(movie["id"] for movie in film)
duplicati={
    id_film: numero for id_film,numero in conteggio.items() if numero>1
}
#print(duplicati)

listaGeneri = extract.lista_generi("/genre/movie/list")
nuovaListaGeneri = transform.transformaGeneri(listaGeneri)

idFilm = {movie["id"] for movie in film}
credits = extract.lista_attori(idFilm)
#print(json.dumps(credits[:2],ensure_ascii=False,indent=4))

attoriDati,associazioni = transform.transformaAttori(credits)

#print(attoriDati[0])
#print(attore["id"] for attore in attoriDati[:5])

idAttori = [scorriAttori["id"] for scorriAttori in attoriDati]
#print(list(idAttori[:5]))

infoAttore = extract.infoAttori(idAttori)

compleannoAttore=transform.compleannoAttore(infoAttore)

#print(list(compleannoAttore.items())[:5])

attori = transform.listaAttori(attoriDati,compleannoAttore)

print("Extract:", infoAttore[:3])
print("Compleanni:", list(compleannoAttore.items())[:3])
print("Transform:", attori[:3])

print(
    "Compleanni presenti:",
    sum(a["compleanno"] is not None for a in attori)
)


load.caricaGeneri(nuovaListaGeneri)
load.caricaFilm(film)
load.caricaAttori(attori,associazioni)

