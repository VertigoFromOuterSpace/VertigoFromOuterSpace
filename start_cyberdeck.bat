@echo off
title CYBERDECK - Vertigo From Outer Space
color 0A

echo.
echo  ╔═══════════════════════════════════════════════════════════════╗
echo  ║  ██╗   ██╗███████╗██████╗ ████████╗██╗ ██████╗  ██████╗       ║
echo  ║  ██║   ██║██╔════╝██╔══██╗╚══██╔══╝██║██╔════╝ ██╔═══██╗      ║
echo  ║  ██║   ██║█████╗  ██████╔╝   ██║   ██║██║  ███╗██║   ██║      ║
echo  ║  ╚██╗ ██╔╝██╔══╝  ██╔══██╗   ██║   ██║██║   ██║██║   ██║      ║
echo  ║   ╚████╔╝ ███████╗██║  ██║   ██║   ██║╚██████╔╝╚██████╔╝      ║
echo  ║    ╚═══╝  ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝  ╚═════╝       ║
echo  ║                                                               ║
echo  ║            FROM OUTER SPACE :: CYBERDECK v3.14               ║
echo  ╚═══════════════════════════════════════════════════════════════╝
echo.

echo [1] Cyberdeck Dashboard
echo [2] Auto GitHub Update
echo [3] Demo Completo
echo [4] Instruções
echo [Q] Sair
echo.

set /p choice="Escolha uma opção [1-4/Q]: "

if /i "%choice%"=="1" (
    .venv\Scripts\python.exe tools\cyberdeck.py
) else if /i "%choice%"=="2" (
    .venv\Scripts\python.exe tools\auto_github.py
) else if /i "%choice%"=="3" (
    .venv\Scripts\python.exe tools\cyberdeck.py --demo
    pause
) else if /i "%choice%"=="4" (
    start tools\INSTRUCTIONS.md
) else if /i "%choice%"=="Q" (
    echo.
    echo 👾 CYBERDECK DISCONNECTED 👾
    timeout /t 2 >nul
    exit
) else (
    echo.
    echo ❌ Opção inválida!
    timeout /t 2 >nul
    goto start
)

:start
start_cyberdeck.bat
