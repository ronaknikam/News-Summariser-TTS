
from gtts import gTTS
import os

def generate_tts(text, index):
    """Converts text to Hindi speech using gTTS and saves the file."""
    output_path = f"tts_output_{index}.mp3"  # Unique filename for each article
    tts = gTTS(text=text, lang="hi")
    tts.save(output_path)
    return output_path  # Return the path of the generated audio file

