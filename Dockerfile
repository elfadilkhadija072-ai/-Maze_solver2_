# Use a slim Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install system dependencies for Matplotlib
RUN apt-get update && apt-get install -y \
    libpng-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy your project files
COPY . /app

# Install Python libraries
RUN pip install --no-cache-dir pandas matplotlib

# Run your main script (adjust 'main.py' to your actual filename)
CMD ["python", "main.py"]
