FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && pip install -r requirements.txt

# Copy all source code
COPY . .

# Expose all ports
EXPOSE 8000 8001 8002

# Start all 3 services
CMD ["./start.sh"]
