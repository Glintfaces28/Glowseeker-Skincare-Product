# Glowseeker Skincare Product

A simple full‑stack app:

- **Backend:** FastAPI + SQLModel + SQLite  
- **Frontend:** React (Create React App)

---

## Local Development

### 1) Backend (FastAPI)

From the repo root:

```bash
# Create and activate venv (Windows PowerShell)
python -m venv venv
.\venv\Scripts\activate

# Install deps
pip install -r Backend/requirements.txt

# Run the API (reload for dev)
cd Backend
uvicorn main:app --reload
# API at http://127.0.0.1:8000
# Swagger docs at http://127.0.0.1:8000/docs

2) Frontend (React)
In a second terminal:
cd frontend
npm install

# Point the frontend to the API (optional if your API runs on 127.0.0.1:8000)
# Create a .env file in /frontend/ with:
# REACT_APP_API_URL=http://127.0.0.1:8000

# Start the dev server
npm start

# React app at http://localhost:3000
Project Structure

3)Glowseeker-Skincare-Product/
├─ Backend/
│  ├─ main.py
│  ├─ models.py
│  ├─ database.py
│  └─ requirements.txt
├─ frontend/
│  ├─ public/
│  └─ src/
├─ .gitignore
├─ package.json
├─ package-lock.json
└─ README.md

## API Endpoints (examples)

- **GET** `/products` → list all products  
- **GET** `/products/{id}` → fetch details for a single product  

Open **Swagger UI** for testing the API endpoints at:  
`http://127.0.0.1:8000/docs`  

---

## Scripts (common)

### Backend
```bash
# From repo root
.\venv\Scripts\activate
cd Backend
uvicorn main:app --reload

cd frontend
npm start

---

## License

MIT License. See the [LICENSE](LICENSE) file for details.
**"Update README with API and Scripts info"**.


