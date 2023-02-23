# Steganography

- [aperisolve](https://github.com/Zeecka/AperiSolve)

- try to find the original image and see the diff https://futureboy.us/stegano/compinput.html
  - https://tineye.com/ - looks for exact duplicates of images

## extracting data

- try to find how the data is hidden, based on how different channels look
- look for specific channels
- `convert noir.png RGB:data`

  - extract RGB data sequentially without A channel into `data` file

- example writeup [noir](https://hackmd.io/@r1t0/HywhSDkWj)

## Video

- extract frames from video
  - `mkdir frames`
  - `ffmpeg -i some.webm frames/out-%03d.jpg`
  - now we can find 'blinking lights' for morse code message

## Tools

- [openpuff](https://embeddedsw.net/OpenPuff_Steganography_Home.html)
  - custom encrypted steganography, blackarch
- [StegExpose - java jar](https://github.com/b3dk7/StegExpose)
  - expose LSB data from PNG or BMP
- [openstego](https://github.com/syvaidya/openstego)
- [steghide](https://github.com/StefanoDeVuono/steghide)
- [stegseek](https://github.com/RickdeJager/stegseek) - steghide cracker

- Image

  - [quickstego](http://quickcrypto.com/free-steganography-software.html)
  - [imagemagick](https://imagemagick.org/index.php) - try to open a file (potentially an image) - command `display` on kali

- Video

  - [spectrology](https://github.com/solusipse/spectrology)

- Audio
  - [deepsound](http://jpinsoft.net/deepsound/overview.aspx)
  - [Sonic visualiser](https://github.com/sonic-visualiser/sonic-visualiser)
    - `sudo apt-get -y install sonic-visualiser`

more....

- https://alternativeto.net/software/quickstego/
- https://0xrick.github.io/lists/stego/

## Exotic

- [spammimic](https://www.spammimic.com/)
  - innocent looking emails
  - Decode spam with a password
  - Decode fake spreadsheet
  - Decode fake PGP
  - Decode fake Russian
  - Decode space

