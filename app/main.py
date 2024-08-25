from http.client import HTTPException
from app import cruds
from app.database import ENGINE, Base, get_db
from app.models import Diagnosis, Result
from app.schemas import DiagnosisCreate, DiagnosisResult
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session


app = FastAPI()

@app.on_event("startup")
def startup():
    Base.metadata.drop_all(bind=ENGINE)
    Base.metadata.create_all(bind=ENGINE)

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.post("/diagnosis/create", response_model=DiagnosisResult)
def diagnosis_create(diagnosis: DiagnosisCreate, db: Session = Depends(get_db)):
    return cruds.create_diagnosis(db=db, diagnosis=diagnosis)

# @app.get('/diagnosis/{result_id}', response_model=Result)
# def read_result(result_id: int, db: Session = Depends(get_db)):
#     db_result = cruds.get_result(db, result_id=result_id)
#     if not db_result:
#         raise HTTPException(status_code=404, detail='Todo not found')
#     return db_result