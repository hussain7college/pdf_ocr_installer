import os
import datetime
from sys import platform
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from werkzeug.utils import secure_filename
from pdf2img import pdf_to_images
from img2text import img_to_text

app = Flask(__name__)

# Apply CORS to your app
CORS(app)

UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'outputs'
DONE_FOLDER = 'done'
DEBUG_FOLDER = 'debug'
ALLOWED_EXTENSIONS = {'pdf'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER
app.config['DONE_FOLDER'] = DONE_FOLDER
app.config['DEBUG_FOLDER'] = DEBUG_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def ocr_file(input_file, output_file, lang="eng"):
    error_pages = []
    images = pdf_to_images(input_file)
    ocr_text = ""

    for idx, img in enumerate(images):
        img.save(f"debug/page_{idx}.png")  # save image for debugging
        ocr_result = img_to_text(img, lang)
        if ocr_result:
            ocr_text += ocr_result + f"\n------------📄 Page ({idx+1}) 📄------------\n"
        else:
            ocr_text += f"\n❌❌❌ Error processing page ({idx+1}) ❌❌❌\n"
            error_pages.append(idx+1)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(ocr_text)
    
    return error_pages

def rename_unique(path):
    name, ext = os.path.splitext(path)
    return name + "-" + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ext

def create_directories():
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)
    os.makedirs(app.config['DONE_FOLDER'], exist_ok=True)
    os.makedirs(app.config['DEBUG_FOLDER'], exist_ok=True)

def generate_unique_filename_name(filename):
    name, ext = os.path.splitext(filename)
    return name + "-" + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

def checkTessData(lang):
    # example C:\\Program Files\\Tesseract-OCR\tessdata\ara.traineddata
    # check if language has + then make it array
    langsArr = lang.split("+")
    for singleLang in langsArr:
        if platform == "win32":
            tessdata_lang_path = r"C:\\Program Files\\Tesseract-OCR\tessdata\\" + singleLang + ".traineddata"
            if not os.path.exists(tessdata_lang_path):
                return False
    return True

@app.route('/')
def home():
    return jsonify({"message": "Welcome to OCR API"}), 200

# Upload a file and get the OCR text
@app.route('/outputs', methods=['POST'])
def upload_file():
    print("request", request)
    if 'files' not in request.files:
        return jsonify({"error": "No files part"}), 400
    
    files = request.files.getlist('files')
    lang = request.form.get('lang', 'eng')
    if not checkTessData(lang):
        return jsonify({"error": "Language not supported"}), 400
    results = []

    for file in files:
        if file.filename == '':
            continue
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            
            new_filename_name = generate_unique_filename_name(filename)
            output_filename = new_filename_name + ".txt"
            output_path = os.path.join(app.config['OUTPUT_FOLDER'], output_filename)
            
            error_pages = ocr_file(file_path, output_path, lang)
            os.rename(file_path, os.path.join(app.config['DONE_FOLDER'], new_filename_name + ".pdf"))
            
            results.append({
                "input_file": filename,
                "output_file": output_filename,
                "error_pages": error_pages
            })
        else:
            results.append({
                "input_file": file.filename,
                "error": "Invalid file format"
            })

    if not results:
        return jsonify({"error": "No valid files uploaded"}), 400

    return jsonify(results), 200

@app.route('/outputs/<filename>', methods=['GET'])
def download_file(filename):
    file_path = os.path.join(app.config['OUTPUT_FOLDER'], filename)
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    return jsonify({"error": "File not found"}), 404

@app.route('/outputs', methods=['GET'])
def get_outputs():
    files = os.listdir(app.config['OUTPUT_FOLDER'])
    return jsonify(files), 200

@app.route('/clean', methods=['POST'])
def clean_files():
    for folder in [app.config['UPLOAD_FOLDER'], app.config['OUTPUT_FOLDER'], app.config['DONE_FOLDER'], app.config['DEBUG_FOLDER']]:
        for file in os.listdir(folder):
            os.remove(os.path.join(folder, file))
    return jsonify({"message": "All files cleaned"}), 200

@app.route('/outputs/<filename>', methods=['DELETE'])
def delete_output(filename):
    file_path = os.path.join(app.config['OUTPUT_FOLDER'], filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        return jsonify({"message": "File deleted"}), 200
    return jsonify({"error": "File not found"}), 404

if __name__ == '__main__':
    create_directories()
    app.run(host='0.0.0.0', port=1112)
