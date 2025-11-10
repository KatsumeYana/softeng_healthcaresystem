"""
Drug/Formulary management routes
Handles drug inventory operations (Major Form: Add New Drug)
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from config.database import get_db
from models.drug import Drug
from models.user import User, UserRole
from utils.schemas import DrugCreate, DrugOut, DrugUpdate
from utils.security import get_current_active_user, require_role

router = APIRouter(
    prefix="/drugs",
    tags=["Drugs"]
)


@router.post(
    "",
    response_model=DrugOut,
    status_code=status.HTTP_201_CREATED,
    summary="Add New Drug Form Endpoint"
)
async def create_drug(
    drug_data: DrugCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role([UserRole.ADMIN, UserRole.PHARMACIST]))
):
    """
    **MAJOR FORM 2: ADD NEW DRUG FORM**
    
    Adds a new drug to the formulary/inventory system.
    
    **Form Controls (10 fields):**
    1. Drug ID (textbox) - required, unique
    2. Brand Name (textbox) - required
    3. Generic Name (textbox) - required
    4. Dosage Form (dropdown) - required (Tablet, Capsule, Syrup, etc.)
    5. Strength (textbox) - required (e.g., "500 mg")
    6. Category (dropdown) - required (Analgesic, Antibiotic, etc.)
    7. Quantity (number) - required, must be >= 0
    8. Cost (number) - required, must be > 0
    9. Supplier (textbox) - optional
    10. Description (textarea) - optional
    
    **Validation:**
    - Drug ID must be unique (no duplicates)
    - All required fields must be provided
    - Quantity cannot be negative
    - Cost must be positive
    - Drug ID is automatically converted to uppercase
    
    **Authorization:**
    - Requires authentication (JWT token)
    - Allowed roles: Admin, Pharmacist
    
    **Process:**
    1. Validate all form data using Pydantic schema
    2. Check user authorization (Admin or Pharmacist only)
    3. Check for duplicate drug_id in database
    4. Create new drug record in database
    5. Log activity (in production)
    6. Return created drug data with assigned ID
    
    **Returns:**
    - Complete drug record with database ID and timestamps
    
    **Errors:**
    - 401 Unauthorized: Missing or invalid token
    - 403 Forbidden: User role not authorized (only Admin/Pharmacist)
    - 409 Conflict: Drug ID already exists
    - 422 Unprocessable Entity: Validation errors
    """
    # Check for duplicate drug_id
    existing_drug = db.query(Drug).filter(Drug.drug_id == drug_data.drug_id).first()
    if existing_drug:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Drug with ID '{drug_data.drug_id}' already exists in the formulary"
        )
    
    # Create new drug instance
    new_drug = Drug(**drug_data.model_dump())
    
    # Add to database
    db.add(new_drug)
    db.commit()
    db.refresh(new_drug)
    
    # In production, log this activity to UserActivityLog
    # log_activity(current_user.id, "CREATE_DRUG", new_drug.id)
    
    return new_drug


@router.get(
    "",
    response_model=List[DrugOut],
    summary="Get All Drugs (Formulary)"
)
async def get_all_drugs(
    skip: int = 0,
    limit: int = 100,
    active_only: bool = True,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Retrieve all drugs in the formulary with pagination.
    
    **Query Parameters:**
    - skip: Number of records to skip (default: 0)
    - limit: Maximum number of records to return (default: 100)
    - active_only: Only return active drugs (default: True)
    
    **Authorization:**
    - Requires authentication
    - All authenticated users can view formulary
    """
    query = db.query(Drug)
    
    if active_only:
        query = query.filter(Drug.is_active == 1)
    
    drugs = query.offset(skip).limit(limit).all()
    return drugs


@router.get(
    "/{drug_id}",
    response_model=DrugOut,
    summary="Get Drug by ID"
)
async def get_drug(
    drug_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Retrieve a specific drug record by database ID.
    
    **Path Parameters:**
    - drug_id: The unique database identifier of the drug
    
    **Authorization:**
    - Requires authentication
    
    **Errors:**
    - 404 Not Found: Drug with specified ID does not exist
    """
    drug = db.query(Drug).filter(Drug.id == drug_id).first()
    
    if not drug:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Drug with ID {drug_id} not found"
        )
    
    return drug


@router.get(
    "/code/{drug_code}",
    response_model=DrugOut,
    summary="Get Drug by Drug Code"
)
async def get_drug_by_code(
    drug_code: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Retrieve a specific drug record by drug code (e.g., "DR-001").
    
    **Path Parameters:**
    - drug_code: The drug identifier code (e.g., DR-001)
    
    **Errors:**
    - 404 Not Found: Drug with specified code does not exist
    """
    drug = db.query(Drug).filter(Drug.drug_id == drug_code.upper()).first()
    
    if not drug:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Drug with code '{drug_code}' not found"
        )
    
    return drug


@router.put(
    "/{drug_id}",
    response_model=DrugOut,
    summary="Update Drug Record"
)
async def update_drug(
    drug_id: int,
    drug_data: DrugUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role([UserRole.ADMIN, UserRole.PHARMACIST]))
):
    """
    Update an existing drug record.
    
    **Authorization:**
    - Requires authentication
    - Allowed roles: Admin, Pharmacist
    
    **Errors:**
    - 404 Not Found: Drug does not exist
    - 403 Forbidden: User role not authorized
    """
    drug = db.query(Drug).filter(Drug.id == drug_id).first()
    
    if not drug:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Drug with ID {drug_id} not found"
        )
    
    # Update only provided fields
    update_data = drug_data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(drug, field, value)
    
    db.commit()
    db.refresh(drug)
    
    return drug


@router.delete(
    "/{drug_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Archive/Delete Drug"
)
async def archive_drug(
    drug_id: int,
    permanent: bool = False,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role([UserRole.ADMIN]))
):
    """
    Archive or permanently delete a drug record.
    
    **Query Parameters:**
    - permanent: If True, permanently delete. If False, just mark as inactive (default: False)
    
    **Authorization:**
    - Requires authentication
    - Allowed roles: Admin only
    
    **Errors:**
    - 404 Not Found: Drug does not exist
    - 403 Forbidden: User is not Admin
    """
    drug = db.query(Drug).filter(Drug.id == drug_id).first()
    
    if not drug:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Drug with ID {drug_id} not found"
        )
    
    if permanent:
        # Permanently delete from database
        db.delete(drug)
    else:
        # Just mark as inactive (soft delete)
        drug.is_active = 0
    
    db.commit()
    
    return None
