# Use official Python runtime as base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy the requirements.txt
COPY requirements.txt .

# Install dependencies (if any)
RUN pip install --no-cache-dir -r requirements.txt

# Copy the script
COPY script.py .

# Make the script executable
RUN chmod +x script.py

# Set the entrypoint to the script
ENTRYPOINT ["python", "script.py"]