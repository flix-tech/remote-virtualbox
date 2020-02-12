"""
Mapping between keys and USB HID codes, used by helpers
Source:
https://gist.github.com/MightyPork/6da26e382a7ad91b5496ee55fdc73db2

also see usb.org for an extensive mapping.

This assumes the keyboard has a US layout. Others layouts add some special keys
to ease the insertion of non-latin characters, currency simbols and meta
keys to work with their respective writing systems.

On most OS is possible to insert arbitrary unicode codepoints and completely
avoid the root problem, this table tries to cover as much as possible.
"""
MAPPING = {
    # lowercase English letters
    "a": (0x04, False),
    "b": (0x05, False),
    "c": (0x06, False),
    "d": (0x07, False),
    "e": (0x08, False),
    "f": (0x09, False),
    "g": (0x0A, False),
    "h": (0x0B, False),
    "i": (0x0C, False),
    "j": (0x0D, False),
    "k": (0x0E, False),
    "l": (0x0F, False),
    "m": (0x10, False),
    "n": (0x11, False),
    "o": (0x12, False),
    "p": (0x13, False),
    "q": (0x14, False),
    "r": (0x15, False),
    "s": (0x16, False),
    "t": (0x17, False),
    "u": (0x18, False),
    "v": (0x19, False),
    "w": (0x1A, False),
    "x": (0x1B, False),
    "y": (0x1C, False),
    "z": (0x1D, False),
    # uppercase English letters
    "A": (0x04, True),
    "B": (0x05, True),
    "C": (0x06, True),
    "D": (0x07, True),
    "E": (0x08, True),
    "F": (0x09, True),
    "G": (0x0A, True),
    "H": (0x0B, True),
    "I": (0x0C, True),
    "J": (0x0D, True),
    "K": (0x0E, True),
    "L": (0x0F, True),
    "M": (0x10, True),
    "N": (0x11, True),
    "O": (0x12, True),
    "P": (0x13, True),
    "Q": (0x14, True),
    "R": (0x15, True),
    "S": (0x16, True),
    "T": (0x17, True),
    "U": (0x18, True),
    "V": (0x19, True),
    "W": (0x1A, True),
    "X": (0x1B, True),
    "Y": (0x1C, True),
    "Z": (0x1D, True),
    # number keys
    "1": (0x1E, False),
    "2": (0x1F, False),
    "3": (0x20, False),
    "4": (0x21, False),
    "5": (0x22, False),
    "6": (0x23, False),
    "7": (0x24, False),
    "8": (0x25, False),
    "9": (0x26, False),
    "0": (0x27, False),
    # simbols on number row
    "!": (0x1E, True),
    "@": (0x1F, True),
    "#": (0x20, True),
    "$": (0x21, True),
    "%": (0x22, True),
    "^": (0x23, True),
    "&": (0x24, True),
    "*": (0x25, True),
    "(": (0x26, True),
    ")": (0x27, True),
    # symbols usually on the right of the keyboard
    "<enter>": (0x28, False),
    "\n": (0x28, False),
    "<esc>": (0x29, False),
    "<backspace>": (0x2A, False),
    "<tab>": (0x2B, False),
    "\t": (0x2B, False),
    " ": (0x2C, False),
    "-": (0x2D, False),
    "_": (0x2D, True),
    "=": (0x2E, False),
    "+": (0x2E, True),
    "[": (0x2F, False),
    "{": (0x2F, True),
    "]": (0x30, False),
    "}": (0x30, True),
    "\\": (0x31, False),
    "|": (0x31, True),
    # >": (0x32 not defined in US
    ";": (0x33, False),
    ":": (0x33, True),
    "'": (0x34, False),
    '"': (0x34, True),
    "`": (0x35, False),
    "~": (0x35, True),
    ",": (0x36, False),
    "<": (0x36, True),
    ".": (0x37, False),
    ">": (0x37, True),
    "/": (0x38, False),
    "?": (0x38, True),
    "<caps lock>": (0x38, False),
    # Function keys
    "<f1>": (0x3A, False),
    "<f2>": (0x3B, False),
    "<f3>": (0x3C, False),
    "<f4>": (0x3D, False),
    "<f5>": (0x3E, False),
    "<f6>": (0x3F, False),
    "<f7>": (0x40, False),
    "<f8>": (0x41, False),
    "<f9>": (0x42, False),
    "<f10>": (0x43, False),
    "<f11>": (0x44, False),
    "<f12>": (0x45, False),
    # special keys
    "<print screen>": (0x46, False),
    "<scroll lock>": (0x47, False),
    "<pause>": (0x48, False),
    "<ins>": (0x49, False),
    "<home>": (0x4A, False),
    "<page up>": (0x4B, False),
    "<del>": (0x4C, False),
    "<end>": (0x4D, False),
    "<page down>": (0x4E, False),
    "<arrow right>": (0x4F, False),
    "<arrow left>": (0x50, False),
    "<arrow down>": (0x51, False),
    "<arrow up>": (0x52, False),
    # num pad
    "<numpad numlock>": (0x53, False),
    "<numpad />": (0x54, False),
    "<numpad *>": (0x55, False),
    "<numpad ->": (0x56, False),
    "<numpad +>": (0x57, False),
    "<numpad enter>": (0x58, False),
    "<numpad 1>": (0x59, False),
    "<numpad 2>": (0x5A, False),
    "<numpad 3>": (0x5B, False),
    "<numpad 4>": (0x5C, False),
    "<numpad 5>": (0x5D, False),
    "<numpad 6>": (0x5E, False),
    "<numpad 7>": (0x5F, False),
    "<numpad 8>": (0x60, False),
    "<numpad 9>": (0x61, False),
    "<numpad 0>": (0x62, False),
    "<numpad .>": (0x63, False),
    # >": (0x64 not defined
    "<app>": (0x65, False),
    "<power>": (0x66, False),
    "<numpad =>": (0x67, False),
    # extra F keys, very rare
    "<f13>": (0x68, False),
    "<f14>": (0x69, False),
    "<f15>": (0x6A, False),
    "<f16>": (0x6B, False),
    "<f17>": (0x6C, False),
    "<f18>": (0x6D, False),
    "<f19>": (0x6E, False),
    "<f20>": (0x6F, False),
    "<f21>": (0x70, False),
    "<f22>": (0x71, False),
    "<f23>": (0x72, False),
    "<f24>": (0x73, False),
    # special extra keys
    "<execute>": (0x74, False),
    "<hel[]>": (0x75, False),
    "<menu>": (0x76, False),
    "<select>": (0x77, False),
    "<stop>": (0x78, False),
    "<again>": (0x79, False),
    "<undo>": (0x7A, False),
    "<cut>": (0x7B, False),
    "<copy>": (0x7C, False),
    "<paste>": (0x7D, False),
    "<find>": (0x7E, False),
    "<mute>": (0x7F, False),
    "<volume up>": (0x80, False),
    "<volume down>": (0x81, False),
    # more numpad
    "<numpad ,>": (0x81, False),
    "<numpad (>": (0xB6, False),
    "<numpad )>": (0xB7, False),
    # control keys
    "<left ctrl>": (0xE0, False),
    "<left shift>": (0xE1, False),
    "<left alt>": (0xE2, False),
    "<left meta>": (0xE3, False),
    "<right ctrl>": (0xE4, False),
    "<right shift>": (0xE5, False),
    "<right alt>": (0xE6, False),
    "<right meta>": (0xE7, False),
    # for simplicity also map the left one as the default ones
    "<ctrl>": (0xE0, False),
    "<shift>": (0xE1, False),
    "<alt>": (0xE2, False),
}
