from fastapi import FastAPI, Body, Path, Query, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from app.schemes import Movies, User, JWTBearer
from typing import List
from app.jwt_manager import create_token
from os import getenv
from app.managers.db_manager import DbManager
from app.view_users import users_view

app = FastAPI()  # instanciacion
app.title = "Mi primera aplicacion con FastAPI"
app.version = "1.0.0"
app.include_router(users_view)

movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        "year": "2009",
                "rating": 7.8,
                "category": "Acción"
    },
	{
		"id": 2,
		"title": "Avatar 2, the way water",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
		"year": "2009",
		"rating": 7.8,
		"category": "Acción"
	}
]


# ----------------------------------------
# LOGIN END POINT
# POST METHOD
# -----------
@app.post('/login', tags=['auth'])
def login(user: User):
    if user.email == 'string' and user.password == 'string':
        token: str = create_token(user.dict())
        return JSONResponse(content = token, status_code = 200)

# ----------------------------------------
# MAIN END POINT
# GET METHOD
# -----------
@app.get('/', tags=['home'])  # ruta de la API
def message():
    with open('app/sources/templates/home.html', 'r') as file:
        response = file.read()
    return HTMLResponse(response)  # mensaje

# ----------------------------------------
# END POINT WITH AUTHORIZATION
# RESPONSE A LIST OF MOVIES OBJECT/CLASS
# GET METHOD
# -----------
# @app.get('/movies', tags=['movies'],
#         response_model= List[Movies],  # indica que retorna una lista de objetos (json)
#         dependencies=[Depends(JWTBearer())]) # indica que solo se peude acceder a la vista una vez autenticado
# def get_movies():
#     # return movies
#     return JSONResponse(content=movies, status_code=200)


# ----------------------------------------
# END POINT WITH PARAMETER
# RESPONSE A MOVIES OBJECT
# GET METHOD
# -----------
# @app.get('/movies/{id}', tags=['movies'], response_model=Movies)
# def get_movies(id: int = Path(default = 1, ge = 1, le = 2000)):
#     for item in movies:
#         if item['id'] == id:
#             # return item
#             return JSONResponse(content=item)
#     # return []
#     return JSONResponse(content=[], status_code=404)

# ----------------------------------------
# END POINT WITH QUERY PARAMETER
# GET METHOD
# -----------
# @app.get('/movies/', tags=['movies'])
# def get_movies(category: str = Query(default = 1, min_length = 5, max_length= 15)):
#     '''
#     '''
#     for item in movies:
#         if item['category'] == category:
#             return item
#     return []


# @app.post('/movies', tags=['movies'])
# # La funcion Body() permite enviar los datos como un payload o json en vez de campos query independientes
# def create_movie(id: int = Body(), title: str = Body(), overview: str = Body(), year: int = Body(), rating: float = Body(), category: str = Body()):
#     movies.append({"id": id,
#                    "title": title,
#                    "overview": overview,
#                    "year": year,
#                    "rating": rating,
#                    "category": category})

#     return movies

# @app.put('/movies', tags=['movies'])
# def update_movie(id: int,
# 	title: str = Body(), 
# 	overview: str = Body(), 
# 	year: int = Body(), 
# 	rating: float = Body(), 
# 	category: str = Body()):

# 	for item in movies:
# 		if item['id'] == id:
# 			item["title"] =  title
# 			item["overview"] = overview
# 			item["year"] = year
# 			item["rating"] = rating
# 			item["category"] = category
# 			return movies

# ----------------------------------------
# DELETE METHOD
# -----------
# @app.delete('/movies', tags=['movies'])
# def delete_movie(id: int):
# 	for item in movies:
# 		if item['id'] == id:
# 			movies.remove(item)
# 			return movies

# ----------------------------------------
# POST METHOD
# -----------
# Usando Esquemas para la manipulacion de datos
# @app.post('/movies', tags=['movies'])
# # La funcion Body() permite enviar los datos como un payload o json en vez de campos query independientes
# def create_movie(movie: Movies):
#     movies.append(movie)
#     return movies

# ----------------------------------------
# PUT METHOD
# ----------
# @app.put('/movies', tags=['movies'])
# def update_movie(id: int, movie: Movies):
# 	for item in movies:
# 		if item['id'] == id:
# 			item["title"] =  movie.title
# 			item["overview"] = movie.overview
# 			item["year"] = movie.year
# 			item["rating"] = movie.rating
# 			item["category"] = movie.category
# 			return movies
