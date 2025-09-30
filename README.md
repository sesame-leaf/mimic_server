python -m venv .venv

.venv\Scripts\activate.bat

pip install -r requirements
or
pip install fastapi[standard] pydantic diffusers transformers accelerate scipy safetensors torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu126


fastapi dev server.py