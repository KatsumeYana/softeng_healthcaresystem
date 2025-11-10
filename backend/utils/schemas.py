"""
Pydantic schemas for request/response validation
These schemas define the structure and validation rules for API data
"""

from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import date, datetime
from models.user import UserRole


# ===================================================================
# TOKEN SCHEMAS
# ===================================================================

class Token(BaseModel):
    """Schema for JWT token response"""
    access_token: str
    token_type: str


class TokenData(BaseModel):
    """Schema for data stored in JWT token"""
    username: Optional[str] = None
    role: Optional[str] = None


# ===================================================================
# USER SCHEMAS
# ===================================================================

class UserBase(BaseModel):
    """Base user schema with common fields"""
    username: str = Field(..., min_length=3, max_length=50)
    full_name: str = Field(..., min_length=1, max_length=100)
    role: UserRole


class UserCreate(UserBase):
    """Schema for creating a new user"""
    password: str = Field(..., min_length=8, max_length=100)


class UserOut(UserBase):
    """Schema for user data in responses"""
    id: int
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True  # Replaces orm_mode in Pydantic v2


# ===================================================================
# PATIENT SCHEMAS
# ===================================================================

class PatientBase(BaseModel):
    """Base patient schema with all form fields"""
    # Personal Details
    full_name: str = Field(..., min_length=1, max_length=100, description="Patient's full name")
    age: int = Field(..., gt=0, le=150, description="Patient's age in years")
    gender: str = Field(..., max_length=10, description="Patient's gender")
    date_of_birth: date = Field(..., description="Patient's date of birth")
    phone_number: str = Field(..., min_length=7, max_length=20, description="Patient's phone number")
    address: Optional[str] = Field(None, max_length=255, description="Patient's address")
    
    # Emergency Contact
    emergency_contact: Optional[str] = Field(None, max_length=100, description="Emergency contact name")
    relationship: Optional[str] = Field(None, max_length=50, description="Relationship to patient")
    emergency_phone: Optional[str] = Field(None, max_length=20, description="Emergency contact phone")
    
    # Physical Details
    height_cm: Optional[int] = Field(None, gt=0, le=300, description="Height in centimeters")
    weight_kg: Optional[str] = Field(None, description="Weight in kilograms")
    
    # Screening Details
    blood_pressure: Optional[str] = Field(None, max_length=20, description="Blood pressure reading")
    temperature: Optional[str] = Field(None, max_length=10, description="Temperature")
    heart_rate: Optional[int] = Field(None, gt=0, le=300, description="Heart rate in BPM")
    
    # Medical Information
    allergies: Optional[str] = Field(None, max_length=255, description="Known allergies")
    symptoms: Optional[str] = Field(None, max_length=500, description="Current symptoms")
    diagnosis: Optional[str] = Field(None, max_length=500, description="Medical diagnosis")
    medical_history: Optional[str] = Field(None, max_length=1000, description="Medical history")

    @validator('date_of_birth')
    def validate_date_of_birth(cls, v):
        """Ensure date of birth is not in the future"""
        if v > date.today():
            raise ValueError('Date of birth cannot be in the future')
        return v

    @validator('gender')
    def validate_gender(cls, v):
        """Validate gender field"""
        allowed_genders = ['Male', 'Female', 'Other']
        if v not in allowed_genders:
            raise ValueError(f'Gender must be one of: {", ".join(allowed_genders)}')
        return v


class PatientCreate(PatientBase):
    """Schema for creating a new patient"""
    pass


class PatientOut(PatientBase):
    """Schema for patient data in responses"""
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# ===================================================================
# DRUG SCHEMAS
# ===================================================================

class DrugBase(BaseModel):
    """Base drug schema with all form fields"""
    drug_id: str = Field(..., min_length=1, max_length=20, description="Unique drug identifier")
    brand_name: str = Field(..., min_length=1, max_length=200, description="Brand name of the drug")
    generic_name: str = Field(..., min_length=1, max_length=200, description="Generic name of the drug")
    dosage_form: str = Field(..., max_length=50, description="Form of dosage (Tablet, Capsule, etc.)")
    strength: str = Field(..., max_length=100, description="Strength of the drug (e.g., 500 mg)")
    category: str = Field(..., max_length=100, description="Drug category (Analgesic, Antibiotic, etc.)")
    manufacturer: Optional[str] = Field(None, max_length=100, description="Manufacturer name")
    batch_number: Optional[str] = Field(None, max_length=50, description="Batch/Lot number")
    expiry_date: Optional[str] = Field(None, max_length=20, description="Expiration date")
    quantity_in_stock: int = Field(..., ge=0, description="Quantity in stock")
    unit_price: float = Field(..., gt=0, description="Cost per unit")
    description: Optional[str] = Field(None, description="Additional drug information")
    side_effects: Optional[str] = Field(None, description="Side effects")
    contraindications: Optional[str] = Field(None, description="Contraindications")
    storage_conditions: Optional[str] = Field(None, description="Storage requirements")
    prescription_required: Optional[bool] = Field(True, description="Whether prescription is required")
    is_active: Optional[bool] = Field(True, description="Whether drug is active")

    @validator('drug_id')
    def validate_drug_id(cls, v):
        """Ensure drug_id follows expected format"""
        if not v.strip():
            raise ValueError('Drug ID cannot be empty')
        return v.strip().upper()


class DrugCreate(DrugBase):
    """Schema for creating a new drug"""
    pass


class DrugUpdate(BaseModel):
    """Schema for updating drug information"""
    brand_name: Optional[str] = Field(None, max_length=200)
    generic_name: Optional[str] = Field(None, max_length=200)
    dosage_form: Optional[str] = Field(None, max_length=50)
    strength: Optional[str] = Field(None, max_length=100)
    category: Optional[str] = Field(None, max_length=100)
    manufacturer: Optional[str] = Field(None, max_length=100)
    batch_number: Optional[str] = Field(None, max_length=50)
    expiry_date: Optional[str] = Field(None, max_length=20)
    quantity_in_stock: Optional[int] = Field(None, ge=0)
    unit_price: Optional[float] = Field(None, gt=0)
    description: Optional[str] = None
    side_effects: Optional[str] = None
    contraindications: Optional[str] = None
    storage_conditions: Optional[str] = None
    prescription_required: Optional[bool] = None
    is_active: Optional[bool] = None


class DrugOut(DrugBase):
    """Schema for drug data in responses"""
    id: int
    is_active: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# ===================================================================
# SEARCH SCHEMAS
# ===================================================================

class SearchResponse(BaseModel):
    """Schema for search results"""
    results: list
    count: int
    search_type: str
