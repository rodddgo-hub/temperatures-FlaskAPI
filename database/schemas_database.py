#---CREATE DB IF NOT EXISTS - this queries have to used when the database not created
#-------------------------------------------------------------------------------------------------
CREATE_ROOMS_TABLE = (
    """
    CREATE TABLE IF NOT EXISTS rooms (
    id SERIAL PRIMARY KEY, 
    name TEXT
    );
    """
)
CREATE_TEMPS_TABLE = """
CREATE TABLE IF NOT EXISTS temperatures (
room_id INTEGER, 
temperature REAL, 
date TIMESTAMP, 
FOREIGN KEY(room_id) REFERENCES rooms(id) ON DELETE CASCADE
);
""" 
#-------------------------------------------------------------------------------------------------

#---INSERT INTO TABLES rooms and temperatures
#-------------------------------------------------------------------------------------------------
INSERT_ROOM_RETURN_ID = "INSERT INTO rooms (name) VALUES (%s) RETURNING id;"

INSERT_TEMP = "INSERT INTO temperatures (room_id, temperature, date) VALUES (%s, %s, %s);"
#-------------------------------------------------------------------------------------------------

#---QUERIES
#-------------------------------------------------------------------------------------------------
GLOBAL_NUMBER_OF_DAYS = ("""SELECT COUNT(DISTINCT DATE(date)) AS days FROM temperatures;""")

GLOBAL_AVG = """SELECT AVG(temperature) AS average FROM temperatures;"""
#-------------------------------------------------------------------------------------------------