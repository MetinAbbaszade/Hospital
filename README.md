# Hospital

A hospital appointment platform with a separate panel for each user role.
Patients find hospitals and doctors and book appointments. Doctors, hospital
owners and admins manage their own data in their own panels.

This is my final project for the Introduction to Software Engineering program
at Holberton School.

## Features

- **Authentication**: sign-up, login and token refresh with JWT access and
  refresh tokens. Passwords are hashed with bcrypt.
- **Four roles**: `patient`, `doctor`, `owner` and `admin`. After login, the
  user is sent to the page for their role.
- **Patients**: browse hospitals and doctors on the main page (MedAze) and
  book appointments. The page is available in Azerbaijani, English and Russian.
- **Doctors**: view their profile, hospital, specializations and appointments.
- **Hospital owners**: manage their hospitals and the doctors who work there.
- **Admins**: manage users, hospitals and appointments.
- **Specializations**: linked to both doctors and hospitals.

The database models and API code for comments (patient → doctor, patient →
hospital, doctor → hospital, and comments on appointments) are written, but
their routes are not enabled yet.

## Tech stack

| Part     | Technologies                                              |
|----------|-----------------------------------------------------------|
| Backend  | Python 3.12, FastAPI, SQLModel / SQLAlchemy, Uvicorn      |
| Database | MySQL (PyMySQL driver)                                    |
| Auth     | PyJWT, passlib + bcrypt                                   |
| Frontend | HTML, CSS, vanilla JavaScript (Fetch API)                 |
| Tooling  | Poetry                                                    |

Database diagram: https://drawsql.app/teams/metins-company/diagrams/hospital-diagram

## Project structure

```
backend/
  app/
    api/v1/endpoints/   # FastAPI routers (one per resource)
    api/v1/schemas/     # Pydantic request/response models
    models/             # SQLModel database tables
    persistence/        # Repository layer
    service/            # Business logic (facades)
  run.py                # Entry point
frontend/
  Main Page/            # Public site for patients
  Login Page/           # Sign-up and login
  Doctor Panel/
  Hospital Management/  # Hospital owner panel
  Admin UI/
```

## Getting started

### Requirements

- Python 3.12 and [Poetry](https://python-poetry.org/)
- A running MySQL server
- A static file server for the frontend, such as the VS Code Live Server
  extension (the project is set up for port `5506`)

### Backend

1. Create a MySQL database named `Hospital`.
2. Update `MYSQL_LINK` in `backend/app/__init__.py` with your MySQL username
   and password.
3. Install the dependencies and start the server:

   ```bash
   cd backend
   poetry install
   poetry run python run.py
   ```

The API runs at `http://0.0.0.0:8000`, and the tables are created
automatically on first run. Interactive API docs are at
`http://localhost:8000/docs`.

### Frontend

Open the repository root in VS Code and start Live Server on port `5506`.
Then go to:

```
http://127.0.0.1:5506/frontend/Main%20Page/index.html
```

The login page sends each role to its panel using these URLs, so the port and
root folder must match.

## API overview

All routes use the `/api/v1` prefix:

| Prefix                     | Purpose                                 |
|----------------------------|-----------------------------------------|
| `/auth`                    | `signup`, `login`, `refresh`            |
| `/patient`                 | Patient profiles                        |
| `/doctor`                  | Doctors, including by hospital          |
| `/owner`                   | Hospital owners                         |
| `/admin`                   | Admin accounts                          |
| `/hospital`                | Hospitals, including by owner           |
| `/appointment`             | Appointments by doctor or patient       |
| `/specialization`          | Medical specializations                 |
| `/doctorspecialization`    | Links between doctors and specializations   |
| `/hospitalspecialization`  | Links between hospitals and specializations |

See `/docs` for the full list of endpoints and request bodies.

## Author

Metin Abbaszade, [GitHub](https://github.com/MetinAbbaszade)
