from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session, select
from models import Product
from database import engine, create_db_and_tables

app = FastAPI()

# Allow frontend access (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():
    create_db_and_tables()
    with Session(engine) as session:
        if not session.exec(select(Product)).first():
            products = [
                Product(
                    name="Glowseeker Body Cream", 
                    description="Hydrating cream", 
                    price=19.99, 
                    size="500ml",
                    ingredients=["Aqua", "Glycerin", "Shea Butter", "Vitamin E", "Hyaluronic Acid"]
                ),
                Product(
                    name="Glowseeker Cleanser", 
                    description="Gentle face wash", 
                    price=12.99, 
                    size="400ml",
                    ingredients=["Aqua", "Sodium Cocoyl Glutamate", "Chamomile Extract", "Aloe Vera", "Vitamin B5"]
                ),
                Product(
                    name="Glowseeker Serum", 
                    description="Brightening serum", 
                    price=24.99, 
                    size="150ml",
                    ingredients=["Aqua", "Niacinamide", "Vitamin C", "Retinol", "Peptides", "Argan Oil"]
                )
            ]
            session.add_all(products)
            session.commit()

# ✅ Route to get all products
@app.get("/products")
def get_products():
    with Session(engine) as session:
        return session.exec(select(Product)).all()

# ✅ Route to get a single product by ID
@app.get("/products/{product_id}")
def get_product(product_id: int):
    with Session(engine) as session:
        product = session.get(Product, product_id)
        if product:
            return product
        return {"error": "Product not found"}
