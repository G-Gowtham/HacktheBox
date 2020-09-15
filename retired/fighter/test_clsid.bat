@echo off
:: Starting port, you can change it
set /a port=10000
SETLOCAL ENABLEDELAYEDEXPANSION

FOR /F %%i IN (C:\windows\system32\spool\drivers\color\CLSID.list) DO (
   echo %%i !port!
   C:\windows\system32\spool\drivers\color\gg.exe -z -l !port! -c %%i >> C:\windows\system32\spool\drivers\color\result.log
   set RET=!ERRORLEVEL!
   :: echo !RET!
   if "!RET!" == "1"  set /a port=port+1
)
