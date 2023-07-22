from pydantic import BaseModel, Field
from typing import Optional
from  fastapi  import HTTPException, Request
from fastapi.security import HTTPBearer
from app.jwt_manager import validate_token

class Movies(BaseModel):
    id: Optional[int] = None
    title: str = Field(default = "alguna pelicula", min_length = 5, max_length = 15)
    overview: str = Field(default = "alguna descripcion", min_length = 15, max_length = 100)
    year: int = Field(default = 2022, le = 2022)
    rating: float = Field(default = 0.0, le = 5.0, ge = 0.0 )
    category: str = Field(default = "otras")

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "title": "mi pelicula",
				"overview": "descripcion de mi pelicula",
				"year": 2022,
				"rating": 9.8,
				"category": "ciencia ficcion"
            }
        }

class User(BaseModel):
    id: Optional[int] = None
    name: str
    role: str
    email: str
    password: str
    start_date: str

class Member(BaseModel):
    id: Optional[int] = None
    name: str
    role: str
    email: str
    start_date: str
      

# Endpoint de autention en aplicacion
class JWTBearer(HTTPBearer):
	async def __call__(self, request: Request):
		auth = await super().__call__(request) #  se llama a la funcion de la clase heredada
		data = validate_token(auth.credentials) # se valida el token

		if data['email'] != "string":
			raise HTTPException(status_code=403, detail="Credenciales son invalidas")