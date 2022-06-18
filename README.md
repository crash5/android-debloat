# Debloat Samsung


remove matching lines: grep -Fvxf B.txt A.txt


adb shell pm list packages > onphone.txt
adb shell pm list packages -d > onphone-disabled.txt
adb shell pm list packages -e > onphone-enabled.txt
adb shell pm list packages -s > onphone-system.txt


adb shell pm disable-user --user 0 <package>
adb shell pm enable --user 0 <package>

adb shell pm uninstall --user 0 <package>
adb shell pm install-existing --user 0 <package>

adb shell am force-stop --user 0 <package>

adb shell pm clear --user <user> <package>


https://github.com/0x192/universal-android-debloater/
https://github.com/khlam/debloat-samsung-android
https://www.alliancex.org/shield/apps.html
https://www.droidwin.com/debloat-remove-bloatware-from-samsung-devices-via-adb/

https://developer.android.com/studio/releases/platform-tools
https://docs.google.com/spreadsheets/d/12jEGQftFUL3vAI03X0Ku1LgoWFQKdwPA_WHuLh_2ics/edit#gid=0
  https://docs.samsungknox.com/CCMode/G991W_5G_R.pdf
  https://docs.samsungknox.com/CCMode/G928V_N.pdf

https://github.com/MuntashirAkon/AppManager


Google play url format: https://play.google.com/store/apps/details?id=flipboard.app


Settings?
adb shell settings put global online_manual_url 0
adb shell settings put system remote_control 0
adb shell settings put system sound_effects_enabled 0

adb shell settings put system air_motion_engine 0
adb shell settings put system air_motion_wake_up 0

adb shell settings put system mcf_continuity 0
adb shell settings put system mcf_continuity_permission_denied 1
adb shell settings put system mcf_permission_denied 1
