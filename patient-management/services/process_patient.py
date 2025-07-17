import json
import datetime
import sys
from models.patient import Patient
from models.visit import Visit

PATIENTS_DB = {}

def load_json(data):
    try:
        return json.loads(data)
    except ValueError as err:
        print(f"Error parsing data: {err}")
        sys.exit(1)

def register_patient(patient):
    PATIENTS_DB[patient.id] = patient

def get_visit(data):
    return Visit(
        date=datetime.datetime.now().isoformat(),
        reason=data.get("reason"),
        symptoms=data.get("symptoms", []),
        temperature=data.get("temperature"),
    )

def get_or_register_patient(data):
    patient_id = data.get("id")
    if patient_id is None:
        print("Missing patient ID")
        return

    if patient_id not in PATIENTS_DB:
        patient = get_patient_from_data(data)
        PATIENTS_DB[patient.id] = patient
    else:
        patient = PATIENTS_DB[patient_id]
    return patient

def get_patient_from_data(data):
    return Patient(
        id=data.get("id"),
        name=data.get("name"),
        birthdate=data.get("birthdate"),
        has_insurance=data.get("has_insurance"),
        visits=[],
        score=0
    )

def update_patient(patient, visit):
    score = compute_patient_score(visit, patient.has_insurance)
    add_visit_to_patient(patient, visit)
    add_score_to_patient(patient, score)

def compute_patient_score(visit, has_insurance):
    score = 0
    if visit.temperature and visit.temperature > 39:
        score += 2
    if "chest pain" in visit.symptoms:
        score += 3
    if "headache" in visit.symptoms:
        score += 1
    if has_insurance is False:
        score -= 1
    return score

def add_visit_to_patient(patient, visit):
    patient.visits.append(visit)

def add_score_to_patient(patient, score):
    patient.score += score

def process_patient_data(data):
    data = load_json(data)

    patient = get_or_register_patient(data)
    visit = get_visit(data)

    update_patient(patient, visit)

    print(f"Updated patient {patient.id} with score {patient.score}")
