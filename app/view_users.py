from fastapi import FastAPI, Body, Path, Query, Depends
from fastapi.responses import JSONResponse
from app.schemes import Movies, User, JWTBearer
from typing import List
from app.jwt_manager import create_token
from os import getenv
from app.managers.db_manager import DbManager
from fastapi import APIRouter
from app.managers.file_manager import FileManager
from app.managers.db_manager import DbManager


users_view = APIRouter()




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
# MAIN END POINT
# GET METHOD
# -----------
# @app.get('/', tags=['home'])  # ruta de la API
# def message():
#     with open('app/home.html', 'r') as file:
#         response = file.read()
#     return HTMLResponse(response)  # mensaje

# ----------------------------------------
# END POINT WITH AUTHORIZATION
# RESPONSE A LIST OF MOVIES OBJECT/CLASS
# GET METHOD
# -----------

@users_view.get('/users', tags=['Users'], response_model= List[User],  dependencies=[Depends(JWTBearer())]) 
def get_movies():
    # file_path = "app/db.json"
    # records = FileManager.read_json_file(path = file_path)
    # print(records)

    # return JSONResponse(content=records, status_code=200)
    
    conn = DbManager.connection()
    session = Session(engine)
    return JSONResponse(content=records, status_code=200)


# ----------------------------------------
# END POINT WITH PARAMETER
# RESPONSE A MOVIES OBJECT
# GET METHOD
# -----------
@users_view.get('/users/{id}', tags=['movies'], response_model=Movies)
def get_movies(id: int = Path(default = 1, ge = 1, le = 2000)):
    for item in movies:
        if item['id'] == id:
            # return item
            return JSONResponse(content=item)
    # return []
    return JSONResponse(content=[], status_code=404)

# ----------------------------------------
# END POINT WITH QUERY PARAMETER
# GET METHOD
# -----------
@users_view.get('/users/', tags=['movies'])
def get_movies(category: str = Query(default = 1, min_length = 5, max_length= 15)):
    for item in movies:
        if item['category'] == category:
            return item
    return []


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
