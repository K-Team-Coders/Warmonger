import os
from dotenv import load_dotenv

from loguru import logger
import psycopg2
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

load_dotenv('../DB.ENV')

IP=os.environ.get("IP")
PORT=os.environ.get("PORT")
DBNAME=os.environ.get("DBNAME")
USER=os.environ.get("USER")
PASSWORD=os.environ.get("PASSWORD")


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

conn = psycopg2.connect(
    dbname=DBNAME, 
    host=IP, 
    user=USER, 
    password=PASSWORD, 
    port=PORT)

cur = conn.cursor()

@app.get("/getDronesCnas/")
def dronescnas():
    cur.execute(f"SELECT * FROM dronescnas")
    data = cur.fetchall()
    result = []
    for index, subdata in enumerate(data):
        name = subdata[0]
        country = subdata[1]
        range_ = subdata[2] * 1000
        params = subdata[3]
        
        result_subdict = {
            'id': index,
            'name': name,
            'country': country,
            'range_': range_
        }
        result_subdict.update(params)

        result.append(result_subdict)

    return result

@app.get('/getSpidersData/')
def spider():
    cur.execute("SELECT * FROM spiders")
    data = cur.fetchall()
    jsoned = []
    for index, subdata in enumerate(data):
        jsoned.append({
                'spider': subdata[0],
                'url': subdata[1],
                "data": subdata[2] 
            })
        
    return jsoned