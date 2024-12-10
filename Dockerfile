# Base Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy necessary files
COPY requirements.txt requirements.txt
COPY flask_login_app/ flask_login_app/
COPY tests/ tests/
# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000
EXPOSE 5000

# Command to run the application
CMD ["python", "flask_login_app/app.py"]
