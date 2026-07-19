@echo off
REM ============================================================
REM  Tamariu Chalet - upload site to web host via WinSCP
REM
REM  HOW IT LOGS IN:
REM    Connects as tamariuc over SFTP on port 1394 and prompts for the
REM    password once per run. No password is stored in this file.
REM
REM    This previously pointed at a saved WinSCP site called
REM    "tamariuchalet.com" that was never actually created, so WinSCP fell
REM    back to treating the name as a bare hostname with no credentials and
REM    every run died with "Credentials were not specified".
REM
REM    To run unattended instead: in WinSCP do Session > Sites > Save Session
REM    as Site, name it tamariuchalet.com, tick "Save password", then set
REM    SESSION=tamariuchalet.com below.
REM
REM  REMOTE_DIR - IMPORTANT:
REM    This hosting account also serves harryhallcycles.co.uk, intelteck.com,
REM    dorchestercourt.uk, park-view-cheltenham.com and 2southville.com.
REM    /home/tamariuc/public_html is the Tamariu Chalet web root. Do not
REM    change it without checking, or the site uploads over another domain.
REM    Note it is /home/tamariuc/public_html, not /public_html - the SFTP
REM    root is the real filesystem root, so the short path does not exist.
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

set SESSION=sftp://tamariuc@tamariuchalet.com:1394/
set LOCAL_DIR=%~dp0
set REMOTE_DIR=/home/tamariuc/public_html
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
    "open %SESSION%" ^
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
