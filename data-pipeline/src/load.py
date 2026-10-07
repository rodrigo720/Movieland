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
            query = "INSERT INTO genere(id,nome) VALUES(%s,%s)"
            
            for genere in generi:
                valori = [genere["id"],genere["nome"]]
                cursor.execute(query,valori)



    
