from flask import Flask, request, jsonify
import easyocr
import base64
from config import Config
from datetime import datetime
import time

app = Flask(__name__)
app.config.from_object(Config)
PORT = 7757
HOST= '0.0.0.0'

import torch
print(f'----------------------------------------------------------------------------')
print(f'Is CUDA available? {torch.cuda.is_available()}')       # ควรได้ True
print(f'----------------------------------------------------------------------------')

# print(f'CUDA version: {torch.version.cuda}')
# print(f'Number of GPUs: {torch.cuda.device_count()}')       # จำนวน GPU ที่ตรวจพบ
# print(f'GPU name: {torch.cuda.get_device_name(0)}')   # ชื่อการ์ดจอ

# Initialize EasyOCR reader with configurable languages

@app.route('/', methods=['GET'])
def health_check():
    return jsonify({
        'api': 'EasyOCR API',
        'version': '1.0.0',
        'status': 'Running',
        'timestamp': datetime.now().astimezone().isoformat()
    }), 200

@app.route('/api/v1/ocr', methods=['POST'])
def ocr_process():
    try:
        data = request.get_json()
        langs = data.get('langs')
        allowed = {'en', 'th'}
        
        if not data or 'img' not in data:
            return jsonify(success=False, error='Missing img parameter'), 400
        
        if not isinstance(langs, list):
            return jsonify(success=False, error='langs must be a list'), 400
        
        if any(lang not in allowed for lang in langs):
            return jsonify(success=False, error='Invalid language code'), 400

        start_time = time.perf_counter()
        print(f"Processing OCR for languages: {langs}")

        # ***
        reader = easyocr.Reader(lang_list=langs, gpu=True)
        image_bytes = base64.b64decode(data['img'])
        results = reader.readtext(image_bytes)

        end_time = time.perf_counter()
        duration = end_time - start_time

        ocr_results = []
        full_text = ""

        for bbox, text, confidence in results:
            # แปลง bbox ให้เป็น Python list of int
            bbox_py = [[int(x), int(y)] for x, y in bbox]

            ocr_results.append({
                'text': text,
                'confidence': float(confidence),
                'bbox': bbox_py
            })
            full_text += text + " "

        return jsonify ({
            'ok':1,
            'text': full_text.strip(),
            'duration': duration,
        }), 200

    except Exception as e:
        return jsonify(success=False, error=str(e)), 500


if __name__ == '__main__':
    print("Starting EasyOCR API...")
    app.run(debug=True, port=PORT , host=HOST)