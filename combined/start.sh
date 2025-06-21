#!/bin/bash

# Start sentiment classifier
uvicorn sentiment_classifier.main:app --host 0.0.0.0 --port 8001 &

# Start custom classifier
uvicorn custom_classifier.main:app --host 0.0.0.0 --port 8002 &

# Start gateway last (foreground to keep container alive)
uvicorn gateway.main:app --host 0.0.0.0 --port 8000
