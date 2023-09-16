import subprocess
import plyer
from plyer.facades import TTS

commands={
    'file-started':'the bot was started',
    'directories-created':'the folders are being created',
    'folder-success':'the folders were created successfully'
}


class UbuntuTTS(TTS):
    def _speak(self, message, speed=150, language='en-us'):
        subprocess.run(['espeak', '-s', str(speed), '-v', language,  message])


tts = UbuntuTTS()
