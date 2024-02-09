import logging
import os
import time
import uuid
from pydantic import BaseModel
# import warnings
# warnings.filterwarnings("ignore")
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from .whisper_wrapper import transcribe

logger = logging.getLogger()
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%H:%M:%S %p')
logger.setLevel(logging.INFO)


app = FastAPI(title="Whisper wrapper", description="Simple wrapper for Whisper model")


@app.exception_handler(Exception)
async def unicorn_exception_handler(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"message": f"Oops! {str(exc)}..."},)


class CaptchaInfo(BaseModel):
    model:str = "tiny.en"
    url: str



class CaptchaResponse(BaseModel):
    text: str = ""
    elapsed: float = 0.0


@app.post("/captcha/text")
async def audio_2_text(info:CaptchaInfo) -> CaptchaResponse:
    t0 = time.time()
    res = CaptchaResponse(text=transcribe(info.url, model=info.model), elapsed=round(time.time() - t0,2))
    return res
