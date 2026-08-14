from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
from pydantic import BaseModel
import io
import soundfile as sf
import numpy as np

# У цьому образі chatterbox встановлено інакше
try:
    from chatterbox.tts import ChatterboxTTS
    print("✅ Chatterbox imported from chatterbox.tts")
except ImportError:
    try:
        from chatterbox import ChatterboxTTS
        print("✅ Chatterbox imported from chatterbox")
    except ImportError:
        print("❌ Chatterbox not found!")
        ChatterboxTTS = None

app = FastAPI()

print("Loading TTS model...")
tts = None
if ChatterboxTTS is not None:
    try:
        tts = ChatterboxTTS()
        print("✅ Model loaded successfully!")
    except Exception as e:
        print(f"❌ Failed to load model: {e}")

class TTSRequest(BaseModel):
    input: str
    voice: str = "default"
    response_format: str = "mp3"

@app.post("/v1/audio/speech")
async def speech(request: TTSRequest):
    if tts is None:
        raise HTTPException(status_code=503, detail="TTS model not loaded")
    try:
        audio = tts.synthesize(request.input)
        buffer = io.BytesIO()
        sf.write(buffer, audio, 24000, format='mp3')
        buffer.seek(0)
        return Response(content=buffer.read(), media_type="audio/mpeg")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health():
    return {"status": "ok", "model_loaded": tts is not None}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
from pydantic import BaseModel
import io
import soundfile as sf
import numpy as np

# Правильний імпорт Chatterbox TTS
from chatterbox.tts import ChatterboxTTS

app = FastAPI()

print("Loading Norwegian TTS model...")
try:
    # Просто створюємо екземпляр – він сам завантажить модель
    # Модель підтримує норвезьку за замовчуванням
    tts = ChatterboxTTS()
    print("✅ Model loaded successfully!")
except Exception as e:
    print(f"❌ Failed to load model: {e}")
    tts = None

class TTSRequest(BaseModel):
    input: str
    voice: str = "default"
    response_format: str = "mp3"

@app.post("/v1/audio/speech")
async def speech(request: TTSRequest):
    if tts is None:
        raise HTTPException(status_code=503, detail="TTS model not loaded")
    try:
        # Генеруємо аудіо
        audio = tts.synthesize(request.input)
        
        # Конвертуємо в MP3
        buffer = io.BytesIO()
        sf.write(buffer, audio, 24000, format='mp3')
        buffer.seek(0)
        
        return Response(content=buffer.read(), media_type="audio/mpeg")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health():
    return {"status": "ok", "model_loaded": tts is not None}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
