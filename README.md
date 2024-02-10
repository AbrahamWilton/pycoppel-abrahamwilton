# pycoppel-abrahamwilton
Examen técnico Backend - Coppel python

# Instalar las dependencias correspondientes si es necesario
--requests, uvicorn, fastapi, etc

# ejecutar el comando para levantar el servicio:
uvicorn webApi:app --reload

# request para probar el servicio (postman) se incluye la coleccion en  postman en el repositorio
buscar show por query -GET
http://127.0.0.1:8000/search_shows?search_query=resort

buscar show por id especifico -GET
http://127.0.0.1:8000/search_show_by_id/228

postear comentario y calificacion en show -POST
http://127.0.0.1:8000/show_review

y objeto en body,  tipo raw, formato JSON
{
  "show_id": 228,
  "comment": "Una excelente serie, coment 2",
  "rating": 5
}