from pydantic import BaseModel
from typing import Optional
from datetime import date

class PatientBase(BaseModel):
    name: str
    dob: Optional[date]
    gender: Optional[str]
    phone: Optional[str]
    email: Optional[str]

class PatientCreate(PatientBase):
    pass

class Patient(PatientBase):
    patient_id: int

    class Config:
        orm_mode = True

class DoctorBase(BaseModel):
    name: str
    email: str
    phone: Optional[str]
    department_id: Optional[int]

class DoctorCreate(DoctorBase): pass

class Doctor(DoctorBase):
    doctor_id: int
    class Config: orm_mode = True

class AppointmentBase(BaseModel):
    patient_id: int
    doctor_id: int
    appointment_date: datetime
    status: Optional[str] = "Scheduled"

class AppointmentCreate(AppointmentBase): pass

class Appointment(AppointmentBase):
    appointment_id: int
    class Config: orm_mode = True
