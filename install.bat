@echo off

echo ✨ Decompressing Project... ✨
:: unzip pdf_ocr_backend.zip and replace
echo   🗃️ unzipping pdf_ocr_backend.zip...
powershell -command "Expand-Archive -Path .\pdf_ocr_backend.zip -DestinationPath .\ -Force"

:: unzip pdf_ocr_frontend.zip and replace
echo   🗃️ unzipping pdf_ocr_frontend.zip...
powershell -command "Expand-Archive -Path .\pdf_ocr_frontend.zip -DestinationPath .\ -Force"

echo ✨ Installing Project... ✨
echo   💿 installing Frontend...
cd .\pdf_ocr_frontend
call .\install.bat

echo   💿 installing Backend...
cd ..\pdf_ocr_backend
call .\install.bat
