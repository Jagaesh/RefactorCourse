import pytest
# from services.patient_service import ScoringService
from services import process_patient
from models.visit import Visit
from datetime import datetime

def test_score_high_temp_and_chest_pain():
    visit = Visit(
        date=datetime.now(),
        reason="Emergency",
        symptoms=["chest pain"],
        temperature=39.5
    )
    # score = ScoringService().compute_score(visit, has_insurance=True)
    score = process_patient.compute_patient_score(visit, has_insurance=True)
    assert score == 5  # 2 (temp) + 3 (chest pain)

def test_score_no_symptoms():
    visit = Visit(
        date=datetime.now(),
        reason="Routine",
        symptoms=[],
        temperature=36.6
    )
    # score = ScoringService().compute_score(visit, has_insurance=True)
    score = process_patient.compute_patient_score(visit, has_insurance=True)
    assert score == 0

def test_score_insurance_penalty():
    visit = Visit(
        date=datetime.now(),
        reason="Check",
        symptoms=["headache"],
        temperature=None
    )
    # score = ScoringService().compute_score(visit, has_insurance=False)
    score = process_patient.compute_patient_score(visit, has_insurance=False)
    assert score == 0  # 1 - 

def test_score_chest_pain_and_fever():
    visit = Visit(
        date=datetime.now().isoformat(),
        reason="Check",
        symptoms=["chest pain", "headache"],
        temperature=39.6
    )
    # score = ScoringService().compute_score(visit, has_insurance=True)
    score = process_patient.compute_patient_score(visit, has_insurance=True)
    assert score == 6  # 2 (temp) + 3 (chest pain) + 1 (headache)

def test_score_without_insurance():
    visit = Visit(
        date=datetime.now().isoformat(),
        reason="Check",
        symptoms=["headache"],
        temperature=37.0
    )
    # score = ScoringService().compute_score(visit, has_insurance=False)
    score = process_patient.compute_patient_score(visit, has_insurance=False)
    assert score == 0  # 1 - 1
