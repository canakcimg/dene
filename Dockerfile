# Base image
FROM python:3.11-slim

# Working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files
COPY . .

# Run the application
CMD ["python", "src/main.py"]

