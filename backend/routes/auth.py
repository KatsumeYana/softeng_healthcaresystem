"""
Authentication routes
Handles login and token generation (Supporting Form: Login)
"""

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta

from config.database import get_db
from config.settings import settings
from models.user import User
from utils.schemas import Token
from utils.security import verify_password, create_access_token

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/token", response_model=Token, summary="Login Form Endpoint")
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    """
    **SUPPORTING FORM 1: LOGIN FORM**
    
    Authenticates a user and returns a JWT access token.
    
    **Form Controls:**
    1. Username (textbox) - required
    2. Password (password field) - required
    
    **Validation:**
    - Username must exist in the database
    - Password must match the hashed password
    - User account must be active
    
    **Process:**
    1. Receive username and password from login form
    2. Query database for user with matching username
    3. Verify password against stored hash
    4. Check if account is active
    5. Generate JWT token with user info
    6. Return token for subsequent authenticated requests
    
    **Returns:**
    - access_token: JWT token for authentication
    - token_type: "bearer"
    
    **Errors:**
    - 401 Unauthorized: Invalid credentials or inactive account
    """
    # Query user from database
    user = db.query(User).filter(User.username == form_data.username).first()
    
    # Verify user exists and password is correct
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Check if user account is active
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Account is inactive. Please contact administrator.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Create access token
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username, "role": user.role.value},
        expires_delta=access_token_expires
    )
    
    # Return token
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


class LoginRequest(BaseModel):
    username: str
    password: str


@router.post("/login", response_model=Token, summary="Alternative Login Endpoint (JSON)")
async def login_json(
    payload: LoginRequest,
    db: Session = Depends(get_db)
):
    """Alternative login endpoint that accepts JSON body.
    **Example Request Body:**
    {
        "username": "admin",
        "password": "admin123"
    }
    """
    try:
        print(f"Login attempt for username: {payload.username}")
        user = db.query(User).filter(User.username == payload.username).first()
        
        if not user:
            print(f"User not found: {payload.username}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password"
            )
            
        print(f"User found: {user.username}, active: {user.is_active}")
        
        if not verify_password(payload.password, user.hashed_password):
            print("Password verification failed")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password"
            )
            
        if not user.is_active:
            print("User account is inactive")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Account is inactive"
            )
            
        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.username, "role": user.role.value},
            expires_delta=access_token_expires
        )
        
        print(f"Login successful for {user.username}")
        return {"access_token": access_token, "token_type": "bearer"}
        
    except Exception as e:
        print(f"Login error: {e}")
        raise
