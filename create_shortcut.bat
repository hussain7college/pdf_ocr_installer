@echo off
setlocal

:: Set the name for the shortcut
set shortcutName=PDF OCR
set shortcutPath=%USERPROFILE%\Desktop\%shortcutName%.lnk

:: Get the current directory (where the script is running)
set currentDir=%~dp0

:: Set the target path for the run.bat script and icon path
set targetPath=%currentDir%run.bat
set iconPath=%currentDir%favicon.ico

:: Create the shortcut
powershell "$ws = New-Object -ComObject WScript.Shell; $s = $ws.CreateShortcut('%shortcutPath%'); $s.TargetPath = '%targetPath%'; $s.IconLocation = '%iconPath%'; $s.Save()"

endlocal
