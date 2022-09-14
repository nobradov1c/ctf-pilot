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
