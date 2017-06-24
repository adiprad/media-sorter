#!/usr/bin/python3

from gi.repository import GExiv2

exif = GExiv2.Metadata('IMG_1234.JPG')

print (exif)
