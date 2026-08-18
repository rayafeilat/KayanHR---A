import os
from flask import Flask
import psycopg

app= Flask(__name__)
DATABASEURL=os.environ.get("DATABASE_URL")

@app.route('/select', methods=['GET'])
with psycopg.connect(DATABASE_URL) as conn :
    with conn.cursor() as cur:
	cur.execute("SELECT 1;")
	result = cur.fetchone()
	print(" Respond was successful")

