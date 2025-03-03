# FCC-Compliance-Communicate
Dashboard to monitor an organizations FCC compliance through regular document scans and tests using AI indexed on FCC regulations

## Backend API

This is the backend API for the FCC Compliance Communicate system.

### Features

- User authentication and authorization
- RESTful API endpoints
- Database integration with SQLAlchemy
- JWT token-based authentication
- Swagger documentation

### Tech Stack

- FastAPI
- SQLAlchemy
- Pydantic
- MySQL
- JWT Authentication

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/FCC-Compliance-Communicate-BE.git
cd FCC-Compliance-Communicate-BE
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file based on `.env.example`:
```bash
cp .env.example .env
```

5. Edit the `.env` file with your configuration.

6. Run the application:
```bash
uvicorn app.main:app --reload
```

### API Documentation

Once the application is running, you can access the API documentation at:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### Docker

You can also run the application using Docker:

```bash
# Build the Docker image
docker build -t fcc-compliance-communicate-be .

# Run the container
docker run --env-file .env -p 8000:8000 fcc-compliance-communicate-be
```

### Project Structure

```
app/
├── api/
│   └── v1/
│       └── endpoints/
│           ├── Auth/
│           │   └── user.py
│           └── UnAuth/
│               └── auth.py
├── core/
│   ├── config.py
│   └── logging_config.py
├── db/
│   └── database.py
├── models/
│   └── user.py
├── schemas/
│   ├── token.py
│   └── user.py
├── utils/
│   ├── auth.py
│   └── security.py
└── main.py
```
