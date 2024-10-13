import fitz  # PyMuPDF
from PIL import Image

def pdf_to_images(pdf_path):
    print("📄📄📄 Converting PDF to images... 📄📄📄")
    images = []
    pdf_document = fitz.open(pdf_path)
    for page_number in range(pdf_document.page_count):
        try:
            print(f"📄📄📄 Converting image page ({page_number}) of ({pdf_document.page_count})")
            page = pdf_document[page_number]
            image = page.get_pixmap()
            # Convert the image to a PIL Image object
            pil_image = Image.frombytes("RGB", [image.width, image.height], image.samples)
            images.append(pil_image)
        except Exception as e:
            print(f"❌❌❌ Error converting image page ({page_number}) ❌❌❌")
            print(e)
            continue
    pdf_document.close()
    return images

if __name__ == "__main__":
    pdf_file_path = "D:\Projects\OCR\multi ocr\in\input.pdf"  # Path to the input PDF file
    output_folder_path = "out"  # Folder to save the output images
    
    print(pdf_to_images(pdf_file_path))
