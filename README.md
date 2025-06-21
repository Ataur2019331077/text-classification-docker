# 📦 Text Classification Microservices with FastAPI
[![Docker Pulls](https://img.shields.io/docker/pulls/ataur077/text-classification-custom.svg)](https://hub.docker.com/r/ataur077/text-classification-custom)
<br>
A microservice-based architecture for text classification, using:

- **🔁 API Gateway (FastAPI):** One unified endpoint.

- **🎯 Sentiment Classifier:** Classifies text as positive, negative, or neutral.

- **🧠 Custom Classifier:** Classifies text using dynamic label sets provided in the request.

- **🔐 API Key Authentication:** Secured communication between client and services.

All services are Dockerized and orchestrated using Docker Compose.

## 🚀 Features
- **🧩 Microservice architecture:** Fully decoupled, easy to scale or extend.

- **📥 One endpoint:** Gateway routes requests based on payload structure.

- **🧠 Custom label classification:** Pass label sets dynamically for per-text classification.

- **🔐 Secure access** using X-API-Key header.

- **⚡ FastAPI-powered** endpoints with interactive Swagger UI.

📁 Project Structure
```
text-classification/
├── docker-compose.yml
├── gateway/
│   ├── main.py
│   ├── Dockerfile
│   └── requirements.txt
├── sentiment_classifier/
│   ├── main.py
│   ├── Dockerfile
│   ├── model/
│   │   └── model.pkl
│   └── requirements.txt
├── custom_classifier/
│   ├── main.py
│   ├── Dockerfile
│   └── requirements.txt
```
## 🛠️ Requirements
```
Docker

Docker Compose
```

If running without Docker, ensure you adjust service URLs to localhost instead of container names like sentiment_service.

## ⚙️ Getting Started
1. Clone the Repository
    ```
    git clone https://github.com/Ataur2019331077/text-classification-docker.git
    cd text-classification-docker
    ```
2. Build and Start Services
    ```
    docker-compose up --build
    ```
- 🌐 Gateway: http://localhost:8000

- 🔁 Sentiment Classifier: internal (sentiment_service:8001)

- 🧠 Custom Classifier: internal (custom_service:8002)



## 📬 Example API Usage
### POST /classify
```
{
  "text": "I am not happy.",
  "type": ["happy", "sad", "angry"]
}
```
- If type is empty → routed to sentiment service

- If type has values → routed to custom classifier

### 🧪 Sample curl:
```
curl -X POST http://localhost:8000/classify \
  -H "Content-Type: application/json" \
  -H "X-API-Key: my-secret-key" \
  -d '{"text": "I am not happy", "type": ["happy", "sad", "angry"]}'
  ```
### 📊 Swagger UI (Interactive Docs)
Available at:
```
http://localhost:8000/docs
```

Use the 🔐 "Authorize" button to input your API key for testing.
