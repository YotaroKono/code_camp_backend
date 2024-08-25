from enum import Enum
from pydantic import BaseModel

class Answer(str, Enum):
    A = "A"
    B = "B"
    C = "C"
    D = "D"

class Questions(BaseModel):
    q_1: Answer
    q_2: Answer
    q_3: Answer
    q_4: Answer
    q_5: Answer

class DiagnosisCreate(BaseModel):
    questions: Questions

class Diagnosis(BaseModel):
    id: int
    questions: Questions

class DiagnosisResult(BaseModel):
    id: int
    questions: Questions
    category_id: int
