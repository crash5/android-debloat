# ALLDOCUBE iPlay 50 Pro

https://androidmtk.com/install-xml-scatter-firmware-mediatek


## First time:

adb reboot bootloader

fastboot flashing unlock

fastboot reboot fastboot

fastboot erase system
fastboot flash system system.img

fastboot -w

fastboot reboot


## Updates:

adb reboot fastboot
fastboot flash system system.img
fastboot reboot

---

$ fastboot erase system
Erasing 'system_a'                                 OKAY [  0.086s]
Finished. Total time: 0.098s


$ fastboot flash system lineage-20.0-20230716-UNOFFICIAL-arm64_bgN.img

Resizing 'system_a'                                OKAY [  0.005s]
Sending sparse 'system_a' 1/11 (262112 KB)         OKAY [  6.290s]
Writing 'system_a'                                 OKAY [  1.665s]
Sending sparse 'system_a' 2/11 (262116 KB)         OKAY [  6.218s]
Writing 'system_a'                                 OKAY [  1.684s]
Sending sparse 'system_a' 3/11 (262112 KB)         OKAY [  6.208s]
Writing 'system_a'                                 OKAY [  1.675s]
Sending sparse 'system_a' 4/11 (262124 KB)         OKAY [  6.130s]
Writing 'system_a'                                 OKAY [  1.696s]
Sending sparse 'system_a' 5/11 (262128 KB)         OKAY [  6.230s]
Writing 'system_a'                                 OKAY [  1.670s]
Sending sparse 'system_a' 6/11 (262112 KB)         OKAY [  6.090s]
Writing 'system_a'                                 OKAY [  1.665s]
Sending sparse 'system_a' 7/11 (262128 KB)         OKAY [  6.115s]
Writing 'system_a'                                 OKAY [  1.680s]
Sending sparse 'system_a' 8/11 (262084 KB)         OKAY [  6.200s]
Writing 'system_a'                                 OKAY [  1.690s]
Sending sparse 'system_a' 9/11 (262124 KB)         OKAY [  6.185s]
Writing 'system_a'                                 OKAY [  1.690s]
Sending sparse 'system_a' 10/11 (262140 KB)        OKAY [  6.125s]
Writing 'system_a'                                 OKAY [  1.695s]
Sending sparse 'system_a' 11/11 (58668 KB)         OKAY [  1.436s]
Writing 'system_a'                                 OKAY [  0.655s]
Finished. Total time: 88.845s
