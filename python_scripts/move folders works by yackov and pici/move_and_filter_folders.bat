@echo off
setlocal

rem Set the default destination path
set "DESTINATION_PATH=D:\OwnerData2\Documents\old_runs"

rem Navigate to the python_scripts directory
cd /d "%~dp0python_scripts"

rem Run the Python script with the default destination path
python move_and_filter_folders.py "%DESTINATION_PATH%"

endlocal
pause
