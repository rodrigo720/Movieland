import time
import extract

idAttori = [43774, 6193, 287]

inizio = time.perf_counter()

risultato = extract.infoAttori(idAttori)

fine = time.perf_counter()

print("Attori estratti:", len(risultato))
print(f"Tempo impiegato: {fine - inizio:.2f} secondi")