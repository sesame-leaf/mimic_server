from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel

# from image_model import generate_image, save_image


# Class Definitions
class ResponseStatus(Enum):
    IMAGE_GENERATING: int = 0
    IMAGE_GENERATION_SUCCESS: int = 1
    IMAGE_GENERATION_FAILED: int = 2
    EMPTY_PROMPT: int = 3


class PromptRequest(BaseModel):
    prompt: str | None = None


class ImageResponse(BaseModel):
    response: ResponseStatus
    image: bytes | None = None


# Constants
ROOT_SAVE_PATH: str = r"C:\Users\user\Desktop\dAiv_Ai_Mimic_Challenge"


# Global Variables
generating_image: bool = False
image_counter: int = 0
app = FastAPI()


@app.post("/")
async def image_generation_response(request: PromptRequest):
    global generating_image, image_counter
    if generating_image:
        return {"response": ResponseStatus.IMAGE_GENERATING}
    
    if request.prompt is None:
        return {"response": ResponseStatus.EMPTY_PROMPT}
    
    generating_image = True

    try:
        # generate_image(request.prompt)
        # save_image(f"{ROOT_SAVE_PATH}\\{image_counter}.png")
        pass
    except:
        generating_image = False
        return {"response": ResponseStatus.IMAGE_GENERATION_FAILED}
    
    image_counter += 1
    generating_image = False
    print(image_counter)
    return {"response": ResponseStatus.IMAGE_GENERATION_SUCCESS}
