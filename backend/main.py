from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai

app = FastAPI()

openai.api_key = "YOUR_OPENAI_API_KEY"

class Message(BaseModel):
    content: str

@app.post("/chat/")
async def chat(message: Message):
    try:
        response = openai.Completion.create(
            engine="gpt-4o",
            prompt=message.content,
            max_tokens=150
        )
        return {"response": response.choices[0].text.strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
