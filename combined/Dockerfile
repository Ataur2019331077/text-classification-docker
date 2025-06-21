FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && pip install -r requirements.txt

# Copy all source code
# Set working dir and install dependencies...
COPY . .

# ✅ Fix permission issue
RUN chmod +x ./start.sh

# Expose ports and run services
EXPOSE 8000 8001 8002
CMD ["./start.sh"]

