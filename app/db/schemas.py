from pydantic import BaseModel


class VotesBase(BaseModel):
    code_dept: str
    code_circ: str
    candidate: str
    percentage: float


class Votes(VotesBase):
    class Config:
        orm_mode = True
