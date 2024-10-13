@echo off

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

