"""
Drug model for storing drug/formulary information
"""

from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from sqlalchemy.sql import func
from config.database import Base


class Drug(Base):
    """
    Drug table for storing formulary information
    Corresponds to the "Add New Drug" form and Formulary maintenance
    """
    __tablename__ = "drugs"

    # Primary Key
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    
    # Drug Identification  
    drug_id = Column(String(20), unique=True, index=True, nullable=False)  # DR-001, DR-002, etc.
    brand_name = Column(String(200), nullable=False, index=True)  # Biogesic, Alnix, etc.
    generic_name = Column(String(200), nullable=False, index=True)  # Paracetamol, Cetirizine, etc.
    
    # Drug Details
    dosage_form = Column(String(50), nullable=False)  # Tablet, Capsule, Syrup, Nebule, etc.
    strength = Column(String(100), nullable=False)  # e.g., "500 mg", "5 mg", "2.5 mg"
    category = Column(String(100), nullable=False)  # Analgesic, Antihistamine, Antibiotic, etc.
    
    # Additional drug information
    manufacturer = Column(String(100), nullable=True)
    batch_number = Column(String(50), nullable=True)
    expiry_date = Column(String(20), nullable=True)  # Store as string for flexibility
    quantity_in_stock = Column(Integer, nullable=False, default=0)
    unit_price = Column(Float, nullable=False)
    description = Column(Text, nullable=True)
    side_effects = Column(Text, nullable=True)
    contraindications = Column(Text, nullable=True)
    storage_conditions = Column(Text, nullable=True)
    prescription_required = Column(Integer, default=1, nullable=False)  # 1 = required, 0 = not required
    
    # Status
    is_active = Column(Integer, default=1, nullable=False)  # 1 = active, 0 = archived
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    def __repr__(self):
        return f"<Drug(id={self.id}, drug_id='{self.drug_id}', brand_name='{self.brand_name}')>"
