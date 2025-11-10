"""
Search routes
Handles searching across patients and drugs (Supporting Form: Search Records)
"""

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import or_
from typing import List, Union, Literal

from config.database import get_db
from models.patient import Patient
from models.drug import Drug
from models.user import User
from utils.schemas import PatientOut, DrugOut
from utils.security import get_current_active_user

router = APIRouter(
    prefix="/search",
    tags=["Search"]
)


@router.get(
    "/patients",
    response_model=List[PatientOut],
    summary="Search Patients"
)
async def search_patients(
    query: str = Query(..., min_length=1, description="Search term for patient name or phone"),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    **SUPPORTING FORM 2: SEARCH RECORDS FORM (Patients)**
    
    Search for patient records by name or phone number.
    
    **Form Controls:**
    1. Search Query (textbox) - required, minimum 1 character
    2. Search Type selector (implicit: patients)
    
    **Search Fields:**
    - Full name (partial match, case-insensitive)
    - Phone number (partial match)
    
    **Validation:**
    - Query must be at least 1 character
    - User must be authenticated
    
    **Process:**
    1. Receive search query from form
    2. Search database for matching patients
    3. Return list of matching patient records
    
    **Authorization:**
    - Requires authentication
    - All authenticated users can search
    
    **Returns:**
    - List of patient records matching the search criteria
    - Empty list if no matches found
    """
    # Search in full_name and phone_number fields
    search_pattern = f"%{query}%"
    
    patients = db.query(Patient).filter(
        or_(
            Patient.full_name.like(search_pattern),
            Patient.phone_number.like(search_pattern)
        )
    ).all()
    
    return patients


@router.get(
    "/drugs",
    response_model=List[DrugOut],
    summary="Search Drugs"
)
async def search_drugs(
    query: str = Query(..., min_length=1, description="Search term for drug ID, brand name, or generic name"),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    **SUPPORTING FORM 2: SEARCH RECORDS FORM (Drugs)**
    
    Search for drugs in the formulary by ID, brand name, or generic name.
    
    **Form Controls:**
    1. Search Query (textbox) - required, minimum 1 character
    2. Search Type selector (implicit: drugs)
    
    **Search Fields:**
    - Drug ID (partial match, case-insensitive)
    - Brand name (partial match, case-insensitive)
    - Generic name (partial match, case-insensitive)
    - Category (partial match, case-insensitive)
    
    **Validation:**
    - Query must be at least 1 character
    - User must be authenticated
    - Only returns active drugs by default
    
    **Process:**
    1. Receive search query from form
    2. Search database for matching drugs
    3. Return list of matching drug records
    
    **Authorization:**
    - Requires authentication
    - All authenticated users can search formulary
    
    **Returns:**
    - List of drug records matching the search criteria
    - Empty list if no matches found
    """
    # Search in multiple fields
    search_pattern = f"%{query}%"
    
    drugs = db.query(Drug).filter(
        Drug.is_active == 1,  # Only search active drugs
        or_(
            Drug.drug_id.like(search_pattern),
            Drug.brand_name.like(search_pattern),
            Drug.generic_name.like(search_pattern),
            Drug.category.like(search_pattern)
        )
    ).all()
    
    return drugs


@router.get(
    "",
    summary="Universal Search Endpoint"
)
async def universal_search(
    query: str = Query(..., min_length=1, description="Search term"),
    scope: Literal['patients', 'drugs', 'all'] = Query('all', description="Search scope"),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    **SUPPORTING FORM 2: SEARCH RECORDS FORM (Universal)**
    
    Universal search endpoint that can search across patients, drugs, or both.
    
    **Form Controls:**
    1. Search Query (textbox) - required
    2. Scope Selector (dropdown/radio) - patients, drugs, or all
    
    **Query Parameters:**
    - query: The search term
    - scope: Where to search ('patients', 'drugs', or 'all')
    
    **Returns:**
    - JSON object with separate lists for patients and drugs
    - Includes count of results in each category
    
    **Example Response:**
    ```json
    {
        "query": "maria",
        "scope": "all",
        "results": {
            "patients": [...],
            "drugs": []
        },
        "counts": {
            "patients": 2,
            "drugs": 0,
            "total": 2
        }
    }
    ```
    """
    search_pattern = f"%{query}%"
    results = {
        "query": query,
        "scope": scope,
        "results": {},
        "counts": {}
    }
    
    # Search patients if requested
    if scope in ['patients', 'all']:
        patients = db.query(Patient).filter(
            or_(
                Patient.full_name.like(search_pattern),
                Patient.phone_number.like(search_pattern)
            )
        ).all()
        results["results"]["patients"] = [PatientOut.model_validate(p) for p in patients]
        results["counts"]["patients"] = len(patients)
    
    # Search drugs if requested
    if scope in ['drugs', 'all']:
        drugs = db.query(Drug).filter(
            Drug.is_active == 1,
            or_(
                Drug.drug_id.like(search_pattern),
                Drug.brand_name.like(search_pattern),
                Drug.generic_name.like(search_pattern),
                Drug.category.like(search_pattern)
            )
        ).all()
        results["results"]["drugs"] = [DrugOut.model_validate(d) for d in drugs]
        results["counts"]["drugs"] = len(drugs)
    
    # Calculate total count
    results["counts"]["total"] = sum(results["counts"].values())
    
    return results
