# tshark -r data.pcapng -T fields -e usb.capdata  | grep -v -e '^$' | sed 's/../:&/g2' > keys.txt
# grep non-empty lines
# separate bytes with : if neccesary

file_name = "keys.txt"


# KEY BINDING FROM: https://gist.github.com/MightyPork/6da26e382a7ad91b5496ee55fdc73db2
# NOT ALL KEYS ADDED, NOT NEEDED FOR PROBLEM CURRENTLY TRYING TO SOLVE, BUT POSSIBLE TO IMPLEMENT LATER IF NECESSARY
# NOT ALL OF THE KEYS THAT HAVE BEEN ADDED ARE ACCOUNTED FOR IN THE CODE TO INTERPRET THE CAPTURE RESULTS
# keys DICTIONARY INDEX IS RELATED TO VALUE IN THIRD COLUMN OF INPUT EVENT
# EACH KEY HAS A LIST ASSOCIATED WITH IT WHERE POSITION 0 IS UNSHIFTED KEY VALUE AND POSITION 1 IS SHIFTED KEY VALUE
keys = {"00": ["NONE", ""], "01": ["KB_ERR_TOO_MANY_KEYS", ""], "02": ["POST_FAIL", ""], "03": ["KB_ERR_UNDEF", ""],
        "04": ["a", "A"], "05": ["b", "B"], "06": ["c", "C"], "07": ["d", "D"], "08": ["e", "E"], "09": ["f", "F"],
        "0a": ["g", "G"], "0b": ["h", "H"], "0c": ["i", "I"], "0d": ["j", "J"], "0e": ["k", "K"], "0f": ["l", "L"],
        "10": ["m", "M"], "11": ["n", "N"], "12": ["o", "O"], "13": ["p", "P"], "14": ["q", "Q"], "15": ["r", "R"],
        "16": ["s", "S"], "17": ["t", "T"], "18": ["u", "U"], "19": ["v", "V"], "1a": ["w", "W"], "1b": ["x", "X"],
        "1c": ["y", "Y"], "1d": ["z", "Z"], "1e": ["1", "!"], "1f": ["2", "@"], "20": ["3", "#"], "21": ["4", "$"],
        "22": ["5", "%"], "23": ["6", "^"], "24": ["7", "&"], "25": ["8", "*"], "26": ["9", "("], "27": ["0", ")"],
        "28": ["\n", ""], "29": ["Esc", ""], "2a": ["BACKSPACE", ""], "2b": ["\t", ""], "2c": [" ", ""], "2d": ["-", "_"],
        "2e": ["=", "+"], "2f": ["[", "{"], "30": ["]", "}"], "31": ["\\", "|"], "32": ["#", "~"], "33": [";", ":"],
        "34": ["'", '"'],  # CONFUSION WARNING
        "35": ["`", "~"], "36": [",", "<"], "37": [".", ">"], "38": ["/", "?"], "39": ["CAPS_LOCK", ""], "3a": ["F1", ""],
        "3b": ["F2", ""], "3c": ["F3", ""], "3d": ["F4", ""], "3e": ["F5", ""], "3f": ["F6", ""], "40": ["F7", ""],
        "41": ["F8", ""], "42": ["F9", ""], "43": ["F10", ""], "44": ["F11", ""], "45": ["F12", ""], "46": ["PRT_SCR", ""],
        "47": ["SCROLL_LOCK", ""], "48": ["PAUSE", ""], "49": ["INSERT", ""], "4a": ["HOME", ""], "4b": ["PAGE_UP", ""],
        "4c": ["DELETE", ""], "4d": ["END", ""], "4e": ["PAGE_DOWN", ""], "4f": ["RIGHT_ARROW", ""], "50": ["LEFT_ARROW", ""],
        "51": ["DOWN_ARROW", ""], "52": ["UP_ARROW", ""], "53": ["NUM_LOCK", ""], "54": ["/", "CLEAR"], "55": ["*", ""],
        "56": ["-", ""], "57": ["+", ""], "58": ["\n", ""], "59": ["1", "END"], "5a": ["2", "DOWN_ARROW"],
        "5b": ["3", "PAGE_DOWN"], "5c": ["4", "LEFT_ARROW"], "5d": ["5", ""], "5e": ["6", "RIGHT_ARROW"], "5f": ["7", "HOME"],
        "60": ["8", "UP_ARROW"], "61": ["9", "PAGE_UP"], "62": ["0", "INSERT"], "63": [".", "DELETE"], "64": ["\\", "|"],
        "65": ["APPLICATION", ""], "66": ["POWER", ""], "67": ["=", ""], "68": ["F13", ""], "69": ["F14", ""], "6a": ["F15", ""],
        "6b": ["F16", ""], "6c": ["F17", ""], "6d": ["F18", ""], "6e": ["F19", ""], "6f": ["F20", ""], "70": ["F21", ""],
        "71": ["F22", ""], "72": ["F23", ""], "73": ["F24", ""],
        # remainder of keys ignored in this solution
        "74": ["", ""], "75": ["", ""], "76": ["", ""], "77": ["", ""], "78": ["", ""], "79": ["", ""], "7a": ["", ""], "7b": ["", ""],
        "7c": ["", ""], "7d": ["", ""], "7e": ["", ""], "7f": ["", ""], "80": ["", ""], "81": ["", ""], "82": ["", ""], "83": ["", ""],
        "84": ["", ""], "85": ["", ""], "86": ["", ""], "87": ["", ""], "88": ["", ""], "89": ["", ""], "8a": ["", ""], "8b": ["", ""],
        "8c": ["", ""], "8d": ["", ""], "8e": ["", ""], "8f": ["", ""], "90": ["", ""], "91": ["", ""], "92": ["", ""], "93": ["", ""],
        "94": ["", ""], "95": ["", ""], "96": ["", ""], "97": ["", ""], "98": ["", ""], "99": ["", ""], "9a": ["", ""], "9b": ["", ""],
        "9c": ["", ""], "9d": ["", ""], "9e": ["", ""], "9f": ["", ""], "a0": ["", ""], "a1": ["", ""], "a2": ["", ""], "a3": ["", ""],
        "a4": ["", ""], "a5": ["", ""], "a6": ["", ""], "a7": ["", ""], "a8": ["", ""], "a9": ["", ""], "aa": ["", ""], "ab": ["", ""],
        "ac": ["", ""], "ad": ["", ""], "ae": ["", ""], "af": ["", ""], "b0": ["", ""], "b1": ["", ""], "b2": ["", ""], "b3": ["", ""],
        "b4": ["", ""], "b5": ["", ""], "b6": ["", ""], "b7": ["", ""], "b8": ["", ""], "b9": ["", ""], "ba": ["", ""], "bb": ["", ""],
        "bc": ["", ""], "bd": ["", ""], "be": ["", ""], "bf": ["", ""], "c0": ["", ""], "c1": ["", ""], "c2": ["", ""], "c3": ["", ""],
        "c4": ["", ""], "c5": ["", ""], "c6": ["", ""], "c7": ["", ""], "c8": ["", ""], "c9": ["", ""], "ca": ["", ""], "cb": ["", ""],
        "cc": ["", ""], "cd": ["", ""], "ce": ["", ""], "cf": ["", ""], "d0": ["", ""], "d1": ["", ""], "d2": ["", ""], "d3": ["", ""],
        "d4": ["", ""], "d5": ["", ""], "d6": ["", ""], "d7": ["", ""], "d8": ["", ""], "d9": ["", ""], "da": ["", ""], "db": ["", ""],
        "dc": ["", ""], "dd": ["", ""],
        }

