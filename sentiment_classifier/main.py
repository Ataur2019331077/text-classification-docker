from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
import json
import requests

app = FastAPI()

HEADER_NAME = "X-API-Key"


def gemini_response(input_text, API_KEY):
    prompt = f"""
        Here is the input text:
        {input_text}
        Classify the text into one of the following categories:
        Positive, Negative or Neutral.

        DO NOT return any other text, just the classification result. JUST THE SINGLE WORD RESULT.
    """

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"
    headers = {
        "Content-Type": "application/json",
    }
    data = {
        "contents": [{
            "parts": [{
                "text": prompt
            }]
        }]
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    response.raise_for_status()
    response_json = response.json()

    generated_text = response_json["candidates"][0]["content"]["parts"][0]["text"]
    generated_text = generated_text.replace("```json", "").replace("```", "").strip()

    return generated_text

class TextInput(BaseModel):
    text: str

@app.post("/predict")
def predict(request: Request, input: TextInput):
    # Check API key
    API_KEY = request.headers.get(HEADER_NAME)
    if not API_KEY:
        raise HTTPException(status_code=401, detail="API key is missing or invalid")

    prediction = gemini_response(input.text, API_KEY)
    return {
        "text": input.text,
        "type": [],
        "prediction": prediction
    }
