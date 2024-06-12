# FastAPI FairyTale

A FairyTale using FastAPI and Postgres.

- Includes routes for all CRUD processes
- Includes CORS Middleware
- Uses Alembic for database migrations

## Route Testing

FastAPI comes with Swagger docs by default, all API routes are testable via: [http://localhost:8000/docs](http://localhost:8000/docs)

## Getting Started

- First, create a local database called `fairytales`
  - Pro Tip: You can create a DB directly via the CLI: `createdb fairytales`
- Use Alembic + FastAPI Models to generate your database tables