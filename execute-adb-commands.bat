FOR /F "tokens=*" %%i IN (own_uninstallnew.txt) DO (
    adb shell pm uninstall --user 0 %%i
)

FOR /F "tokens=*" %%i IN (own_disable.txt) DO (
    adb shell pm disable-user --user 0 %%i
    adb shell am force-stop %%i
)

set /p DUMMY=Hit ENTER to continue...
