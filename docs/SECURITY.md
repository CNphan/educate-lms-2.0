# Security and privacy development policy

**Prototype only. Not audited, compliant, or production-ready.** Do not store PII, PHI, education records, or real student information.

- Local `.env` files, secrets, keys and credentials must never enter Git.
- `.env.example` has placeholders only; development containers should bind ports to localhost.
- Enforce server-side school tenancy and role permissions on every endpoint and job.
- Add PostgreSQL RLS before any production tenant data.
- Implement school SSO, MFA, audit events, rate limiting, encrypted backups, disaster recovery, retention controls, and monitoring.
- Complete FERPA/COPPA applicability review; determine HIPAA applicability with counsel where school health data are in scope.
- Commission independent security/privacy assessments before accepting real school data.
