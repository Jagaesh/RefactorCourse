import json
from datetime import datetime
from models.patient import Patient
from models.visit import Visit

# Simulation d'une base de données en mémoire
PATIENTS_DB = {}

class ScoringService:
    def compute_score(self, visit: Visit, has_insurance: bool) -> int:
        score = 0
        if visit.temperature and visit.temperature > 39:
            score += 2
        if "chest pain" in visit.symptoms:
            score += 3
        if "headache" in visit.symptoms:
            score += 1
        if not has_insurance:
            score -= 1
        return score

class PatientService:
    def __init__(self):
        self.scorer = ScoringService()

    def process_patient_data(self, data: str):
        try:
            parsed = json.loads(data)
        except json.JSONDecodeError as e:
            print("Invalid JSON:", e)
            return

        patient_id = parsed.get("id")
        if not patient_id:
            print("Missing patient ID")
            return

        if patient_id not in PATIENTS_DB:
            PATIENTS_DB[patient_id] = Patient(
                id=patient_id,
                name=parsed.get("name"),
                birthdate=parsed.get("birthdate")
            )

        visit = Visit(
            date=datetime.now(),
            reason=parsed.get("reason"),
            symptoms=parsed.get("symptoms", []),
            temperature=parsed.get("temperature")
        )

        patient = PATIENTS_DB[patient_id]
        patient.visits.append(visit)

        score = self.scorer.compute_score(visit, parsed.get("has_insurance", True))
        patient.score += score

        print(f"Updated patient {patient.id} with score {score}")