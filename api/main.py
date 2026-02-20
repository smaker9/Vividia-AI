from fastapi import FastAPI
from pydantic import BaseModel
import os
from groq import Groq

app = FastAPI()
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

class ChatRequest(BaseModel):
    message: str

@app.post("/api/chat")
async def chat(request: ChatRequest):
    try:
        completion = client.chat.completions.create(
            model="mixtral-8x7b-32768",
            messages=[{"role": "user", "content": request.message}]
        )
        return {"response": completion.choices[0].message.content}
    except Exception as e:
        return {"response": f"خطأ في المحرك: {str(e)}"}
