from sqlalchemy import Column, Integer, String, Date, Enum, ForeignKey, DateTime, Text, DECIMAL
from sqlalchemy.orm import relationship
from app.database import Base

class Department(Base):
    __tablename__ = "departments"
    department_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    doctors = relationship("Doctor", back_populates="department")

class Doctor(Base):
    __tablename__ = "doctors"
    doctor_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(15))
    department_id = Column(Integer, ForeignKey("departments.department_id"))
    department = relationship("Department", back_populates="doctors")

class Patient(Base):
    __tablename__ = "patients"
    patient_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    dob = Column(Date)
    gender = Column(Enum("Male", "Female", "Other"))
    phone = Column(String(15), unique=True)
    email = Column(String(100), unique=True)
