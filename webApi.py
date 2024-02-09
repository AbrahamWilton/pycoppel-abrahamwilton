# ejecutar para levantar servicio: uvicorn webApi:app --reload
from fastapi import FastAPI, HTTPException, Query, Path
import requests
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from show import Show

app = FastAPI()


# Configura la conexión a MongoDB
uri = "mongodb+srv://abrahamwilton:YZ8e9xNuwQbCw7Q9@cluster0.0e4duv5.mongodb.net/?retryWrites=true&w=majority"
mongo_client = MongoClient(uri, server_api=ServerApi('1'))
db = mongo_client["shows_db"]
collection = db["shows_colletion"]

servicio_url = 'https://api.tvmaze.com/'

@app.get('/search_shows')
def search_shows(search_query: str = Query(..., description="A-Endpoint search")):
    
    path = 'search/shows'
    try:
        
        response = requests.get(servicio_url + path, params={'q': search_query})
        if response.status_code == 200:
            
            data = response.json()
            transformed_data = {
                "id": data[0]["show"]["id"],
                "name": data[0]["show"]["name"],
                "channel": data[0]["show"]["network"]["name"] if data[0]["show"]["network"] else data[0]["show"]["webChannel"],
                "summary": data[0]["show"]["summary"],
                "genres": data[0]["show"]["genres"]
            }

            return transformed_data
        else:
            
            return {'error': 'No se pudo consumir el servicio'}, response.status_code

    except requests.exceptions.RequestException as e:
        
        return {'error': f'Error de solicitud: {str(e)}'}

def get_data_from_cache_or_db(item_id: int, use_cache: bool):
    if use_cache:
        # Intenta obtener los datos directamente desde MongoDB
        data_from_db = collection.find_one({"_id": item_id})
        if data_from_db:
            #print(data_from_db)
            return data_from_db

@app.get('/search_show_by_id/{id}')
def search_shows_by_id(id: int = Path(..., description="B-Endpoint show"), use_cache: bool = True):

    path = f'shows/{id}'
    show_data = get_data_from_cache_or_db(id, use_cache)
    if not show_data:
        try:
            print("datos NO encontrados en cache, solicitando de tv maze")   
            response = requests.get(servicio_url + path)
            response.raise_for_status()
            data = response.json()

            print("guardando en cache mongo")
            collection.update_one({"_id": id}, {"$set": data}, upsert=True)

            show_instance = Show(data)
            return show_instance

        except requests.exceptions.RequestException as e:
            return {'error': f'Error de solicitud: {str(e)}'}, 500

        except HTTPException as e:
            # en caso de erroes en la solicitud
            if e.status_code == 404:
                return {'error': 'Item not found'}, 404
    else:
        print("datos encontrados en cache")            
        return show_data