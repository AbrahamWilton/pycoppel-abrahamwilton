# pycoppel-abrahamwilton
Examen técnico Backend - Coppel python

# ejecutar para levantar servicio:
uvicorn webApi:app --reload

# buscar show por query
http://127.0.0.1:8000/search_shows?search_query=resort

# buscar show por id especifico
http://127.0.0.1:8000/search_show_by_id/228

# postear comentario y calificacion en show, verbo: POST, objeto en body
http://127.0.0.1:8000/show_review
{
  "show_id": 228,
  "comment": "Una excelente serie, coment 2",
  "rating": 5
}