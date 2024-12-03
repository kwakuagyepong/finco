# Flask Auth Api (Login, Signup)

This is a simple Flask API for user registration (signup) and login with MySQL database.

## Setup

1. Clone the repository:

```bash
git clone https://github.com/Iam-Makafui/flask-auth-api.git
cd flask-auth-api
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
.\venv\Scripts\activate
```

3. Install the dependencies:
```bash
pip install -r requirements.txt
```

4. Set up your MySQL database and configure your connection in app/__init__.py.
5. Run the application:

```bash
python run.py
```

The API will be available at http://127.0.0.1:5000.

## API Endpoints

### Create a New User

**POST /users**

- **Description:** Create a new user.
- **Headers:**
  - `Authorization: Bearer <valid_token>`
- **Body Parameters:**
  - `email`: (string) The email of the new user.
  - `password`: (string) The password of the new user.


### Login

**GET /users**
- **Description:** User login.
- **Headers:**
  - `Authorization: Bearer <valid_token>`

  /:{email}/:{password}: Log in an existing user (requires a valid token in the Authorization header).


