from fastapi import FastAPI, Body, Path, Query, Depends
from fastapi.responses import JSONResponse
from app.schemes import Movies, User, JWTBearer, Members
from typing import List
from app.jwt_manager import create_token
from os import getenv
from app.managers.db_manager import DbManager
from fastapi import APIRouter
from app.managers.file_manager import FileManager
from app.managers.db_manager import DbManager
from sqlalchemy.exc import SQLAlchemyError


members_view = APIRouter()
SessionLocal, Base = DbManager.connection()

@members_view.post('/members', tags=['members'], response_model = List[Members ]) 
def get_members(members: Members):
    try:
        db = SessionLocal()
        db.add(members)
        db.commit()
        db.refresh(members)
        return members
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    finally:
        db.close()

@members_view.get('/members/{name}', tags=['members by name'])
def get_members(name: str):
    db = SessionLocal()
    item = db.query(Members).filter(Members.id == name).first()
    db.close()
    return item

@members_view.get('/members/', tags=['members'])
def get_members():
    db = SessionLocal()
    item = db.query(Members).all()
    db.close()
    return item
