@echo off
echo ✨ Installing Virtual Environment...
pip install virtualenv >nul 2>&1
cd ..
python -m venv venv
echo   💻 Activating Virtual Environment...
call venv\Scripts\activate
echo ✨ Installing Python Libraries...
pip install flask >nul 2>&1
echo   ➕ flask
pip install flask-cors >nul 2>&1
echo   ➕ flask-cors
pip install werkzeug >nul 2>&1
echo   ➕ werkzeug
pip install pytesseract >nul 2>&1
echo   ➕ pytesseract
pip install PyMuPDF >nul 2>&1
echo   ➕ PyMuPDF
pip install pillow >nul 2>&1
echo   ➕ pillow
cd installing