from fastapi import FastAPI
from app.routers import patients, doctors

app = FastAPI()

app.include_router(patients.router, prefix="/patients", tags=["Patients"])
app.include_router(doctors.router, prefix="/doctors", tags=["Doctors"])
