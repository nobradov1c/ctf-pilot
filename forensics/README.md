# Forensics

## Docker

- `docker history --no-trunc <image_id>` - show used commands
- [dive](https://github.com/wagoodman/dive) - explore layer contents
- [skopeo](https://github.com/containers/skopeo) - inspect properties and configuration
  - `skopeo inspect docker-daemon:hackinglab/jumphost:latest`
  - `skopeo inspect --config docker-daemon:hackinglab/jumphost:latest`
- `/var/lib/docker/overlay2` - layers location

- `docker load -i dockREleakage.tar.gz`

## Pcap, wireshark

- extract keyboard input from USB protocol
  - [option1](pcap/parse-keyboard-1.py)
  - [option2](pcap/parse-keyboard-2.py)

## [Android](./android.md)

## Firefox

- [Firefox Decrypt](https://github.com/unode/firefox_decrypt) - extract passwords from Mozilla (Firefox™, Waterfox™, Thunderbird®, SeaMonkey®) profiles

## more tools

- [binwalk](https://github.com/ReFirmLabs/binwalk)
- [foremost](https://www.kali.org/tools/foremost/#tool-documentation)
- [scalpel](https://github.com/sleuthkit/scalpel)

## [Obfuscation](./obfuscation.md)

## other file formats

- [pdf analysis](https://book.hacktricks.xyz/generic-methodologies-and-resources/basic-forensic-methodology/specific-software-file-type-tricks/pdf-file-analysis)
  - [pdftotext](https://github.com/spatie/pdf-to-text)
    - [pdftotext online](https://smallpdf.com/blog/pdf-to-text)
    - [pdftotext online 2](https://pdftotext.com/)

## RAW, binary files

- [Veles](https://codisec.com/veles/) - Binary data analysis and visualization tool

