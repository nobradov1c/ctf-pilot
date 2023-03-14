# Android

- [PhoneSploit-Pro](https://github.com/AzeemIdrisi/PhoneSploit-Pro) - remotely exploit

- [forensics](../forensics/android.md)

## apk adb tools

- install app
  - `adb -s emulator-5554 install .\zero.apk`
- start an app + activity

  - `adb shell am start -n com.hellocmu.picoctf/com.hellocmu.picoctf.MainActivity`

- logs

  - https://developer.android.com/studio/command-line/logcat
  - adb logcat

        adb -d logcat <your package name>:<log level> *:S

        -d denotes an actual device and -e denotes an emulator. If there's more than 1 emulator running you can use -s emulator-<emulator number> (eg, -s emulator-5558)

        Example: adb -d logcat com.example.example:I \*:S


        Or if you are using System.out.print to send messages to the log you can use adb -d logcat System.out:I *:S to show only calls to System.out.



        - `adb -e logcat com.hellocmu.picoctf`

## rev

- [apktool](https://github.com/iBotPeaches/Apktool) - a tool for reverse engineering Android apk files
- [bytecode-viewer](https://github.com/Konloch/bytecode-viewer) - A Java 8+ Jar & Android APK Reverse Engineering Suite (Decompiler, Editor, Debugger & More)
