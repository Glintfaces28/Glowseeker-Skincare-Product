from sqlmodel import SQLModel, create_engine

sqlite_file = "products.db"
engine = create_engine(f"sqlite:///{sqlite_file}")

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
