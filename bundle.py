#!/bin/env python
from wrpg.wfont.pack import pack_font
import xml.etree.ElementTree as ET
import sys

# Littera exports in UTF-8. We want Extended ASCII.
# There is a need to convert the values
# {in: out}
littera_char_translations = {
    338: 140,
    339: 155,
}


def parse_littera_xml_font(tree):
    root = tree.getroot()
    common = root.find('common')
    baseline = int(common.get('base'))
    chars = []
    chars_element = root.find('chars')
    for char in chars_element:
        xml_id = int(char.get('id'))
        char_id = xml_id
        if xml_id in littera_char_translations:
            new_id = littera_char_translations[xml_id]
            print('Correspondant char {} => {}'.format(xml_id, new_id))
            char_id = new_id
        if char_id > 255:
            continue

        chars.append({'index': int(char_id),
                      'x': int(char.get('x')),
                      'y': int(char.get('y')),
                      'width': int(char.get('width')),
                      'height': int(char.get('height')),
                      'x_offset': int(char.get('xoffset')),
                      'y_offset': int(char.get('yoffset'))
                      })
    return {'baseline': baseline, 'chars': chars}


def main():
    if len(sys.argv) != 3:
        return usage()
    tree = ET.parse(sys.argv[1])
    char_data = parse_littera_xml_font(tree)
    print('- Data found -')
    print('Baseline : {}'.format(char_data['baseline']))
    with open(sys.argv[2], 'wb+') as f:
        f.write(pack_font(char_data))


def usage():
    print('Usage : {} file output_file'.format(sys.argv[0]))

if __name__ == '__main__':
    main()
