# ejecutar para levantar servicio: uvicorn webApi:app --reload
from fastapi import FastAPI, Query
import requests

app = FastAPI()
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