from fastapi import Depends
from sqlalchemy.orm import Session
from ..config import get_db

class DBSessionContext(object):
    def __init__(self): 
        self.db = list(get_db())[0]


class AppRepo(DBSessionContext):
    pass


class AppCRUD(DBSessionContext):
    pass
