# Android

## Tools

- [andriller](https://github.com/den4uk/andriller)
  - `pip install andriller -U`
    - `sudo pacman -Sy tk`

## open image

- `qemu-system-x86_64 -enable-kvm -m 2048 -smp 2 -cpu host -device ES1370 -device virtio-mouse-pci -device virtio-keyboard-pci -serial mon:stdio -boot menu=on -net nic -net user,hostfwd=tcp::5555-:22 -display gtk,gl=on -drive format=raw,file=android_forensics_easy.dd`
