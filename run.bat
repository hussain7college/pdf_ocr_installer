@echo off
:: check if pdf_ocr_backend and pdf_ocr_frontend folders exist
if not exist pdf_ocr_backend (
    echo 🚨 pdf_ocr_backend folder not found
    echo 🚨 Please run install.bat first
    exit /b  
)else if not exist pdf_ocr_frontend (
    echo 🚨 pdf_ocr_frontend folder not found
    echo 🚨 Please run install.bat first
    exit /b  
)

echo 🚀 Running Backend Server...
start "Backend Server" powershell -WindowStyle Hidden -Command "cd ./pdf_ocr_backend; ./run.bat"
echo   ✅ Backend Server is running

echo 🚀 Running Frontend Server...
start "Frontend Server" powershell -WindowStyle Hidden -Command "cd ./pdf_ocr_frontend; ./run.bat"
echo   ✅ Frontend Server is running

echo.
echo 🛜 You can open OCR PDF at http://localhost:1111
start http://localhost:1111
echo.

