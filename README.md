# Flask Login App

A simple login application built with Flask and Docker, featuring a professional and elegant banking-themed background.

## Project Structure
```
flask-login-app/
├── flask_login_app/
│   ├── __init__.py
│   ├── app.py
│   └── templates/
│       └── login.html
├── requirements.txt
├── Dockerfile
├── static/
│   └── background.jpg
├── tests/
│   ├── __init__.py
│   └── test_app.py
└── README.md
```

## Features
- **Login Page:** A placeholder login form with username and password fields.
- **Stylish Background:** A professional banking-themed background image.
- **Dockerized Application:** Runs seamlessly in a Docker container.

## How to Run
1. **Build the Docker image:**
   ```bash
   docker build -t flask-login-app .
   ```

2. **Run the container:**
   ```bash
   docker run -p 5000:5000 flask-login-app
   ```

3. **Open the application:**
   Navigate to `http://localhost:5000` in your web browser to see the app.

## How to Run Tests
1. **Install the dependencies locally:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the tests:**
   ```bash
   pytest tests/
   ```

## Project Dependencies
- **Flask:** For building the web application.
- **Pytest:** For unit testing.

## Notes
- **Background Image:** Located in the `static/` directory, used to style the application background.
- **Port:** The app runs on port `5000` by default.
- **Default Credentials:** Placeholder login form, does not authenticate users.
