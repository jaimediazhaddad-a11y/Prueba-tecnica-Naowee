from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np

app = FastAPI(title="Student Performance API")

# Modelo simulado
class FakeModel:
    def predict(self, X):
        return [1 if (row[1] < 55 or row[0] < 3) else 0 for row in X]

model = FakeModel()

# Esquema del estudiante
class Student(BaseModel):
    hours_studied: float
    previous_scores: float
    sleep_hours: float
    sample_question_papers_practiced: float
    extracurricular_activities: int

# CRUD simulado
db = {}

@app.post("/student/")
def create_student(student: Student):
    student_id = len(db) + 1
    db[student_id] = student.dict()
    return {"id": student_id, "data": db[student_id]}

@app.get("/student/{student_id}")
def read_student(student_id: int):
    return db.get(student_id, {"error": "not found"})

@app.put("/student/{student_id}")
def update_student(student_id: int, student: Student):
    if student_id not in db:
        return {"error": "not found"}
    db[student_id] = student.dict()
    return {"updated": db[student_id]}

@app.delete("/student/{student_id}")
def delete_student(student_id: int):
    if student_id not in db:
        return {"error": "not found"}
    del db[student_id]
    return {"msg": "deleted"}

# ----------------------------
# Endpoint de predicción
# ----------------------------
@app.post("/predict/")
def predict(student: Student):
    X = np.array([[student.hours_studied,
                   student.previous_scores,
                   student.sleep_hours,
                   student.sample_question_papers_practiced,
                   student.extracurricular_activities]])

    pred = model.predict(X)[0]

    return {
        "risk": int(pred),
        "meaning": "Bajo desempeño" if pred == 1 else "Rendimiento normal"
    }
