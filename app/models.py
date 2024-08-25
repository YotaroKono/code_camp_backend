from sqlalchemy import Column, ForeignKey, Integer, String, JSON, Float
from sqlalchemy.orm import relationship

from app.database import Base


class Diagnosis(Base):
    __tablename__ = "diagnosis"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    questions  = Column(JSON)

    result = relationship("Result", back_populates="diagnosis")
    # result = relationship(
    #     "Result",
    #     primaryjoin="Diagnosis.id==Result.diagnosis_id",
    #     back_populates="diagnosis",
    #     uselist=True
    # )


class Result(Base):
    __tablename__ = "result"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    category_id = Column(Integer)
    diagnosis_id = Column(Integer, ForeignKey("diagnosis.id"))
    score = Column(Float)

    diagnosis = relationship("Diagnosis", back_populates="result")
    # diagnosis = relationship(
    #     Diagnosis,
    #     primaryjoin=("Result.diagnosis_id==Diagnosis.id"),
    # )