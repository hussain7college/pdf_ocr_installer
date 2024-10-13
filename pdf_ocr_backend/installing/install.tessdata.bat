@echo off
echo ✨ installing tesseract trained data...
setlocal enabledelayedexpansion

:: This script will restart itself with admin rights
openfiles >nul 2>&1
if '%errorlevel%' NEQ '0' (
  echo "Requesting administrative privileges..."
  powershell -Command "Start-Process '%~f0' -Verb runAs"
  exit /b
)

set TESSDATA_PATH=C:\Program Files\Tesseract-OCR\tessdata
set TESSDATA_SOURCE_PATH=%~dp0tessdata

if not exist "%TESSDATA_PATH%" (
  echo "TESSDATA_PATH does not exist: %TESSDATA_PATH%"
  exit /b 1
)

if not exist "%TESSDATA_SOURCE_PATH%" (
  echo "TESSDATA_SOURCE_PATH does not exist: %TESSDATA_SOURCE_PATH%"
  exit /b 1
)

for /r "%TESSDATA_SOURCE_PATH%" %%f in (*.traineddata) do (
  set FILE=%%~nxf
  echo Copying !FILE! to %TESSDATA_PATH%\!FILE!
  copy /y "%%f" "%TESSDATA_PATH%\!FILE!"
)

echo "Done Successfully"