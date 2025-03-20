# Base image
FROM python:3.11-slim

# Working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

ENV PYTHONPATH=/app


# Copy project files
COPY . .

# Run the application
CMD ["python", "src/main.py"]

