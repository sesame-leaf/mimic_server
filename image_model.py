import torch
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
import os

os.chdir("./images")

image = None
model_id = "stabilityai/stable-diffusion-2-1"

# Use the DPMSolverMultistepScheduler (DPM-Solver++) scheduler here instead
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
pipe = pipe.to("cuda")


def generate_image(prompt: str):
    global image
    image = pipe(prompt).images[0]


def save_image(path: str) -> None:
    global image
    image.save(path)


def main():
    print("generating")
    generate_image("astronaut riding a horse")
    print("saving")
    save_image("astronaut_rides_horse.png")


if __name__ == "__main__":
    print("starting")
    main()
