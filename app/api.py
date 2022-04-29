from fastapi import FastAPI, Depends

from app.db import schemas, crud
from app.db.database import SessionLocal, Session

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/results', response_model=schemas.CircResult)
async def get_results(code_dept: str, code_circ: str, db: Session = Depends(get_db)):
    votes = crud.get_circ_results(db, code_dept, code_circ)

    return votes
