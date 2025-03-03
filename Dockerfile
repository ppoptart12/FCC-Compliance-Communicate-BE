FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    libmariadb-dev-compat \
    libmariadb-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port that the app runs on
EXPOSE 8000

# Command to run the application
#     uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 1
#docker build -t my-fastapi-app .
# docker run --env-file .env -p 8000:8000 my-fastapi-app
# docker run --env-file .env --restart unless-stopped -p 8000:8000 my-fastapi-app

#LOOK AT HOW MANY WORKERS ARE ON THE SERVER
CMD ["gunicorn", "-w", "2", "-k", "uvicorn.workers.UvicornWorker", "app.main:app", "--bind", "0.0.0.0:8000"]