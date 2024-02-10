# pycoppel-abrahamwilton
Examen técnico Backend - Coppel python

# ejecutar para levantar servicio:
uvicorn webApi:app --reload

# buscar show por query
http://127.0.0.1:8000/search_shows?search_query=resort"

# buscar show por id especifico
http://127.0.0.1:8000/search_show_by_id/228

# postear comentario y calificacion en show
http://127.0.0.1:8000/show_review