"""
A sample program that demonstrates the use of grayscalelib.

To run:
  $ python sample.py <path to some image>
"""

from PIL import Image

import argparse
import grayscalelib

parser = argparse.ArgumentParser()
parser.add_argument('filename', help='File name of image to process.')
args = parser.parse_args()

print 'Converting to grayscale:', args.filename
im = Image.open(args.filename)
im.show()

out_filename = grayscalelib.convert_file_to_grayscale(args.filename)

print 'Output saved to:', out_filename
gray_im = Image.open(out_filename)
gray_im.show()

