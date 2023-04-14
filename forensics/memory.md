# Memory forensics

- [volatility](https://www.volatilityfoundation.org/)
  - [profiles](https://github.com/volatilityfoundation/profiles)
- [redline](https://fireeye.market/apps/211364) - nice GUI

## [Volatility](https://www.volatilityfoundation.org/)

- [hacktricks cheatsheet](https://book.hacktricks.xyz/generic-methodologies-and-resources/basic-forensic-methodology/memory-dump-analysis/volatility-cheatsheet)
- [volatility workbench](https://www.osforensics.com/tools/volatility-workbench.html) - volatility3 windows gui
- [VolUtility](https://github.com/kevthehermit/VolUtility) - volatility GUI plguin, deprecated

Volatility 2:

- [command reference](https://github.com/volatilityfoundation/volatility/wiki/Command-Reference)
- `volatility -h` - list of plugins

1.  `volatility -f MEMORY_FILE.raw imageinfo` - figure out what volatility profile we need to use
2.  `volatility -f MEMORY_FILE.raw --profile=PROFILE pslist` - verify correct profile with pslist command, also view active processes
3.  `volatility -f MEMORY_FILE.raw --profile=PROFILE netscan` - view active network connections at the time of image creation
4.  `volatility -f MEMORY_FILE.raw --profile=PROFILE psxview` - view intentionally hidden processes
5.  `volatility -f MEMORY_FILE.raw --profile=PROFILE ldrmodules`

    - In addition to viewing hidden processes via psxview, we can also check this with a greater focus via the command 'ldrmodules'. Three columns will appear here in the middle, InLoad, InInit, InMem. If any of these are false, that module has likely been injected which is a really bad thing. On a normal system the grep statement above should return no output. Which process has all three columns listed as 'False' (other than System)?

6.  `volatility -f MEMORY_FILE.raw --profile=PROFILE apihooks`

    - Processes aren't the only area we're concerned with when we're examining a machine. Using the 'apihooks' command we can view unexpected patches in the standard system DLLs. If we see an instance where Hooking module: <unknown> that's really bad. This command will take a while to run, however, it will show you all of the extraneous code introduced by the malware.

7.  `volatility -f MEMORY_FILE.raw --profile=PROFILE malfind -D <Destination Directory>`

    - Injected code can be a huge issue and is highly indicative of very very bad things. We can check for this with the command `malfind`. Using the full command `volatility -f MEMORY_FILE.raw --profile=PROFILE malfind -D <Destination Directory>` we can not only find this code, but also dump it to our specified directory.

8.  `volatility -f MEMORY_FILE.raw --profile=PROFILE dlllist`
    - Last but certainly not least we can view all of the DLLs loaded into memory. DLLs are shared system libraries utilized in system processes. These are commonly subjected to hijacking and other side-loading attacks, making them a key target for forensics. Let's list all of the DLLs in memory now with the command `dlllist`

bonus commands

- `cmdscan`
  - Commands entered into cmd.exe are processed by conhost.exe (csrss.exe prior to Windows 7). So even if an attacker managed to kill the cmd.exe prior to us obtaining a memory dump, there is still a good chance of recovering history of the command line session from conhost.exe’s memory. If you find something weird (using the console's modules), try to dump the memory of the conhost.exe associated process and search for strings inside it to extract the command lines.
- `shutdowntime`
- `truecryptpassphrase`

Volatility 3:

- `vol3 -f MEMORY_FILE.raw windows.cmdline --pid 2752`

## Resources

- [virustotal](https://www.virustotal.com)
- [AlienVault Open Threat Exchange (OTX)](https://otx.alienvault.com/) - An open-source threat tracking system
- [SANS 408](https://www.sans.org/blog/for408-windows-forensic-analysis-has-been-renumbered-to-for500-windows-forensics-analysis/) - SANS Digital Forensics and Incident Response Blog

