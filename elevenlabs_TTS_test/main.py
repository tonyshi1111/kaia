from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs import play 
import os

load_dotenv()

elevenlabs = ElevenLabs(
  api_key=os.getenv("ELEVENLABS_API_KEY"),
)

audio = elevenlabs.text_to_speech.convert(
    text="Hi! I'm Kaia, your personal assistant. I'm here to help you with your daily tasks and make your life easier. What would you like to do?",
    voice_id="JBFqnCBsd6RMkjVDRZzb",
    model_id="eleven_multilingual_v2",
    output_format="mp3_44100_128",
)

play(audio)
