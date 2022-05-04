# This script extracts the keypresses from a pcapng file.
import os

# change this to the path of your pcapng file
pcapng_filename = "data.pcapng"


# no need to change this
keypress_ids_filename = "keypress_ids.txt"

# create the output for
command_pcapng_to_keypress_ids = (
    # f"tshark -r {pcapng_filename} -T fields -e usb.capdata > {keypress_ids_filename}"
    f"tshark -r {pcapng_filename} -Y 'usb.capdata && usb.data_len == 8' -T fields -e usb.capdata > {keypress_ids_filename}"
)
print(
    f"Running the following bash command to convert the pcapng file to 00xx00000 nrs:\n{command_pcapng_to_keypress_ids}"
)
os.system(command_pcapng_to_keypress_ids)

# read keypress id file
switcher = {
    "04": 'a',
    "05": 'b',
    "06": 'c',
    "07": 'd',
    "08": 'e',
    "09": 'f',
    "0a": 'g',
    "0b": 'h',
    "0c": 'i',
    "0d": 'j',
    "0e": 'k',
    "0f": 'l',
    "10": 'm',
    "11": 'n',
    "12": 'o',
    "13": 'p',
    "14": 'q',
    "15": 'r',
    "16": 's',
    "17": 't',
    "18": 'u',
    "19": 'v',
    "1a": 'w',
    "1b": 'x',
    "1c": 'y',
    "1d": 'z',
    "1e": '1',
    "1f": '2',
    "20": '3',
    "21": '4',
    "22": '5',
    "23": '6',
    "24": '7',
    "25": '8',
    "26": '9',
    "27": '0',
    "28": '\n',
    "29": 'ESC',
    "2a": 'BACKSPACE',
    "2c": ' ',
    "2d": '-',
    "2r": '=',
    "2f": '[',
    "30": ']',
    "32": '#/~',
    "33": ';',
    "34": '\'',
    "36": ',',
    "37": '.',
    "38": '/',
    "39": 'CAPSLOCK',
    "2b": '\t',
    "4f": 'right',
    "50": 'left',
    "51": 'down',
    "52": 'up',
    "4d": "end",
    "4a": 'home',
    "4c": 'del forward',
    "02": "L shift",
    "2b": "Tab",
    "28": "Enter",
}

switcher_mods = {
    "00": "",
    "02": "L shift",
    "20": "R shift",
    "40": "F7/shift",
}


def readFile(filename):
    fileOpen = open(filename)
    return fileOpen


file = readFile(keypress_ids_filename)
print(f"file={file}")

# parse the 0000050000000000 etc codes and convert them into keystrokes
for line in file:
    if len(line) == 17:
        two_chars = line[4:6]
        mod = line[0:2]
        try:
            print(
                f"line={line[0:16]}, relevant characters indicating keypress ID: {two_chars} convert keypres ID to letter: {switcher[two_chars]} + {switcher_mods[mod]}"
            )
        except:
            if(two_chars not in ["ff", "00", "01", "02", "03"] and two_chars[0] != 'f'):
                print(
                    f"line={line[0:16]}, relevant characters indicating keypress ID: {two_chars} convert keypres ID to letter: ???"
                )
