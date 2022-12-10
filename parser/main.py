from telegram import *
from news import *
import requests

requests.post('http://127.0.0.1:8000/main/addNews/', data={'news':'awwaw', 'orgs':'org', 'locs':'loc'})