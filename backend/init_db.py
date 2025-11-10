"""
Database initialization script
Creates all tables and optionally seeds initial data
"""

from sqlalchemy import create_engine
from config.database import Base
from config.settings import settings
from models.user import User, UserRole
from models.patient import Patient
from models.drug import Drug
from utils.security import get_password_hash


def init_database():
    """
    Initialize the database by creating all tables
    """
    print("=" * 60)
    print("St. Blaise Medical Clinic - Database Initialization")
    print("=" * 60)
    
    # Create engine
    engine = create_engine(settings.DATABASE_URL, echo=True)
    
    print("\n[1/2] Creating database tables...")
    try:
        # Create all tables
        Base.metadata.create_all(bind=engine)
        print("✓ All tables created successfully!")
    except Exception as e:
        print(f"✗ Error creating tables: {e}")
        return False
    
    print("\n[2/2] Database initialization complete!")
    print("=" * 60)
    
    return True


def seed_initial_data():
    """
    Seed the database with initial test data
    """
    from sqlalchemy.orm import sessionmaker
    from config.database import engine
    
    print("\n" + "=" * 60)
    print("Seeding Initial Data")
    print("=" * 60)
    
    SessionLocal = sessionmaker(bind=engine)
    db = SessionLocal()
    
    try:
        # Check if users already exist
        existing_users = db.query(User).count()
        if existing_users > 0:
            print("\n⚠ Users already exist in database. Skipping user creation.")
        else:
            print("\n[1/3] Creating initial users...")
            
            # Create admin user
            admin_user = User(
                username="admin",
                full_name="Administrator",
                hashed_password=get_password_hash("admin123"),
                role=UserRole.ADMIN,
                is_active=True
            )
            db.add(admin_user)
            
            # Create doctor user
            doctor_user = User(
                username="dr_anasantos",
                full_name="Dr. Ana Santos",
                hashed_password=get_password_hash("doctor123"),
                role=UserRole.DOCTOR,
                is_active=True
            )
            db.add(doctor_user)
            
            # Create pharmacist user
            pharmacist_user = User(
                username="pharm_isabella",
                full_name="Isabella Cruz",
                hashed_password=get_password_hash("pharm123"),
                role=UserRole.PHARMACIST,
                is_active=True
            )
            db.add(pharmacist_user)
            
            # Create assistant user
            assistant_user = User(
                username="asst_juan",
                full_name="Juan Dela Cruz",
                hashed_password=get_password_hash("assistant123"),
                role=UserRole.ASSISTANT_CASHIER,
                is_active=True
            )
            db.add(assistant_user)
            
            db.commit()
            print("✓ Created 4 users (admin, doctor, pharmacist, assistant)")
        
        # Check if drugs already exist
        existing_drugs = db.query(Drug).count()
        if existing_drugs > 0:
            print("\n⚠ Drugs already exist in database. Skipping drug creation.")
        else:
            print("\n[2/3] Creating sample drugs...")
            
            # Sample drugs from the UI design
            drugs = [
                Drug(
                    drug_id="DR-001",
                    brand_name="Biogesic",
                    generic_name="Paracetamol",
                    dosage_form="Tablet",
                    strength="500 mg",
                    category="Analgesic",
                    manufacturer="Generic Pharma Inc.",
                    quantity_in_stock=200,
                    unit_price=5.00,
                    prescription_required=0
                ),
                Drug(
                    drug_id="DR-002",
                    brand_name="Alnix",
                    generic_name="Cetirizine Hydrochloride",
                    dosage_form="Syrup",
                    strength="5 mg",
                    category="Antihistamine",
                    manufacturer="Allergy Solutions Ltd.",
                    quantity_in_stock=50,
                    unit_price=85.00,
                    prescription_required=0
                ),
                Drug(
                    drug_id="DR-003",
                    brand_name="Amoxil",
                    generic_name="Amoxicillin",
                    dosage_form="Capsule",
                    strength="500 mg",
                    category="Antibiotic",
                    manufacturer="Antibiotic Suppliers Co.",
                    quantity_in_stock=150,
                    unit_price=12.00,
                    prescription_required=1
                ),
                Drug(
                    drug_id="DR-004",
                    brand_name="Diatabs",
                    generic_name="Loperamide",
                    dosage_form="Tablet",
                    strength="2 mg",
                    category="Antidiarrheal",
                    manufacturer="Digestive Health Inc.",
                    quantity_in_stock=100,
                    unit_price=8.00,
                    prescription_required=0
                ),
                Drug(
                    drug_id="DR-005",
                    brand_name="Ventolin",
                    generic_name="Salbutamol",
                    dosage_form="Nebule",
                    strength="2.5 mg",
                    category="Bronchodilator",
                    manufacturer="Respiratory Care Ltd.",
                    quantity_in_stock=75,
                    unit_price=15.00,
                    prescription_required=1
                ),
            ]
            
            for drug in drugs:
                db.add(drug)
            
            db.commit()
            print(f"✓ Created {len(drugs)} sample drugs")
        
        print("\n[3/3] Seeding complete!")
        print("\n" + "=" * 60)
        print("Initial Login Credentials:")
        print("=" * 60)
        print("Admin:      username: admin           | password: admin123")
        print("Doctor:     username: dr_anasantos    | password: doctor123")
        print("Pharmacist: username: pharm_isabella  | password: pharm123")
        print("Assistant:  username: asst_juan       | password: assistant123")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n✗ Error seeding data: {e}")
        db.rollback()
        return False
    finally:
        db.close()
    
    return True


if __name__ == "__main__":
    print("\nStarting database initialization...\n")
    
    # Initialize database structure
    if init_database():
        # Seed initial data
        seed_initial_data()
        print("\n✓ Database setup complete!\n")
    else:
        print("\n✗ Database setup failed!\n")
