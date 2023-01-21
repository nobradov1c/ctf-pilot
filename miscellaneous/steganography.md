# Steganography

- [aperisolve](https://github.com/Zeecka/AperiSolve)

- try to find the original image and see the diff https://futureboy.us/stegano/compinput.html

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

- Video

  - [spectrology](https://github.com/solusipse/spectrology)

- Audio
  - [deepsound](http://jpinsoft.net/deepsound/overview.aspx)

more....

- https://alternativeto.net/software/quickstego/

