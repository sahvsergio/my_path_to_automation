import subprocess
import plyer
from plyer.facades import TTS


class UbuntuTTS(TTS):
    def _speak(self, message, speed=150, language='en-us'):
        subprocess.run(['espeak', '-s', str(speed), '-v', language,  message])


tts = UbuntuTTS()
