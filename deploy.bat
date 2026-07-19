@echo off
REM ============================================================
REM  Tamariu Chalet - upload site to web host via WinSCP
REM
REM  BEFORE FIRST USE:
REM    1. Open WinSCP, connect to your host as normal.
REM    2. Session > Sites > Save Session as Site...
REM       Give it the name:  tamariuchalet.com
REM       Tick "Save password" so the script can log in unattended.
REM    3. Check REMOTE_DIR below matches your web root on the server
REM       (often /public_html, /httpdocs, /www or /htdocs).
REM       Port, host key and credentials all come from the saved site,
REM       so nothing sensitive lives in this file. iFastNet uses SFTP
REM       on port 1394, not the default 22.
REM
REM  WHAT GETS UPLOADED:
REM    Everything except the notes/ folder and the dev files listed in
REM    the filemask below. notes/ holds documentation, backups, source
REM    images and scripts that the live site does not need.
REM    Files that MUST stay at the root and DO go up:
REM      77cddc...txt  - IndexNow verification key
REM      sitemap.xml, robots.txt, favicon.*, site.webmanifest
REM    sync-bookings.py stays at root for the GitHub Action, but is
REM    excluded from upload by the *.py mask.
REM ============================================================

set SESSION=tamariuchalet.com
set PORT=1394
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

%WINSCP% /log="%~dp0deploy.log" /command ^
    "open %SESSION% -rawsettings PortNumber=%PORT%" ^
    "cd %REMOTE_DIR%" ^
    "lcd ""%LOCAL_DIR%""" ^
    "synchronize remote -criteria=time -filemask=""| notes/; .git/; .github/; .well-known/; *.py; *.docx; *.xlsx; *.log; *.bat; *.exe; *.txt.bak; README.md; CLAUDE.md; .gitignore; .cpanel.yml""" ^
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
