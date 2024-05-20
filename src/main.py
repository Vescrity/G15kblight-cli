#!/bin/python
import sys
import awelc
from patch import g15_5520_patch

import argparse
from functools import partial

def hex_color_type(hex_str):
    value = int(hex_str, 16)
    return (value >> 16) & 0xFF, (value >> 8) & 0xFF, value & 0xFF

parser = argparse.ArgumentParser(prog='dccli', description='Set keyborad backlight color')
parser.add_argument('-s', type=hex_color_type, help='Static color')
parser.add_argument('-m', type=hex_color_type, help='Morph color')
parser.add_argument('-t', type=int, choices=range(0x4, 0x1000), default=255, metavar='duration', help='Morph duration')
args = parser.parse_args()
if args.s and args.m:
    awelc.set_color_and_morph(*args.s, *args.m, args.t)
elif args.s:
    awelc.set_static(*args.s)
elif args.m:
    awelc.set_morph(*args.m, args.t)
else:
    parser.print_help()