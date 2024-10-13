from pytesseract import image_to_string, pytesseract
from sys import platform

# check if windows
print("Platform:", platform)
if platform == "win32":
    pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def img_to_text(img, lang="eng"):
    try:
        text = image_to_string(img, lang=lang)
        text = text.replace("‎", "")
        text = text.replace("‏", "")
        return text
    except Exception as e:
        print("❌❌❌", e)
        return False
    
# print(image_to_string("debug/page_0.png")) # OCR image