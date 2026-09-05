# Use a lightweight Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy application files
COPY test.py /app/

# Run as non-root user for basic container security
USER 10001

CMD ["python", "test.py"]