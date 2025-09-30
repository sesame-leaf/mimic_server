from enum import Enum
import time
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
import mimetypes
import base64

from image_model import generate_image, save_image


# Class Definitions
class ResponseStatus(Enum):
    IMAGE_GENERATING: int = 0
    IMAGE_GENERATION_SUCCESS: int = 1
    IMAGE_GENERATION_FAILED: int = 2
    EMPTY_PROMPT: int = 3


class RequestModel(BaseModel):
    prompt: str | None = None


class ResponseModel(BaseModel):
    response_state: int | None = None


# Constants
ROOT_SAVE_PATH: str = r"C:\Users\user\Desktop\dAiv_Ai_Mimic_Challenge"


# Global Variables
generating_image: bool = False
app = FastAPI()


@app.post("/")
async def image_generation_response(request: RequestModel):
    global generating_image

    if generating_image:
        return ResponseModel(response_state=ResponseStatus.IMAGE_GENERATING)
    
    if request.prompt is None:
        return ResponseModel(response_state=ResponseStatus.EMPTY_PROMPT)
    
    generating_image = True

    try:
        image_name: str = str(int(time.time())) + ".png"
        generate_image(request.prompt)
        save_image(f"{ROOT_SAVE_PATH}/{image_name}")
        save_image(f"images/{image_name}")
    except:
        generating_image = False
        return ResponseModel(response_state=ResponseStatus.IMAGE_GENERATION_FAILED)
    
    ###############주소 넣어줘####################
    file_path = f"images/{image_name}"

    with open(file_path, "rb") as image_file:
        contents = image_file.read()

    mime_type, _ = mimetypes.guess_type(file_path)
    if mime_type is None:
        mime_type = "application/octet-stream"

    base64_image = base64.b64encode(contents).decode('utf-8')

    ###################################
    
    generating_image = False
    return {"mime_type": mime_type, "base64_image": base64_image}
