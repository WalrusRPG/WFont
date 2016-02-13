#!/bin/env python
import struct
import zlib
from wrpg.wfont.common import (header_structure, character_entry_strucutre, PFONT_VERSION)


def pack_fontdata(archive):
    default_char = struct.pack(character_entry_strucutre(), 0, 0, 0, 0, 0, 0)
    char_array = [default_char] * 256
    for char in archive['chars']:
        char_array[char['index']] = struct.pack(character_entry_strucutre(),
                                                char['x'],
                                                char['y'],
                                                char['width'],
                                                char['height'],
                                                char['x_offset'],
                                                char['y_offset'])

    return b''.join(char_array)


def pack_header(archive, archived_font_data):
    checksum = zlib.crc32(
        b'' + struct.pack('>IIII', PFONT_VERSION,
                          archive['baseline'], 0, archive['space_width']) + archived_font_data)
    return struct.pack(header_structure(),
                       b'WFONT',
                       checksum,
                       PFONT_VERSION,
                       archive['baseline'],
                       0x0,
                       archive['space_width'])


def pack_font(archive):
    font_data = pack_fontdata(archive)
    font_header = pack_header(archive, font_data)
    return font_header + font_data
