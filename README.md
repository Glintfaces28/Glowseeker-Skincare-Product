🌟 Glowseeker Skincare Product
A simple full‑stack web application for browsing skincare products.
Built with:

.Backend: FastAPI + SQLModel + SQLite
.Frontend: React (Create React App)

🚀 Features

📦 Product listing with name, price, and size
🔍 View detailed information for each product
⚡ Fast API responses using FastAPI
🎨 Modern, responsive React frontend

🛠️ Project Structure

Glowseeker-Skincare-Product/
├─ Backend/
│  ├─ main.py            # API entry point
│  ├─ models.py          # Database models
│  ├─ database.py        # Database setup
│  ├─ requirements.txt   # Python dependencies
├─ frontend/
│  ├─ public/
│  └─ src/
├─ .gitignore
├─ package.json
├─ package-lock.json
└─ README.md

1️⃣ Backend (FastAPI)

# Create and activate a virtual environment
python -m venv venv
.\venv\Scripts\activate   # Windows
# source venv/bin/activate  # Mac/Linux
# Install dependencies
pip install -r Backend/requirements.txt
# Run the API server
cd Backend
uvicorn main:app --reload
📌 API will run at: http://127.0.0.1:8000
📌 Swagger UI (API docs): http://127.0.0.1:8000/docs

2️⃣ Frontend (React)
In a second terminal:

cd frontend
npm install
# Optional: create a .env file with API URL
echo REACT_APP_API_URL=http://127.0.0.1:8000 > .env
# Start the frontend
npm start
# React app available at: http://localhost:3000


📡 API Endpoints
Method	Endpoint	Description
GET	/products	List all products
GET	/products/{id}	Get details of a product
Swagger UI is available at:
http://127.0.0.1:8000/docs

📜 License
This project is licensed under the MIT License – see the LICENSE file for details.






