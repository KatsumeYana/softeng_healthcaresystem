"""API routes package for St. Blaise Medical Clinic API"""

from .auth import router as auth_router
from .patients import router as patients_router
from .drugs import router as drugs_router
from .search import router as search_router

__all__ = ["auth_router", "patients_router", "drugs_router", "search_router"]
