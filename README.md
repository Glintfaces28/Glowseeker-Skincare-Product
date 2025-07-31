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

# Run the API
uvicorn Backend.main:app --reload
# API: http://127.0.0.1:8000
# Docs: http://127.0.0.1:8000/docs
