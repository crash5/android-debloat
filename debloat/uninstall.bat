FOR /F "tokens=*" %%i IN (uninstall.txt) DO (
    adb shell pm uninstall --user 0 %%i
)

set /p DUMMY=Hit ENTER to continue...
