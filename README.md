# 🏥 Clinic Booking System

A full-featured MySQL database project designed to manage the core operations of a medical clinic — including patient registration, doctor assignments, appointment scheduling, medical records management, and payment tracking.

---

## 📌 Project Overview

This project simulates a real-world **Clinic Booking System** using only **MySQL**. It models essential entities such as Patients, Doctors, Departments, Appointments, Medical Records, and Payments — with proper relationships and constraints to ensure data integrity.

---

## 📁 Features

- ✅ Patient and Doctor Registration  
- ✅ Department-to-Doctor Assignment (1:M)  
- ✅ Appointment Scheduling between Patients and Doctors (M:M)  
- ✅ Storing and Linking Medical Records to Appointments (1:1)  
- ✅ Payment Management and Linking to Appointments (1:M)

---

## 🧱 Database Entities

- `departments` — Clinic departments like Cardiology, Neurology, etc.  
- `doctors` — Doctors associated with departments  
- `patients` — Registered patients  
- `appointments` — Booking between doctors and patients  
- `medical_records` — Diagnosis and prescriptions per appointment  
- `payments` — Payment details for completed appointments  
