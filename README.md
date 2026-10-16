# Educate LMS 2.0

A clean-room, multi-tenant learning management system SaaS starter for schools, universities and independent educators.

**Stack:** Next.js + TypeScript, Django REST Framework, PostgreSQL, Docker. AWS production infrastructure is planned, not implemented.

> **Development only. Do not deploy publicly or upload real student, health, or personal data.** This project is not certified for FERPA, COPPA, HIPAA or other compliance frameworks.

## Getting started

1. Install Docker Desktop.
2. Copy `.env.example` to `.env` and replace the placeholder local secrets.
3. Run `docker compose up --build -d`.
4. Visit `http://localhost:3000` for the app and `http://localhost:8000/health/` for health status.
5. Run `docker compose exec api python manage.py test`.

The current dashboard is a preview, **not** an authenticated production application. No real school data should be stored.

## Roadmap

- [x] Initial Next.js / Django / PostgreSQL development scaffold
- [x] School membership and course data models
- [x] Preliminary organization-scoped API queries and tests
- [ ] Real login, SSO/MFA and authorization review
- [ ] Database Row Level Security and tenant isolation tests
- [ ] Auditing, privacy rights workflow, secure file storage
- [ ] Assignments, gradebook and student/teacher experiences
- [ ] AWS infrastructure as code, monitoring and independent security reviews

See `docs/SECURITY.md` and `docs/ARCHITECTURE.md`.
