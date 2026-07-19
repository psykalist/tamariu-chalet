@echo off
REM ============================================================
REM  Tamariu Chalet - upload site to web host via WinSCP
REM
REM  BEFORE FIRST USE:
REM    1. Open WinSCP, connect to your host as normal.
REM    2. Session > Sites > Save Session as Site...
REM       Give it the name:  tamariuchalet
REM       Tick "Save password" so the script can log in unattended.
REM    3. Check REMOTE_DIR below matches your web root on the server
REM       (often /public_html, /httpdocs, /www or /htdocs).
REM ============================================================

set SESSION=tamariuchalet
set LOCAL_DIR=%~dp0
set REMOTE_DIR=/public_html
set WINSCP="C:\Program Files (x86)\WinSCP\winscp.com"

if not exist %WINSCP% set WINSCP="C:\Program Files\WinSCP\winscp.com"
if not exist %WINSCP% (
  echo Could not find winscp.com - edit the WINSCP line in this file.
  pause
  exit /b 1
)

echo.
echo  Uploading site to %SESSION%%REMOTE_DIR%
echo.

%WINSCP% /log="%~dp0deploy.log" /ini=nul /command ^
    "open %SESSION%" ^
    "cd %REMOTE_DIR%" ^
    "lcd ""%LOCAL_DIR%""" ^
    "synchronize remote -criteria=time -filemask=""| _backups/; _originals/; .git/; *.py; *.docx; *.xlsx; *.log; *.bat; *.txt.bak; deploy.log""" ^
    "exit"

set RESULT=%ERRORLEVEL%
echo.
if %RESULT% neq 0 (
  echo  UPLOAD FAILED - see deploy.log for details.
) else (
  echo  Upload complete.
)
echo.
pause
exit /b %RESULT%
