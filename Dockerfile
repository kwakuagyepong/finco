FROM python:3.11-alpine

# Set up environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies for mysqlclient
RUN apk add --no-cache \
    gcc \
    musl-dev \
    mariadb-connector-c-dev \
    mariadb-dev

# Create and set the working directory
WORKDIR /app

# Copy only the requirements file first to leverage Docker caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application code
COPY . .

# Expose the port your application will run on
EXPOSE 5000
EXPOSE 3306

# Specify the command to run on container start
CMD ["python", "run.py"]