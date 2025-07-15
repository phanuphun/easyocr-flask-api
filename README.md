# EasyOCR Flask API
- [EasyOCR]("https://github.com/JaidedAI/EasyOCR")

## Installation and setup
- Create virtual environment : `python -m venv env`
- Activate venv : `.\env\Scripts\activate`
- Install dependencies : `pip install -r requirements.txt`
- Run Application : `python app.py`
- Server runs at `http://localhost:7757`

## Notes 
- Check Nvidia CUDA driver version : `nvidia-smi`
- Check Cuda compiler version : `nvcc --version`

## CUDA Testing Compatible

### CUDA 12.9
- python version : `3.12.8`
- touch version : latest version from easy ocr auto install
- result : it's work

### CUDA 11.4 : (Test 1)
- image version: `nvidia/cuda:11.4.3-base-ubuntu20.04`
- python version: `3.10`
- easyOCR version: `1.7.2`
- touch version:
    - --extra-index-url https://download.pytorch.org/whl/cu113
    - torch==1.12.1+cu113
    - torchvision==0.13.1+cu113
    - torchaudio==0.12.1+cu113
- result: EasyOCR(`1.7.2`) using `touch.load()` but in touch(`1.12.1+cu113`) is not have argument `weights_only` in function 

