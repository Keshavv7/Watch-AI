# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Install dependencies
COPY backend/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container
COPY . /app/

# Create a user to run the application
RUN useradd -m myuser
USER myuser

# Run the FastAPI application
# CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
CMD ["sh", "-c", "PYTHONPATH=/app/src uvicorn src.main:app --host 0.0.0.0 --port 8000"]
