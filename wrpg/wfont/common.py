from enum import IntEnum
import struct

PFONT_VERSION = 0x00000000


class FontType(IntEnum):
    UNKNOWN = 0
    MONOSPACE = 1
    VARIABLE_WIDTH = 2


def header_structure():
    return (
        ">"  # Big Endian
        "4s"  # Magic Header
        "I"  # File Checksum (from NB Characters)
        "I"  # NB Characters
    )


def header_size():
    return struct.calcsize(header_structure())


def character_entry_strucutre():
    return (
        ">"  # Big Endian
        "I"  # X
        "I"  # Y
        "I"  # Width
        "I"  # Height
        "i"  # X rendering offset
        "i"  # Y rendering offset
    )


def character_entry_size():
    return struct.calcsize(character_entry_strucutre)
