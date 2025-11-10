"""
Patient management routes
Handles patient record operations (Major Form: Add New Patient)
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from config.database import get_db
from models.patient import Patient
from models.user import User, UserRole
from utils.schemas import PatientCreate, PatientOut
from utils.security import get_current_active_user, require_role

router = APIRouter(
    prefix="/patients",
    tags=["Patients"]
)


@router.post(
    "",
    response_model=PatientOut,
    status_code=status.HTTP_201_CREATED,
    summary="Add New Patient Form Endpoint"
)
async def create_patient(
    patient_data: PatientCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role([UserRole.ADMIN, UserRole.DOCTOR, UserRole.ASSISTANT_CASHIER]))
):
    """
    **MAJOR FORM 1: ADD NEW PATIENT FORM**
    
    Creates a new patient record in the system.
    
    **Form Controls (15+ fields):**
    1. Full Name (textbox) - required
    2. Age (number) - required
    3. Gender (dropdown/radio) - required
    4. Date of Birth (date) - required
    5. Phone Number (textbox) - required
    6. Address (textarea) - optional
    7. Emergency Contact Name (textbox) - optional
    8. Emergency Contact Relationship (textbox) - optional
    9. Emergency Contact Phone (textbox) - optional
    10. Height in cm (number) - optional
    11. Weight in kg (number) - optional
    12. Blood Pressure (textbox) - optional
    13. Temperature (textbox) - optional
    14. Heart Rate (textbox) - optional
    15. Allergies (textbox) - optional
    16. Symptoms (textarea) - optional
    17. Diagnosis (textarea) - optional
    18. Medical History (textarea) - optional
    
    **Validation:**
    - All required fields must be provided
    - Age must be positive and realistic (1-150)
    - Date of birth cannot be in the future
    - Phone numbers must be valid format
    - Height and weight must be positive if provided
    - Gender must be Male, Female, or Other
    
    **Authorization:**
    - Requires authentication (JWT token)
    - Allowed roles: Admin, Doctor, Assistant/Cashier
    
    **Process:**
    1. Validate all form data using Pydantic schema
    2. Check user authorization
    3. Create new patient record in database
    4. Log activity (in production)
    5. Return created patient data with assigned ID
    
    **Returns:**
    - Complete patient record with database ID and timestamps
    
    **Errors:**
    - 401 Unauthorized: Missing or invalid token
    - 403 Forbidden: User role not authorized
    - 422 Unprocessable Entity: Validation errors
    """
    # Create new patient instance
    new_patient = Patient(**patient_data.model_dump())
    
    # Add to database
    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)
    
    # In production, log this activity to UserActivityLog
    # log_activity(current_user.id, "CREATE_PATIENT", new_patient.id)
    
    return new_patient


@router.get(
    "",
    response_model=List[PatientOut],
    summary="Get All Patients"
)
async def get_all_patients(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Retrieve all patient records with pagination.
    
    **Query Parameters:**
    - skip: Number of records to skip (default: 0)
    - limit: Maximum number of records to return (default: 100)
    
    **Authorization:**
    - Requires authentication
    - All authenticated users can view patient list
    """
    patients = db.query(Patient).offset(skip).limit(limit).all()
    return patients


@router.get(
    "/{patient_id}",
    response_model=PatientOut,
    summary="Get Patient by ID"
)
async def get_patient(
    patient_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Retrieve a specific patient record by ID.
    
    **Path Parameters:**
    - patient_id: The unique identifier of the patient
    
    **Authorization:**
    - Requires authentication
    
    **Errors:**
    - 404 Not Found: Patient with specified ID does not exist
    """
    patient = db.query(Patient).filter(Patient.id == patient_id).first()
    
    if not patient:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Patient with ID {patient_id} not found"
        )
    
    return patient


@router.put(
    "/{patient_id}",
    response_model=PatientOut,
    summary="Update Patient Record"
)
async def update_patient(
    patient_id: int,
    patient_data: PatientCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role([UserRole.ADMIN, UserRole.DOCTOR]))
):
    """
    Update an existing patient record.
    
    **Authorization:**
    - Requires authentication
    - Allowed roles: Admin, Doctor
    
    **Errors:**
    - 404 Not Found: Patient does not exist
    - 403 Forbidden: User role not authorized
    """
    patient = db.query(Patient).filter(Patient.id == patient_id).first()
    
    if not patient:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Patient with ID {patient_id} not found"
        )
    
    # Update patient fields
    for field, value in patient_data.model_dump().items():
        setattr(patient, field, value)
    
    db.commit()
    db.refresh(patient)
    
    return patient


@router.delete(
    "/{patient_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete Patient Record"
)
async def delete_patient(
    patient_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role([UserRole.ADMIN]))
):
    """
    Delete a patient record (Admin only).
    
    **Authorization:**
    - Requires authentication
    - Allowed roles: Admin only
    
    **Errors:**
    - 404 Not Found: Patient does not exist
    - 403 Forbidden: User is not Admin
    """
    patient = db.query(Patient).filter(Patient.id == patient_id).first()
    
    if not patient:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Patient with ID {patient_id} not found"
        )
    
    db.delete(patient)
    db.commit()
    
    return None
