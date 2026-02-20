from fastapi import FastAPI
from pydantic import BaseModel
import os
from groq import Groq

app = FastAPI()

# إنشاء عميل Groq باستخدام المفتاح السري الموجود في إعدادات Vercel
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

class ChatRequest(BaseModel):
    message: str

@app.post("/api/chat")
async def chat(request: ChatRequest):
    try:
        # استخدام الموديل الجديد المحدث لعام 2026
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "أنت مساعد ذكي ومفيد تدعى Vividia AI، تجيب باللغة العربية بأسلوب لبق ومبدع."},
                {"role": "user", "content": request.message}
            ],
            temperature=0.7,
            max_tokens=1024
        )
        return {"response": completion.choices[0].message.content}
    except Exception as e:
        # في حال حدوث أي خطأ، سيظهر لنا السبب بوضوح
        return {"response": f"عذراً، حدث خطأ في المحرك: {str(e)}"}