# IGNORED KEYS FROM 0X74 ONWARDS FOR LATER ADDITION:
'''
#define KEY_OPEN 0x74 // Keyboard Execute
#define KEY_HELP 0x75 // Keyboard Help
#define KEY_PROPS 0x76 // Keyboard Menu
#define KEY_FRONT 0x77 // Keyboard Select
#define KEY_STOP 0x78 // Keyboard Stop
#define KEY_AGAIN 0x79 // Keyboard Again
#define KEY_UNDO 0x7a // Keyboard Undo
#define KEY_CUT 0x7b // Keyboard Cut
#define KEY_COPY 0x7c // Keyboard Copy
#define KEY_PASTE 0x7d // Keyboard Paste
#define KEY_FIND 0x7e // Keyboard Find
#define KEY_MUTE 0x7f // Keyboard Mute
#define KEY_VOLUMEUP 0x80 // Keyboard Volume Up
#define KEY_VOLUMEDOWN 0x81 // Keyboard Volume Down
// 0x82  Keyboard Locking Caps Lock
// 0x83  Keyboard Locking Num Lock
// 0x84  Keyboard Locking Scroll Lock
#define KEY_KPCOMMA 0x85 // Keypad Comma
// 0x86  Keypad Equal Sign
#define KEY_RO 0x87 // Keyboard International1
#define KEY_KATAKANAHIRAGANA 0x88 // Keyboard International2
#define KEY_YEN 0x89 // Keyboard International3
#define KEY_HENKAN 0x8a // Keyboard International4
#define KEY_MUHENKAN 0x8b // Keyboard International5
#define KEY_KPJPCOMMA 0x8c // Keyboard International6
// 0x8d  Keyboard International7
// 0x8e  Keyboard International8
// 0x8f  Keyboard International9
#define KEY_HANGEUL 0x90 // Keyboard LANG1
#define KEY_HANJA 0x91 // Keyboard LANG2
#define KEY_KATAKANA 0x92 // Keyboard LANG3
#define KEY_HIRAGANA 0x93 // Keyboard LANG4
#define KEY_ZENKAKUHANKAKU 0x94 // Keyboard LANG5
// 0x95  Keyboard LANG6
// 0x96  Keyboard LANG7
// 0x97  Keyboard LANG8
// 0x98  Keyboard LANG9
// 0x99  Keyboard Alternate Erase
// 0x9a  Keyboard SysReq/Attention
// 0x9b  Keyboard Cancel
// 0x9c  Keyboard Clear
// 0x9d  Keyboard Prior
// 0x9e  Keyboard Return
// 0x9f  Keyboard Separator
// 0xa0  Keyboard Out
// 0xa1  Keyboard Oper
// 0xa2  Keyboard Clear/Again
// 0xa3  Keyboard CrSel/Props
// 0xa4  Keyboard ExSel

// 0xb0  Keypad 00
// 0xb1  Keypad 000
// 0xb2  Thousands Separator
// 0xb3  Decimal Separator
// 0xb4  Currency Unit
// 0xb5  Currency Sub-unit
#define KEY_KPLEFTPAREN 0xb6 // Keypad (
#define KEY_KPRIGHTPAREN 0xb7 // Keypad )
// 0xb8  Keypad {
// 0xb9  Keypad }
// 0xba  Keypad Tab
// 0xbb  Keypad Backspace
// 0xbc  Keypad A
// 0xbd  Keypad B
// 0xbe  Keypad C
// 0xbf  Keypad D
// 0xc0  Keypad E
// 0xc1  Keypad F
// 0xc2  Keypad XOR
// 0xc3  Keypad ^
// 0xc4  Keypad %
// 0xc5  Keypad <
// 0xc6  Keypad >
// 0xc7  Keypad &
// 0xc8  Keypad &&
// 0xc9  Keypad |
// 0xca  Keypad ||
// 0xcb  Keypad :
// 0xcc  Keypad #
// 0xcd  Keypad Space
// 0xce  Keypad @
// 0xcf  Keypad !
// 0xd0  Keypad Memory Store
// 0xd1  Keypad Memory Recall
// 0xd2  Keypad Memory Clear
// 0xd3  Keypad Memory Add
// 0xd4  Keypad Memory Subtract
// 0xd5  Keypad Memory Multiply
// 0xd6  Keypad Memory Divide
// 0xd7  Keypad +/-
// 0xd8  Keypad Clear
// 0xd9  Keypad Clear Entry
// 0xda  Keypad Binary
// 0xdb  Keypad Octal
// 0xdc  Keypad Decimal
// 0xdd  Keypad Hexadecimal
'''

