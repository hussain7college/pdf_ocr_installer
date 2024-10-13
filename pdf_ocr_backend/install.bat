@echo off
echo ✨ installing dependencies...
cd .\installing
call .\install.checkdeps.bat
call .\install.tessdata.bat
call .\install.libs.bat
