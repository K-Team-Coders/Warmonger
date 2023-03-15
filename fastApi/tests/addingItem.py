import requests
import datetime


requests.post("http://127.0.0.1:8000/addNew/", json={
    "id" : 1,
    "text" : "Kajrat",
    "source": "ukrscaner",
    "datetime": "2023-03-01T14:28:01"
})