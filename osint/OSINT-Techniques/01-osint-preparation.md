# OSINT preparation

## Host workstation setup

- VPN

  - https://inteltechniques.com/vpn.html
  - https://mullvad.net/en

- Password Manager

  - while doing OSINT, you will likely need many accounts and profiles across various services...
  - https://keepass.info/

- Windows

  - https://www.oo-software.com/en/shutup10
  - https://www.oo-software.com/en/ooappbuster
  - https://www.bleachbit.org/

- Linux

  - https://www.bleachbit.org/

- macOS

  - follow the book for setup instructions, or go to https://inteltechniques.com/osintbook10/

  - privacy:

    - you might not need this for conducting investigations inside a virtual machine
    - https://github.com/objective-see/LuLu (free)
    - https://www.obdev.at/products/littlesnitch/index.html (paid)
    - https://inteltechniques.com/blog/2021/08/03/minimizing-macos-telemetry/
    - https://inteltechniques.com/blog/2021/08/18/macos-telemetry-update/

    - system cleaner
      - https://privacy.sexy/ - will generate a script

  - [UTM - virtual machines](https://getutm.app/)

- antivirus & antimalware

  - windows:
    - windowd defender
    - [malwarebytes](https://www.malwarebytes.com/)
  - macOS and Linux:
    - https://github.com/Cisco-Talos/clamav
    - https://www.clamav.net/

- extra

- https://inteltechniques.com/osintbook10/
  - user: osint10
  - pass: book286xt

## Linux virtual machines

- Windows and Linux
  - [virtualbox](https://www.virtualbox.org/)
- macOS

  - [UTM - virtual machines](https://getutm.app/)

- os
  - [ubuntu](https://ubuntu.com/download/desktop) - easiest to work with
    - if using apple with M chip, download ARM version of Ubuntu

### tips

- shrink birtualbox machine
  1. update your linux vm system
  2. fill all "empty" space on the VM drive with a "zero file"
     ```sh
       - cd ~/Downloads
       - dd if=/dev/zero of=zerofillfile bs=1M
       - rm zerofillfile
     ```
  3. `VBoxManage modifyhd --compact <path to VDI file`

## Browser

- https://privacytests.org/

  - Brave
  - Firefox
  - Chromium - clean browser if needed
  - Tor browser

- Firefox addons
  - Firefox Containers: Isolate specific sites within tabs which do not see settings from other sites.
  - uBlock Origin: Block undesired scripts from loading.
  - DownThemAll: Download bulk media automatically.
  - Bulk Media Downloader: Download bulk media automatically.
  - VideoDownloadHelper: Download media from a page v.rith a click of a button.
  - FireShot: Generate screenshots of partial and entire web pages.
  - Nimbus: Alternative screen capture for large web pages.
  - SingleFile: New alternative screen capture option for HTML files.
  - ExifViewer: Identify metadata embedded inside a photograph.
  - User-Agent Switcher and Manager: Emulate various browsers and devices.
  - Image Search Options: Conduct automatic reverse image searches.
  - Search By Image: An alternative tool for reverse image search.
  - Resurrect Pages: Enable historical search on deleted websites.
  - Web Archives: Search archived versions of the current website.
  - Copy Selected Links: Quickly copy all hyperlinks from a website.
  - OneTab: Collapse or expand tabs into a single resource.
  - Stream Detector: Identify embedded video streams for archiving.

