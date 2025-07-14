# Flask EasyOCR API

Flask API สำหรับประมวลผล OCR (Optical Character Recognition) โดยใช้ EasyOCR

## การติดตั้ง

1. สร้าง virtual environment:
```bash
python -m venv venv
```

2. เปิดใช้ virtual environment:
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. ติดตั้ง dependencies:
```bash
pip install -r requirements.txt
```

## การรันโปรแกรม

```bash
python app.py
```

API จะรันที่ `http://localhost:5000`

## API Endpoints

### POST /api/v1/easy-ocr

ประมวลผล OCR จากรูปภาพที่ส่งมาในรูปแบบ base64

**Request Body:**
```json
{
    "imageBase64": "base64_encoded_image_string"
}
```

**Response (Success):**
```json
{
    "success": true,
    "data": {
        "full_text": "ข้อความที่อ่านได้ทั้งหมด",
        "results": [
            {
                "text": "ข้อความที่อ่านได้",
                "confidence": 0.95,
                "bbox": [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]
            }
        ],
        "total_detections": 1
    }
}
```

**Response (Error):**
```json
{
    "success": false,
    "error": "error_message"
}
```

### GET /health

ตรวจสอบสถานะของ API

**Response:**
```json
{
    "success": true,
    "message": "EasyOCR API is running",
    "supported_languages": ["en", "th"]
}
```

## ตัวอย่างการใช้งาน

```python
import requests
import base64

# อ่านไฟล์รูปภาพ
with open("image.jpg", "rb") as image_file:
    image_base64 = base64.b64encode(image_file.read()).decode('utf-8')

# ส่ง request ไปยัง API
response = requests.post(
    "http://localhost:5000/api/v1/easy-ocr",
    json={"imageBase64": image_base64}
)

result = response.json()
print(result)
```

## สนับสนุนภาษา

- อังกฤษ (en)
- ไทย (th)

สามารถเพิ่มภาษาอื่นได้โดยแก้ไขใน `app.py` ที่บรรทัด:
```python
reader = easyocr.Reader(['en', 'th'])  # เพิ่มภาษาที่ต้องการ
```
