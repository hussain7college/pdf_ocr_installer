@echo off

where node >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ Node.js is installed
) else (
    echo ❌ Node.js is not installed. Please install Node.js from https://nodejs.org/
    exit /b 1
)

where pnpm >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ pnpm is installed
) else (
    echo ❌ pnpm is not installed
    echo ✨ Installing pnpm...
    npm install -g pnpm
    corepack enable pnpm
)
pnpm install