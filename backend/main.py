"""
St. Blaise Medical Clinic and Pharmacy - Backend API
Main application file that initializes FastAPI and registers all routes
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config.settings import settings
from routes import auth_router, patients_router, drugs_router, search_router

# Create FastAPI application instance
app = FastAPI(
    title=settings.APP_NAME,
    description="""
    Backend API for St. Blaise Medical Clinic and Pharmacy Management System.
    
    Features
    
    This API provides endpoints for:
    
    *Authentication - User login and JWT token management
    *Patient Management - Create, read, update, and delete patient records
    *Drug/Formulary Management - Manage drug inventory and formulary
    *Search - Search across patient and drug records
    
    ## Forms Implemented
    
    Major Forms (2 required)
    1. Add New Patient Form - Complete patient registration with 15+ fields
    2. Add New Drug Form - Drug formulary management with 10+ fields
    
    ### Supporting Forms (2 required)
    1. Login Form - User authentication with username and password
    2. Search Records Form - Search patients and drugs by various criteria
    
    ## Authentication
    
    Most endpoints require authentication using JWT tokens:
    1. Login via `/auth/token` to get an access token
    2. Include the token in subsequent requests: `Authorization: Bearer <token>`
    
    ## Authorization
    
    Different endpoints require different user roles:
    - Admin: Full access to all operations
    - Doctor: Patient management, view formulary
    - Pharmacist: Drug management, view patients
    - Assistant/Cashier: Patient registration, view records
    """,
    version=settings.APP_VERSION,
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configure CORS (Cross-Origin Resource Sharing)
# This allows the Flutter frontend to communicate with the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(auth_router)
app.include_router(patients_router)
app.include_router(drugs_router)
app.include_router(search_router)


@app.get("/", tags=["Root"])
async def root():
    """
    Root endpoint - API health check and information
    """
    return {
        "message": "St. Blaise Medical Clinic and Pharmacy API",
        "version": settings.APP_VERSION,
        "status": "operational",
        "docs": "/docs",
        "redoc": "/redoc"
    }


@app.get("/health", tags=["Root"])
async def health_check():
    """
    Health check endpoint for monitoring
    """
    return {
        "status": "healthy",
        "service": settings.APP_NAME,
        "version": settings.APP_VERSION
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.DEBUG
    )