# Assumption made as to the initial state of the keyboard
# Not implemented in this version, added in case of future work
CAPS_LOCK = False
NUM_LOCK = False
SCROLL_LOCK = False

# track typed message as intended
typed_message = []
# track typed message in raw form, e.g. including backspace as 'BACKSPACE'
raw_typed_message = ""
cursor_position = 0

for data_line in open(file_name, "r").readlines():
    capdata = data_line.split(":")
    if capdata[2] not in ["00", "01", "02", "03", "ff", "fe", "fd", "fc"]:
        raw_typed_message += keys[capdata[2]][1] if (
            capdata[0] == "02" or capdata[0] == "20") else keys[capdata[2]][0]
        print(keys[capdata[2]][1] if (capdata[0] ==
              "02" or capdata[0] == "20") else keys[capdata[2]][0])
        # Deal with Cursor Position changes first
        # if home cursor to zero position
        if keys[capdata[2]][0] == "HOME":
            cursor_position = 0
        # if end cursor to message length
        elif keys[capdata[2]][0] == "END":
            cursor_position = len(typed_message)
        # if right arrow and cursor less than message length cursor++
        elif keys[capdata[2]][0] == "RIGHT_ARROW":
            # Cursor position doesn't need to move if it is already at the end of the message when right arrow pressed
            if cursor_position < len(typed_message):
                cursor_position = cursor_position + 1
        # if left arrow and cursor greater than 1 cursor--
        elif keys[capdata[2]][0] == "LEFT_ARROW":
            # Cursor position doesn't need to move if it is already at the start of the message when left arrow pressed
            if cursor_position > 0:
                cursor_position = cursor_position - 1
        # Other key press events are assumed to change typed_message
        else:
            # Behaviour of key events depends on cursor position
            # if cursor postion is at the end of the message
            if cursor_position == len(typed_message):
                # Delete Key ignored if cursor is at end of string
                # Backspace Key and there is something to backspace
                if keys[capdata[2]][0] == "BACKSPACE" and len(typed_message) > 0:
                    typed_message.pop()
                    cursor_position = cursor_position - 1
                # Other Keys
                else:
                    # if shift key is held append shifted key, else append unshifted key
                    typed_message.append(keys[capdata[2]][1]) if (
                        capdata[0] == "02" or capdata[0] == "20") else typed_message.append(keys[capdata[2]][0])
                    cursor_position = cursor_position + 1
            # Cursor position is not at the end of the message
            else:
                # Delete character to right of cursor position
                if keys[capdata[2]][0] == "DELETE" and len(typed_message) > 0:
                    typed_message.pop(cursor_position)
                # Backspace Key and there is something to backspace
                elif keys[capdata[2]][0] == "BACKSPACE" and cursor_position > 0:
                    typed_message.pop(cursor_position-1)
                    cursor_position = cursor_position - 1
                else:
                    # if shift key is held insert shifted key, else insert unshifted key
                    typed_message.insert(cursor_position, keys[capdata[2]][1]) if (
                        capdata[0] == "02" or capdata[0] == "20") else typed_message.insert(cursor_position, keys[capdata[2]][0])
                    cursor_position = cursor_position + 1

print("".join(typed_message))
print('"' + raw_typed_message + '"')
