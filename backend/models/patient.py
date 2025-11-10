"""
Patient model for storing patient records
"""

from sqlalchemy import Column, Integer, String, Date, DateTime, Text
from sqlalchemy.sql import func
from config.database import Base


class Patient(Base):
    """
    Patient table for storing patient information
    Corresponds to the "Add New Patient" form
    """
    __tablename__ = "patients"

    # Primary Key
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    
    # Personal Details
    full_name = Column(String(200), nullable=False, index=True)
    age = Column(Integer, nullable=False)
    gender = Column(String(10), nullable=False)  # Male, Female, Other
    date_of_birth = Column(Date, nullable=False)
    phone_number = Column(String(20), nullable=True)
    address = Column(Text, nullable=True)
    
    # Emergency Contact
    emergency_contact = Column(String(100), nullable=True)
    relationship = Column(String(50), nullable=True)
    emergency_phone = Column(String(20), nullable=True)
    
    # Physical Details
    height_cm = Column(Integer, nullable=True)
    weight_kg = Column(String(10), nullable=True)  # Decimal as string for flexibility
    
    # Screening Details
    blood_pressure = Column(String(20), nullable=True)
    temperature = Column(String(10), nullable=True)  # e.g., "37.2°C"
    heart_rate = Column(Integer, nullable=True)  # BPM as integer
    
    # Medical Information
    allergies = Column(Text, nullable=True)
    symptoms = Column(Text, nullable=True)
    diagnosis = Column(Text, nullable=True)
    medical_history = Column(Text, nullable=True)
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    def __repr__(self):
        return f"<Patient(id={self.id}, name='{self.full_name}', age={self.age})>"
