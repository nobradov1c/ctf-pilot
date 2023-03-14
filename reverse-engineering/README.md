# Reverse Engineering

## quick tools

- `file`
- `strings`
- `xxd` hex view
- `objdump -x` Show all headers
- `objdump -d/D` Disassemble
- `strace`
- `ltrace`

## Disassemblers and debugers

- IDA, Ghidra, gdb, edb
- if they don't work try Cutter
- ILSpy, dnSpy, dotPeek
- [ollydbg1](https://www.ollydbg.de/)
- [ollydbg2](https://www.ollydbg.de/version2.html)
- [x64dbg](https://x64dbg.com/) - an open-source x64/x32 debugger for windows

- tips:

  - edb and Cutter can show hexdumps next to disassembly, look for parameters to function calls

  ### multipurpose

  - https://ide.kaitai.io/ - [kaitai](http://kaitai.io/)
  - https://cerbero.io/ - [tutorials](https://cerbero.io/resources/)

  ### tools for elf files

  - https://github.com/horsicq/XELFViewer

  ### tools for PE (windows)

  - https://github.com/Washi1337/AsmResolver

  ### .NET [dotnet, mono]

  - [ILSpy](https://github.com/icsharpcode/ILSpy)
  - [dotPeek](https://www.jetbrains.com/decompiler/)
  - [dnSpy - revived](https://github.com/dnSpyEx/dnSpy) - Unofficial revival of the well known .NET debugger and assembly editor, dnSpy
  - [RunDotNetDll](https://github.com/enkomio/RunDotNetDll) - a simple utility to list all methods of a given .NET Assembly and to invoke them

  - [dnSpy, archived](https://github.com/dnSpy/dnSpy) - .NET debugger and assembly editor
    - can debug and edit binaries
  - [dnSpy unity, archived](https://github.com/dnSpy/dnSpy-Unity-mono) - Fork of Unity mono that's used to compile mono.dll with debugging support enabled

## Packing

- [PEiD](https://www.aldeid.com/wiki/PEiD)\
  - detects most common packers, cryptors and compilers for PE files
- [UPX](https://github.com/upx/upx)
  - `upx -d cake.exe`
    - sometimes before unpacking with UPX you must disable the ASLR: `setdllcharacteristics -d cake.exe`, unpacked program might not run without this (for debugging) like cake.exe for example (chall from HTB)

## gdb [cheat sheet](./gdb.md)

- `gdb -q <program> [core dump]`

## fuzzing

- manipulate the binary so it still executes, but a debugger can't open it
  - [example script, random, inefficient and dumb way](/other/python/scripts/reverse-engineering/elf-fuzzer.py)
  - [Melkor ELF Fuzzer](https://github.com/IOActive/Melkor_ELF_Fuzzer)
  - [elf specs 1](https://refspecs.linuxfoundation.org/elf/elf.pdf)
  - [elf specs 2](https://www.cs.cmu.edu/afs/cs/academic/class/15213-f00/docs/elf.pdf)

## Assembly

- [intel x86 manual](https://ost2images.s3.amazonaws.com/Arch2001/CourseMaterials/325462-sdm-vol-1-2abcd-3abcd.pdf)

## Android

- [apktool](https://github.com/iBotPeaches/Apktool) - a tool for reverse engineering Android apk files

## Java

- [bytecode-viewer](https://github.com/Konloch/bytecode-viewer) - A Java 8+ Jar & Android APK Reverse Engineering Suite (Decompiler, Editor, Debugger & More)

## VB - visual basic

- [vbsedit](https://www.vbsedit.com/)
- [vbdec](http://sandsprite.com/vbdec/) - VB6 P-Code Disassembler and debugger

## PE

The Portable Executable (PE) format is a file format for executables, object code, DLLs and others used in 32-bit and 64-bit versions of Windows operating systems

tools:

- [CFF Explorer](https://ntcore.com/?page_id=388) - PE inspection
- [dependencywalker](http://www.dependencywalker.com/) - utility that scans any 32-bit or 64-bit Windows module (exe, dll, ocx, sys, etc.) and builds a hierarchical tree diagram of all dependent modules
- [Dependencies](https://github.com/lucasg/Dependencies) - A rewrite of the old legacy software "depends.exe" in C# for Windows devs to troubleshoot dll load dependencies issues.
- [PE Detective](https://ntcore.com/?page_id=367) - ???
- [PE Bear](https://github.com/hasherezade/pe-bear) - Portable Executable reversing tool with a friendly GUI
  - https://hshrzd.wordpress.com/pe-bear/
- [PEiD](https://www.aldeid.com/wiki/PEiD) - PEiD detects most common packers, cryptors and compilers for PE files
- [peid](https://github.com/packing-box/peid) - python implementation of peid
- [Task Explorer](https://github.com/DavidXanatos/TaskExplorer) - Power full Task Manager

utilities:

- [API monitor](http://www.rohitab.com/apimonitor)
- [capa](https://github.com/mandiant/capa) - The FLARE team's open-source tool to identify capabilities in executable files
- [Detect-It-Easy](https://github.com/horsicq/Detect-It-Easy) - Program for determining types of files for Windows, Linux and MacOS
- [flare-floss](https://github.com/mandiant/flare-floss) - FLARE Obfuscated String Solver - Automatically extract obfuscated strings from malware
- [process-explorer](https://learn.microsoft.com/en-us/sysinternals/downloads/process-explorer)
- [procmon](https://learn.microsoft.com/en-us/sysinternals/downloads/procmon)
- [Regshot-Advanced](https://github.com/skydive241/Regshot-Advanced) - registry compare utility
- [Process-Dump](https://github.com/glmcdona/Process-Dump) - Windows tool for dumping malware PE files from memory back to disk for analysis
- [UniExtract2](https://github.com/Bioruebe/UniExtract2) - a tool to extract files from any type of archive or installer
- [DirWatch](https://www.aldeid.com/wiki/SysAnalyzer/DirWatch) - an interface that monitors file modifications
- [FrausDNS](https://github.com/ChrisM09/FrausDNS) - A Windows DNS Spoofer designed to capture DNS requests made from malware. Used to isolate and analyze malware
- [MAP](https://github.com/dzzie/MAP) - Malcode Analyst Pack

- [other windows internals](https://learn.microsoft.com/en-us/sysinternals/)

## Other

- [Python vulnerabilities](./python.md)
- [Virus total](https://www.virustotal.com/gui/home/upload)
- [Meta Defender OPSWAT](https://metadefender.opswat.com/)
- [Cerbero Suite](https://getintopc.com/softwares/analysis/cerbero-suite-advanced-2021-free-download/) - The Hacker’s Multitool

## cool useless stuff

- https://github.com/xoreaxeaxeax/REpsych
- https://github.com/xoreaxeaxeax/movfuscator

