import os
import psycopg2
from flask import Flask, request
from dotenv import load_dotenv
from datetime import datetime,timezone

#api modules
import database


load_dotenv()

app = Flask(__name__)

try:
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )
    print("Conexão estabelecida!")
    

except:
    print("do not can connect to database")

@app.route('/')
def home():
    return "Hello World!"


@app.post('/api/room')
def create_room():
    data = request.get_json()
    name = data['name']
    
    with conn:
        with conn.cursor() as cursor:
            
            #create database if not exists
            cursor.execute(database.CREATE_ROOMS_TABLE)

            #creating room w name
            cursor.execute(database.INSERT_ROOM_RETURN_ID, (name,))

            room_id = cursor.fetchone()[0] #returns the query - when room created by the name inserted, this query return her id. 
    
    return {"id": room_id, "message": f"room {name} created."}, 201 #201 is the status code.
    

@app.post('/api/temperature')
def add_temp():
    # Room Name | Room ID | Temperature

    data= request.get_json()
    temperature= data["temperature"]
    room_id= data["room"]

    try:
        date = datetime.strptime(data["date"], "%d-%m-%Y %H:%M")
        ...
    except KeyError: #references to: data["key"]
        data = datetime.now(timezone.utc)
        ...


app.run(host="127.0.0.1", port=3000)
