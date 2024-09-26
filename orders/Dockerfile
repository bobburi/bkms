# Use Python base image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the code
COPY orders.py .

# Expose port 5000
EXPOSE 5001

# Run the application
CMD ["python", "orders.py"]
