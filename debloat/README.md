# Debloat Android

- Platform tools: https://developer.android.com/tools/releases/platform-tools
- USB drivers: https://developer.android.com/studio/run/win-usb
    - OEM drivers: https://developer.android.com/studio/run/oem-usb#Drivers
- uad_lists.json: https://github.com/Universal-Debloater-Alliance/universal-android-debloater-next-generation/tree/main/resources/assets


```bash
adb shell pm list packages > ondevice.txt
adb shell pm list packages -d > ondevice-disabled.txt
adb shell pm list packages -e > ondevice-enabled.txt
adb shell pm list packages -s > ondevice-system.txt


adb shell pm disable-user --user 0 <package>
adb shell am force-stop --user 0 <package>

adb shell pm enable <package>

# Keep the data and cache directories after removal
adb shell pm uninstall -k --user 0 <package>

adb shell pm uninstall --user 0 <package>
adb shell pm install-existing --user 0 <package>


adb shell pm clear --user <user> <package>
```


remove matching lines: grep -Fvxf B.txt A.txt


https://www.alliancex.org/shield/apps.html

https://docs.google.com/spreadsheets/d/12jEGQftFUL3vAI03X0Ku1LgoWFQKdwPA_WHuLh_2ics/edit#gid=0
  https://docs.samsungknox.com/CCMode/G991W_5G_R.pdf
  https://docs.samsungknox.com/CCMode/G928V_N.pdf

https://github.com/MuntashirAkon/AppManager
