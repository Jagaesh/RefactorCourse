import json
import datetime

PATIENTS_DB = {}

def process_patient_data(data):
    try:
        data = json.loads(data)
    except Exception as e:
        print("Invalid JSON:", e)
        return

    patient_id = data.get("id")
    if not patient_id:
        print("Missing patient ID")
        return

    if patient_id not in PATIENTS_DB:
        PATIENTS_DB[patient_id] = {
            "id": patient_id,
            "name": data.get("name"),
            "birthdate": data.get("birthdate"),
            "visits": [],
            "score": 0
        }

    visit = {
        "date": datetime.datetime.now().isoformat(),
        "reason": data.get("reason"),
        "symptoms": data.get("symptoms", []),
        "temperature": data.get("temperature")
    }

    PATIENTS_DB[patient_id]["visits"].append(visit)

    # crude scoring logic
    score = 0
    if visit["temperature"] and visit["temperature"] > 39:
        score += 2
    if "chest pain" in visit["symptoms"]:
        score += 3
    if "headache" in visit["symptoms"]:
        score += 1
    if data.get("has_insurance") is False:
        score -= 1

    PATIENTS_DB[patient_id]["score"] += score

    print(f"Updated patient {patient_id} with score {score}")
