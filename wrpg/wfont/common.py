from enum import IntEnum
import struct

PFONT_VERSION = 0x00000000


def header_structure():
    return (
        ">"  # Big Endian
        "4s"  # Magic Header
        "I"  # File Checksum (from Baseline)
        "I"  # Baseline
        "I"  # Font defined width (0 == variable width)
    )


def header_size():
    return struct.calcsize(header_structure())


def character_entry_strucutre():
    return (
        ">"  # Big Endian
        "H"  # X
        "H"  # Y
        "H"  # Width
        "H"  # Height
        "h"  # X rendering offset
        "h"  # Y rendering offset
    )


def character_entry_size():
    return struct.calcsize(character_entry_strucutre)
