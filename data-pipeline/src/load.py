import psycopg
import os 
from dotenv import load_dotenv

def connessioneDB ():
    load_dotenv()
    return psycopg.connect(
    host = os.getenv("DB_HOST"),
    port = os.getenv("DB_PORT"),
    dbname = os.getenv("DB_NAME"),
    user = os.getenv("DB_USER"),
    password = os.getenv("DB_PASSWORD")
    ) 

def caricaGeneri(generi):
    with connessioneDB() as connessione:
        with connessione.cursor() as cursor :
            query = """
                    INSERT INTO genere(id,nome) VALUES(%s,%s)   
                    ON CONFLICT(id) DO UPDATE SET nome = EXCLUDED.nome 
                    """
            
            for genere in generi:
                valori = [genere["id"],genere["nome"]]
                cursor.execute(query,valori)




def caricaFilm(film):
    with connessioneDB() as connessione:
        with connessione.cursor() as cursor:
            query1 = """
                     INSERT INTO film(id,nome,anno) VALUES(%s,%s,%s) 
                     ON CONFLICT(id) DO UPDATE SET nome = EXCLUDED.nome  
                     , anno = EXCLUDED.anno
                     """

            query2 = """
                     INSERT INTO film_genere(id_film,id_genere) VALUES(%s,%s) 
                     ON CONFLICT(id_film,id_genere) DO NOTHING
                     """

            for movie in film:
                valoriFilm = [movie["id"],movie["nome"],movie["anno"]]
                cursor.execute(query1,valoriFilm)
                for generi in movie["genere"]:
                    valoriVincolo = [movie["id"],generi]
                    cursor.execute(query2,valoriVincolo)
