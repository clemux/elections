from fastapi import FastAPI, Depends
from starlette.routing import Route, Mount
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from app.db import schemas, crud
from app.db.database import SessionLocal, Session

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/votes', response_model=list[schemas.Votes])
async def get_votes(code_dept: str, code_circ: str, db: Session = Depends(get_db)):
    votes = crud.get_votes(db, code_dept, code_circ)

    return votes
