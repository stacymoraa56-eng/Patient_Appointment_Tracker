from sqlalchemy.orm import Session 
import models, schemas 

#CREATE NEW PATIENT RECORDS 
def create_patient(db:Session, patient:schemas.PatientCreate):
    db_patient = models.Patient(**patient.model_dump())
    db.add(db_patient)
    db.commit()
    db. refresh(db_patient)
    return db_patient 


#READ ONE patient's record
def get_patient(db:Session, patient_id:int):
    return db.query(models.Patient).filter(
        models.Patient.id==patient_id).first()

# READ ALL records 
def get_patients(db:Session):
    return db.query(models.Patient).all()

#UPDATE a record 
def update_patient(db:Session, patient_id:int,
                   data:schemas.PatientUpdate):

    patient = db.query(models.Patient).filter(
        models.Patient.id==patient_id
    ).first()

    if not patient:
        return None
    
    updates = data.model_dump(exclude_unset=True)
    
    # Checking for duplicates 
    if "phone" in updates: 
        existing_patient = db.query(models.Patient).filter(
            models.Patient.phone == updates["phone"],
            models.Patient.id != patient_id
        ).first()

        if existing_patient:
            return "duplicate_phone"

    

    for field, value in updates.items():
        setattr(patient, field, value)


    db.commit()
    db.refresh(patient)
        
        
    return patient


#DELETE ONEpatient's record 
def delete_patient(db:Session, patient_id:int):
    patient = db.query(models.Patient).filter(
        models.Patient.id == patient_id).first()
    if not patient: 
        return None
    
    db.delete(patient)
    db.commit()
    return patient 
 
# Get patients' schedule by DOCTOR's NAME 
def get_patients_by_doctor(db: Session, doctor_name: str):
    return db.query(models.Patient).filter(
        models.Patient.doctor == doctor_name).all()


# Get Patient by Phone Number 
def get_patient_by_phone(db: Session, phone: str):
    return db.query(models.Patient).filter(
        models.Patient.phone == phone).first()

