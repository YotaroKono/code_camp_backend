import random
from typing import Dict
from app.models import Diagnosis as DiagnosisModel, Result
from app.models import Result as ResultModel
from app.music_type_config import MUSIC_CATEGORY_TYPES, SCORING_MATRIX
from app.schemas import DiagnosisCreate, DiagnosisResult, Questions
from sqlalchemy.orm import Session

def create_diagnosis(db: Session, diagnosis: DiagnosisCreate) -> DiagnosisResult:
    db_diagnosis = DiagnosisModel(questions=diagnosis.questions.dict())
    db.add(db_diagnosis)
    db.commit()

    # 音楽タイプを決定
    scores = determine_music_type(diagnosis.questions)
    category_id = max(scores, key=scores.get)
    score = max(scores.values())

    # 結果をデータベースに保存
    db_result = ResultModel(diagnosis_id=db_diagnosis.id, category_id=category_id, score=score)
    db.add(db_result)
    db.commit()

    # 結果を即座に返す
    return DiagnosisResult(
        id=db_diagnosis.id,
        questions=diagnosis.questions,
        category_id=category_id
    )


def determine_music_type(questions: Questions) -> Dict[int, float]:
    scores = {}
    for category_id in MUSIC_CATEGORY_TYPES.keys():
        scores[category_id] = 0

    for q, a in questions.dict().items():
        if q in SCORING_MATRIX:
            for category_id, score in SCORING_MATRIX[q][a].items():
                scores[category_id] += score

    # 同順位対策: 各ジャンルに0.1から0.7のランダムな値を加算
    for category_id in scores:
        scores[category_id] += round(random.uniform(0.1, 0.7), 1)

    return scores