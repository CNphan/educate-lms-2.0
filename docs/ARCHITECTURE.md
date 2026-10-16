# Architecture (planned)

Next.js / TypeScript UI → Django REST API → PostgreSQL. The initial proof of concept provides membership-scoped read endpoints. Future milestones introduce SSO/MFA, database Row Level Security, school-specific configuration, auditable data access, and AWS ECS/RDS/S3/SQS resources managed as code.

**Trust boundary:** the browser does not determine tenant identity or authorization. Every data access must enforce the authenticated principal and membership; later, PostgreSQL RLS should provide independent defense in depth. No real school data should be stored during prototype development.
