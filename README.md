# MaaS - Math As A Service

A FastAPI-based web service providing math functions with JWT authentication, user management, and request logging.

## Features

- **User Registration & Login**: Secure user creation and login with password hashing and JWT token issuance.
- **JWT Authentication**: All math and log endpoints are protected; only authenticated users can access them.
- **Math Endpoints**:
  - `GET /api/v1/pow`: Power calculation (`base`, `exp`)
  - `GET /api/v1/nFib`: Nth Fibonacci number (`n`)
  - `GET /api/v1/factorial`: Factorial calculation (`n`)
- **Request Logging**: All operations are logged with input, result, and request source.
- **User Management**: List all users (admin/protected endpoint).
- **Global Error Handling**: Consistent JSON error responses for validation, integrity, and HTTP errors.
- **Swagger UI**: Interactive API docs at `/docs`.

## Installation

1. **Clone the repository**:
   ```sh
   git clone <your-repo-url>
   cd tema python 2
   ```

2. **Create a virtual environment (optional but recommended)**:
   ```sh
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```sh
   uvicorn main:app --reload
   ```

5. **Access the API**:
   - Root: [http://localhost:8000/](http://localhost:8000/)
   - Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)

## Usage

### 1. Register a User

`POST /api/v1/user/create`

Body (JSON):
```json
{
  "username": "yourname",
  "email": "your@email.com",
  "password": "yourpassword"
}
```
Returns a JWT token.

### 2. Login

`POST /api/v1/user/login`

Body (JSON):
```json
{
  "email": "your@email.com",
  "password": "yourpassword"
}
```
Returns a JWT token.

### 3. Authorize in Swagger

- Click "Authorize" in Swagger UI.
- Enter: `Bearer <your_token>`

### 4. Use Math Endpoints

All math endpoints require the JWT token in the `Authorization` header.

Example (using curl):
```sh
curl -H "Authorization: Bearer <your_token>" "http://localhost:8000/api/v1/factorial?n=5"
```

### 5. View Logs

`GET /api/v1/logs/all` (JWT required)

### 6. List Users

`GET /api/v1/users` (JWT required)

---

Let me know if you want to add more details or usage examples!
