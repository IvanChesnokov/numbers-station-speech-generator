@echo off
echo Administrative permissions required. Detecting permissions...
net session >nul 2>&1
    if %errorLevel% == 0 (
        echo Success: Administrative permissions confirmed. 
        @"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
        refreshenv
		choco install python
		pip install datetime
		pip install	pyqt5
		pip install pydub
		echo ...
		echo Installation of dependencies complete. Press Enter to exit.
        pause >nul
    ) else (
        echo Failure: Current permissions inadequate. Run as Administrator. Press Enter to exit.
        pause >nul
    )