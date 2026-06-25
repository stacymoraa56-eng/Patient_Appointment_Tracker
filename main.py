from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models, schemas, crud 
from database import get_db, engine 

models.Base.metadata.create_all(bind=engine)

app =FastAPI(title ="Patient Appointment Tracker", 
             description= "Track patient appointment schedules with FastAPI ", 
             version="1.0.0"
             )


#CREATE 
# GET PATIENT BY PHONE NUMBER 
@app.post("/patients/",
          response_model=schemas.PatientResponse)
def create_patient(
        patient: schemas.PatientCreate,
        db: Session = Depends(get_db)):
    # Checking for duplicates before creating a new patient record 
    existing_patient = crud.get_patient_by_phone(db,patient.phone)
    if existing_patient:
        raise HTTPException(
            status_code=400,
            detail="Phone number already registered")
    return crud.create_patient(db, patient)

#READ  ALL
@app.get("/patients/", response_model= List[schemas.PatientResponse])
def get_patients(db:Session = Depends(get_db)):
    return crud.get_patients(db)

# READ ONE 
@app.get("/patients/{patient_id}", response_model= schemas.PatientResponse)
def get_patient(patient_id:int, db:Session= Depends(get_db)):
    patient =crud.get_patient(db, patient_id )
    if not patient: 
        raise HTTPException(404, "Patient not found")
    return patient 
    
# UPDATE ONE FEATURE in a patient's record 
@app.put("/patients/{patient_id}", 
         response_model= schemas.PatientResponse)
def update_patient(patient_id: int, 
                   data:schemas.PatientUpdate,
                   db:Session = Depends(get_db)):
    updated_patient = crud.update_patient(
        db, patient_id, data)
    if not updated_patient:
        raise HTTPException(404, "Patient not found")
    # Checking for duplicates before updating a patient's record  
    if updated_patient == "duplicate_phone":
        raise HTTPException(
        status_code=400,
        detail="Phone number already registered")
    return updated_patient
    


# GET PATIENTSby DOCTOR'S NAME 
@app.get("/patients/doctor/{doctor_name}", response_model=list[schemas.PatientResponse])
def get_patients_by_doctor(doctor_name: str, db: Session = Depends(get_db)):
    return crud.get_patients_by_doctor(db, doctor_name)

# DELETE ONE patient's record
@app.delete("/patients/{patient_id}")
def delete_patient(patient_id:int, db:Session = Depends(get_db)):
    patient = crud.delete_patient(db,patient_id)
    if not patient:
        raise HTTPException(404, "Patient  not found")
    return {
    "message": "Appointment deleted successfully"
}

# READ patient records using PHone number
@app.get("/patients/phone/{phone}",
    response_model=schemas.PatientResponse
)
def get_patient_by_phone(
    phone: str,
    db: Session = Depends(get_db)):
    patient = crud.get_patient_by_phone(db, phone)

    if not patient:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    return patient


