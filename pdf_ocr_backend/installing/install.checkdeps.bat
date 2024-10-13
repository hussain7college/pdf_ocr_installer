@echo off
echo ✨ check installed dependencies...

setlocal enabledelayedexpansion

set TESSERACT_PATH=C:\Program Files\Tesseract-OCR\tesseract.exe

if not exist "%TESSERACT_PATH%" (
  echo ❌ Tesseract does not exist, please install Tesseract OCR from https://github.com/UB-Mannheim/tesseract/releases/download/v5.4.0.20240606/tesseract-ocr-w64-setup-5.4.0.20240606.exe
) else (
  echo ✅ Tesseract exists
)

set PYTHON_PATH=C:\Users\%USERNAME%\AppData\Local\Programs\Python

if not exist "%PYTHON_PATH%" (
  echo ❌ Python does not exist, please install Python from https://www.python.org/downloads/
) else (
  echo ✅ Python exists
)

