from flask import Flask, request, jsonify
import easyocr
import base64
import io
from PIL import Image
import numpy as np
import cv2
from config import Config
from datetime import datetime
import time

app = Flask(__name__)
app.config.from_object(Config)
 

# Initialize EasyOCR reader with configurable languages

@app.route('/', methods=['GET'])
def health_check():
    return jsonify({
        'api': 'EasyOCR API',
        'version': '1.0.0',
        'status': 'Running',
        'timestamp': datetime.now().astimezone().isoformat()
    }), 200

@app.route('/api/v1/easy-ocr', methods=['POST'])
def ocr_process():
    try:
        data = request.get_json()
        lang = data.get('lang', None)
        if not data or 'img' not in data:
            return jsonify(success=False, error='Missing img parameter'), 400
        
        if lang == 'en':
            langs = ['en']
        elif lang == 'th':
            langs = ['th']
        else:
            langs = ['en', 'th']

        start_time = time.perf_counter()
        print(f"Processing OCR for languages: {langs}")
        reader = easyocr.Reader(langs,True)

        # Decode base64 เป็น bytes แล้วเปิดด้วย PIL
        image_bytes = base64.b64decode(data['img'])
        image = Image.open(io.BytesIO(image_bytes))
        image_np = np.array(image)
        if image_np.ndim == 3:
            image_np = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

        # เรียก EasyOCR
        results = reader.readtext(image_np)

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
    app.run(debug=True, port=7756)