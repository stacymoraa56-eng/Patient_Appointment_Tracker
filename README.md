# Patient Appointment Tracker API

## Overview

The Patient Appointment Tracker API is a RESTful web service built using FastAPI, SQLAlchemy, and Pydantic. It allows a clinic to manage patient appointment records efficiently through standard CRUD (Create, Read, Update, Delete) operations.

The project stores appointment information in a SQLite database and provides endpoints for creating, retrieving, updating, and deleting patient records.

---

## Technologies Used

* Python
* FastAPI
* SQLAlchemy
* Pydantic
* SQLite
* Uvicorn

---

## Project Structure

```
appointment_tracker/
│
├── database.py
├── models.py
├── schemas.py
├── crud.py
├── main.py
├── appointments.db
└── README.md
```

---

## Features

### Core CRUD Operations

* Create a patient appointment
* Retrieve all patient appointments
* Retrieve a patient appointment by ID
* Update appointment information
* Delete an appointment

### Bonus Features

* Retrieve appointments by doctor name
* Prevent duplicate patient registration using phone number validation
* Prevent duplicate patient updates using phone number validation 

---

## API Endpoints

### Create Appointment

**POST** `/patients/`

Creates a new patient appointment.

---

### Get All Appointments

**GET** `/patients/`

Returns all patient appointments.

---

### Get Appointment by ID

**GET** `/patients/{patient_id}`

Returns a single patient appointment by ID.

---

### Update Appointment

**PUT** `/patients/{patient_id}`

Updates one or more appointment fields.
```json
{
  "status": "completed"
}
```
This only updates the status section of the patient records 

---

### Delete Appointment

**DELETE** `/patients/{patient_id}`

Deletes an appointment and returns a success message.

---

### Get Appointments by Doctor

**GET** `/patients/doctor/{doctor_name}`

Returns all appointments assigned to a specific doctor.

---

## Validation

The API uses Pydantic validation to ensure data integrity.

Examples:

* Invalid data types return a 422 Validation Error.
* Duplicate phone numbers return a 400 Bad Request.

---

## Running the Project

### Install Dependencies

```bash
pip install "fastapi[standard]" 
```

```bash 
pip install uvicorn sqlalchemy pydantic
```
### Start the Server

```bash
uvicorn main:app --reload
```

### Access API Documentation

FastAPI automatically generates interactive documentation:

* Swagger UI: http://127.0.0.1:8000/docs


---

## Author

Stacy Moraa

Built to demonstrate  the integration of FastAPI, SQLAlchemy, Pydantic, and SQLite.
