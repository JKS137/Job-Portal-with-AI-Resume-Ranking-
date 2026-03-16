# Job Portal with AI Resume Ranking
**Domain / Category:** Web Application | Artificial Intelligence | NLP

---

## Abstract

The **Job Portal with AI Resume Ranking** is an intelligent recruitment platform that connects job seekers with relevant job listings using Artificial Intelligence (AI) and Natural Language Processing (NLP). Candidates upload their resumes, which are parsed and ranked against job descriptions using AI-powered matching algorithms. Recruiters receive an automatically sorted shortlist of the best-matching applicants, drastically reducing manual screening time.

---

## Objectives

- Automate resume screening and reduce recruiter workload.
- Match candidates to job listings using semantic AI (BERT-based) rather than simple keyword matching.
- Provide job seekers a transparent, user-friendly experience to track applications.
- Generate insights and analytics for recruiters and admins on hiring trends.

---

## User Roles

| Role | Description |
|------|-------------|
| **Job Seeker** | Registers, uploads resume, applies for jobs, tracks status |
| **Recruiter** | Posts jobs, views AI-ranked applicants, schedules interviews |
| **Admin** | Manages users, monitors AI performance, oversees system |

---

## Functional Requirements

### 1. User Management

**Job Seeker Module:**
- Register / Login (email, Google, LinkedIn OAuth)
- Upload and manage resumes (PDF, DOC formats)
- Apply for jobs and track application status in real time

**Recruiter Module:**
- Register / Login as an employer
- Post job listings with detailed descriptions, required skills, and filters
- View AI-ranked candidate applications per listing

**Admin Module:**
- Manage all job postings, users, and system settings
- Monitor AI performance metrics and retrain/refine algorithms

---

### 2. AI-Based Resume Ranking (Core Feature)

#### a. Resume Parsing

Extract and structure information from uploaded resumes:

| Step | Process | Tools |
|------|---------|-------|
| Text Extraction | Extract raw text from PDF/DOC | PyMuPDF, PDFMiner, Apache Tika |
| Data Structuring | Identify name, email, experience, education, skills | Regex + NLP |
| Named Entity Recognition (NER) | Tag entities like job titles, universities | spaCy, NLTK, BERT |
| Keyword Extraction | Identify relevant terms using frequency analysis | TF-IDF |

Extracted fields per resume:
- Personal Info (Name, Email, Phone, Location)
- Work Experience (Titles, Companies, Years)
- Education (Degrees, Institutions, Graduation Year)
- Skills (Technical + Soft)
- Certifications & Projects

#### b. Job Matching Algorithm

Semantic similarity between resume and job description using **BERT**:

- BERT understands full contextual meaning (not just exact keyword matches).
- Example: A job requiring "cloud technologies" will match a resume listing "AWS, Azure, Google Cloud" even without exact word overlap.
- Cosine similarity score between job description embedding and resume embedding generates a rank.

#### c. Skill-Based Filtering

- **Technical Skills:** Ranked by hard-skill match (e.g., Python, React.js, Docker)
- **Soft Skills:** Sentiment analysis on cover letters / summaries
- **Experience Filter:** Recruiters can set minimum years of experience to auto-filter

---

### 3. Job Search & Discovery

- Full-text keyword search for job seekers
- Advanced filters: location, salary range, job type, experience level
- AI-powered personalized job recommendation engine

---

### 4. Application Tracking System (ATS)

- Recruiters view shortlisted candidates sorted by AI rank score
- Accept / Reject applications with one click
- Automated email/SMS notifications to applicants on status change
- Interview scheduling and in-portal communication tools

---

### 5. Data Visualization & Analytics Dashboard

- Job trend charts (most in-demand skills, locations, industries)
- Applicant demographics and pipeline analytics
- Recruiter performance insights

---

### 6. Notifications & Alerts

- Email/SMS alerts for new matching job postings
- Application status update notifications
- AI-generated upskilling course recommendations based on skill gaps

---

## Tech Stack

### Backend
- **Language:** Python
- **Framework:** Flask or Django
- **API Style:** REST (JSON)

### Frontend
- **Framework:** React.js or Angular.js
- **Styling:** Tailwind CSS / Bootstrap

### Database
- **Primary DB:** MySQL
- **Search Index:** Elasticsearch (optional, for fast job search)

### AI / ML Libraries

| Purpose | Library / Tool |
|---------|----------------|
| Resume Parsing | PyMuPDF, PDFMiner |
| NLP & NER | spaCy, NLTK |
| Semantic Matching | HuggingFace Transformers (BERT) |
| Keyword Extraction | TF-IDF (scikit-learn) |
| Ranking Model | Scikit-learn, TensorFlow |

### Authentication
- JWT Tokens for session management
- OAuth2 (Google / LinkedIn login)

### Hosting (Suggested)
- Backend: Heroku / Railway / AWS EC2
- Frontend: Vercel / Netlify
- DB: PlanetScale / AWS RDS

---

## System Architecture

```
[Job Seeker / Recruiter / Admin]
         |
    [React.js Frontend]
         |
    [Flask/Django REST API]
         |
   ┌─────┴──────┐
[MySQL DB]  [AI Engine]
              |
    ┌─────────┴─────────┐
 [Resume Parser]  [BERT Matcher]
 (PyMuPDF + spaCy)  (HuggingFace)
```

---

## Development Workflow

### Phase 1 — Setup & Planning
- [ ] Define SRS (Software Requirements Specification)
- [ ] Design ER diagram and database schema
- [ ] Set up Git repository and project structure

### Phase 2 — Core Backend
- [ ] User registration, login, and role-based access
- [ ] Job posting CRUD endpoints
- [ ] Resume upload and storage (local or S3)

### Phase 3 — AI Engine
- [ ] Resume text extraction module
- [ ] NER and keyword extraction pipeline
- [ ] BERT-based semantic similarity model
- [ ] Ranking and scoring API endpoint

### Phase 4 — Frontend
- [ ] Job Seeker dashboard (search, apply, track)
- [ ] Recruiter dashboard (post, view ranked applicants)
- [ ] Admin panel (user/job management)

### Phase 5 — Integration & Testing
- [ ] Connect frontend to API
- [ ] Unit tests for AI components
- [ ] End-to-end workflow testing

### Phase 6 — Deployment & Documentation
- [ ] Deploy backend and frontend
- [ ] Write user manual and technical docs
- [ ] Final demo and submission

---

## Suggested Dataset / Resources

- Resume datasets from Kaggle (e.g., "Resume Dataset" by gauravduttakiit)
- Job description datasets (LinkedIn Job Postings dataset on Kaggle)
- HuggingFace pre-trained BERT: `bert-base-uncased`

---

## Important Notes

- VU will **not** pay for any software, library, toolkit, or API used in this project.
- Attendance at MS Teams sessions with supervisor is **mandatory**.
- Students must prepare SRS and initial design documentation as prerequisites.
- Free-tier cloud services (Heroku, Vercel, PlanetScale) are recommended to avoid costs.

---

## Deliverables Checklist

- [ ] Software Requirements Specification (SRS)
- [ ] UI/UX Wireframes (Figma or hand-drawn)
- [ ] Database Schema (ER Diagram)
- [ ] Functional AI Resume Parsing & Ranking Module
- [ ] Fully working web application (frontend + backend)
- [ ] Deployed live demo link
- [ ] Final project report and presentation

---