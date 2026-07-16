"""Chat endpoint with Groq AI"""
import logging, os, httpx
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"))

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = "llama-3.1-8b-instant"
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

router = APIRouter(prefix="/v1", tags=["chat"])

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    reply: str

SYSTEM_PROMPT = """Eres un asistente experto en ciberseguridad y prevención del ciberacoso en español. 
Tu nombre es SecBot. Debes responder preguntas sobre:
- Qué es el ciberacoso (cyberbullying)
- Cómo prevenirlo y protegerse
- Señales de alerta en niños y adolescentes
- Cómo reportar en redes sociales (Facebook, Instagram, TikTok, Twitter, WhatsApp, YouTube)
- Cómo bloquear a usuarios en redes sociales
- Pasos a seguir si alguien sufre ciberacoso
- Leyes y recursos en Panamá (Ley 81, línea de ayuda +507 800-1725)
- Consejos para padres
- Privacidad en línea
- Tipos de ciberacoso (exclusión, difamación, suplantación, ciberacoso sexual, sexting, grooming)

Responde siempre en español, de forma clara, breve y útil (máximo 4 párrafos).
Si la pregunta no está relacionada con ciberseguridad o ciberacoso, responde amablemente que solo puedes ayudar con temas de seguridad digital y ciberacoso."""

@router.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    if not GROQ_API_KEY:
        raise HTTPException(status_code=500, detail="GROQ_API_KEY no configurada")
    try:
        async with httpx.AsyncClient(timeout=30) as client:
            resp = await client.post(
                GROQ_URL,
                headers={"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"},
                json={
                    "model": GROQ_MODEL,
                    "messages": [
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {"role": "user", "content": req.message},
                    ],
                    "temperature": 0.7,
                    "max_tokens": 500,
                },
            )
        if resp.status_code != 200:
            raise HTTPException(status_code=resp.status_code, detail=f"Groq API error: {resp.text}")
        data = resp.json()
        reply = data["choices"][0]["message"]["content"]
        return ChatResponse(reply=reply)
    except httpx.TimeoutException:
        raise HTTPException(status_code=504, detail="Groq API timeout")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
