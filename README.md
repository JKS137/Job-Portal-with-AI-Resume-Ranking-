# Job Portal with AI Resume Ranking

A recruitment platform that connects job seekers with job listings using AI-based resume parsing and ranking.

## Repository structure

- `backend/` – Django REST API for user, job, and resume management.
- `frontend/` – React application for job seekers and recruiters.

## Local setup

### Backend (Django)

1. Create a virtual environment:
   ```bash
   python -m venv backend/venv
   ```
2. Activate the venv:
   - Windows (PowerShell): `backend\venv\Scripts\Activate.ps1`
   - macOS/Linux: `source backend/venv/bin/activate`
3. Install dependencies:
   ```bash
   pip install -r backend/requirements.txt
   ```
4. Apply migrations and start server:
   ```bash
   cd backend
   python manage.py migrate
   python manage.py runserver
   ```

The API will run at: `http://127.0.0.1:8000/`

### Frontend (React)

1. Install dependencies:
   ```bash
   cd frontend
   npm install
   ```
2. Start the development server:
   ```bash
   npm run dev
   ```

The frontend will run at: `http://localhost:5173/`

## Notes

- The backend uses SQLite for development by default.
- Update environment variables for production configuration (e.g., `DJANGO_SECRET_KEY`).
