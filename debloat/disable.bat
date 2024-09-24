FOR /F "tokens=*" %%i IN (disable.txt) DO (
    adb shell pm disable-user --user 0 %%i
    adb shell am force-stop %%i
)

set /p DUMMY=Hit ENTER to continue...
