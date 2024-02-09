import logging
import warnings

# All
warnings.filterwarnings("ignore")

import whisper

logger = logging.getLogger(__name__)


def transcribe(filename: str, model="tiny.en") -> str:
    model: whisper.Whisper = whisper.load_model(model)
    try:
        result = model.transcribe(filename, language="en")
        logger.debug(result)
        return result.get("text", "").strip()
    except Exception as e:
        logger.error(f"Got exception {e}", e)
        return ""


if __name__ == '__main__':
    rc = transcribe("https://dd.prod.captcha-delivery.com/audio/2024-02-09/en/aaefe2be939c8af3ed6192bd8bf1c7d5.wav")
    #rc = transcribe("https://dd.prod.captcha-delivery.com/audio/2024-02-09/en/d24a25be9858e582f6df703a576482d7.wav")
    print(rc)
