import os
import psycopg2
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from datetime import datetime,timezone

#api modules
import database.schemas_database as schemas_database
import simulated_interface.user_input as user_input


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

except ConnectionRefusedError:
    print("Do not can connect to database")


#--- GET and POST of api/room endpoint ----------
@app.get('/api/room/')
def get_room_name():
    room_name = user_input.getting_room_name()

    return jsonify({'name': room_name}), 200

@app.post('/api/room')
def create_room():
    data = request.get_json()
    room_name = data['name']
    with conn:
        with conn.cursor() as cursor:
            #creating room w name
            cursor.execute(schemas_database.INSERT_ROOM_RETURN_ID, (room_name,))
            room_id = cursor.fetchone()[0] #returns the query - when room was created by the name inserted, this query return her id. 
    
    return {"id": room_id, "message": f"room {room_name} created."}, 201 #201 is the status code.
#-------------------------------------------------------------------------------------------------


#--- GET and POST of api/temperature endpoint ---------

@app.post('/api/temperature')
def add_temp():
    data= request.get_json()

    # Room Name | Room ID | Temperature
    temperature= data["temperature"]
    room_id= data["room"]

    try:
        date = datetime.strptime(data["date"], "%d-%m-%Y %H:%M")
        ...
    except KeyError: #references to: data["key"]
        data = datetime.now(timezone.utc)
        ...

    with conn.cursor() as cursor:
        cursor.execute(schemas_database.CREATE_TEMPS_TABLE)
        cursor.execute(schemas_database.INSERT_TEMP, (room_id,temperature,date))
    return {"message":"temperature added"}, 201
#-------------------------------------------------------------------------------------------------

app.run(host=os.getenv("HOST"), port=os.getenv("PORT"))
