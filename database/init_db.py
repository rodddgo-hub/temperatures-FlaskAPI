import psycopg2
from dotenv import load_dotenv
from os import getenv

# api modules
import database.schemas_database as schemas_database

def init_database():
    
    load_dotenv()
    
    try:
        conn = psycopg2.connect(
            host=getenv("DB_HOST"),
            port=getenv("DB_PORT"),
            dbname=getenv("DB_NAME"),
            user=getenv("DB_USER"),
            password=getenv("DB_PASSWORD")
            )
        print("Connection Stabilished!")

    except ConnectionError as e:
        print(e)        

    with conn:
            with conn.cursor() as cursor:
                cursor.execute(schemas_database.CREATE_ROOMS_TABLE)
                cursor.execute(schemas_database.CREATE_TEMPS_TABLE)
                
    return "Database created was success"