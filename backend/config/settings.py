"""
Configuration settings for St. Blaise Medical Clinic API
Loads environment variables and provides configuration objects
"""

from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Application settings loaded from environment variables"""
    
    # Database Configuration  
    DATABASE_URL: str = "mysql+pymysql://healthcare_user:healthcare_pass@localhost:3306/healthcare_system"
    
    # MySQL Database Settings
    DB_HOST: str = "localhost"
    DB_PORT: int = 3306
    DB_NAME: str = "healthcare_system"
    DB_USER: str = "healthcare_user" 
    DB_PASSWORD: str = "healthcare_pass"
    
    # Security Configuration
    SECRET_KEY: str = "healthcare-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Application Configuration
    APP_NAME: str = "St. Blaise Medical Clinic API"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True
    
    class Config:
        env_file = ".env"
        case_sensitive = True


# Create a global settings instance
settings = Settings()
