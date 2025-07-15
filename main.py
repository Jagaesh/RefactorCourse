from services import process_patient
# from services.patient_service import PatientService
import sys
import json


def main():
    # Simulation d'entrée utilisateur (à remplacer par lecture fichier, API, etc.)
    patient_data = {
        "id": "123",
        "name": "Alice",
        "birthdate": "1980-01-01",
        "reason": "Checkup",
        "symptoms": ["chest pain"],
        "temperature": 39.5,
        "has_insurance": True
    }
    
    process_patient.process_patient_data(json.dumps(patient_data))
    # service = PatientService()
    # service.process_patient_data(patient_data)

if __name__ == '__main__':
    main()