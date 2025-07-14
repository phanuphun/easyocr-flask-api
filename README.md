# EasyOCR Flask API

A simple Flask API for testing EasyOCR functionality. This project is just for basic experimentation with EasyOCR.

## Quick Start

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the server:
```bash
python app.py
```

Server runs at `http://localhost:5000`

## API Usage

### POST `/api/v1/easy-ocr`
Extract text from image (base64 format)

**Request:**
```json
{
    "imageBase64": "your_base64_image_string"
}
```

**Response:**
```json
{
    "ok":1,
    "text":"....",
    "duraton":10.000000
}
```
