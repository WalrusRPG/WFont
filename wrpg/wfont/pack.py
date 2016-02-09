#!/bin/env python
import struct
import zlib
from wrpg.pfont.common import (header_structure, character_entry_strucutre)


def pack_fontdata(archive):
    default_char = struct.pack(character_entry_strucutre(), 0, 0, 0, 0, 0, 0)
    char_array = [default_char] * 256
    for char in archive['chars']:
        char_array[char['index']] = sruct.pack(character_entry_strucutre(),
                                               char['x'],
                                               char['y'],
                                               char['width'],
                                               char['height'],
                                               char['x_offset'],
                                               char['y_offset'])

    return ''.join(char_array)


def pack_header(archive, archived_font_data):
    checksum = zlib.crc32('{}{}'.format(
        len(archive['chars'])), archived_font_data)
    return struct.pack(b'WFONT', checksum, len(archive['chars']))


def pack_font(archive):
    font_data = pack_fontdata(archive)
    font_header = pack_fontdata(archive, archived_font_data)
    return pack_header + pack_fontdata
