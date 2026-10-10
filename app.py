import os
import psycopg2
from flask import Flask
from dotenv import load_dotenv









load_dotenv()

app = Flask(__name__)

conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)
print("Conexão estabelecida!")

conn.close()

@app.get('/')
def home():
    return "hello home"

app.run(host='127.0.0.1',port=3000)