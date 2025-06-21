from fastapi import FastAPI, HTTPException, Security
from fastapi.security.api_key import APIKeyHeader
from pydantic import BaseModel
from typing import List
import httpx

app = FastAPI()

API_KEY = "my-secret-key"
API_KEY_NAME = "X-API-Key"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

class ClassificationRequest(BaseModel):
    text: str
    type: List[str]

@app.post("/classify")
async def classify(
    body: ClassificationRequest,
    api_key: str = Security(api_key_header)
):

    async with httpx.AsyncClient() as client:
        headers = {API_KEY_NAME: api_key}

        if not body.type:
            response = await client.post(
                "http://sentiment_service:8001/predict",
                json={"text": body.text},
                headers=headers
            )
        else:
            response = await client.post(
                "http://custom_service:8002/predict",
                json={"text": body.text, "type": body.type},
                headers=headers
            )

    return response.json()
