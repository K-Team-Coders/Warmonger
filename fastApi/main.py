import os
from dotenv import load_dotenv

from loguru import logger
import psycopg2
from fastapi import FastAPI

from models import *

load_dotenv('../DB.ENV')

IP=os.environ.get("IP")
PORT=os.environ.get("PORT")
DBNAME=os.environ.get("DBNAME")
USER=os.environ.get("USER")
PASSWORD=os.environ.get("PASSWORD")

app = FastAPI()

conn = psycopg2.connect(
    dbname=DBNAME, 
    host=IP, 
    user=USER, 
    password=PASSWORD, 
    port=PORT)
cur = conn.cursor()

@app.post("/collectNewsAfter/")
def index(date):
    cur.execute(f"""SELECT * FROM news WHERE news.datetime > '{date}' """)
    date = cur.fetchall()
    return date
