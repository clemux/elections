from sqlalchemy.orm import Session

from . import models
from .models import CircResult


def get_votes(db: Session, code_dept: str, code_circ: str) -> list[CircResult]:
    print(code_dept, code_circ)
    return db.query(models.CircResult).filter_by(
        code_circ=code_circ,
        code_dept=code_dept,
    ).all()