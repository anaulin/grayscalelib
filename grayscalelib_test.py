# -*- coding: utf-8 -*-

from PIL import Image, ImageChops
from cStringIO import StringIO

import grayscalelib
import unittest


# Paths to test images.
# NOTE: These tests assume they are being run from the root directory of the
#       grayscalelib repository.
TEST_JPG_FILE = "testdata/test_image.jpg"
TEST_PNG_FILE = "testdata/test_image.png"
EXPECTED_CONVERTED_JPG_FILE = "testdata/expected_test_image_grayscale.jpg"
EXPECTED_CONVERTED_PNG_FILE = "testdata/expected_test_image_grayscale.png"


class TestGrayscalelib(unittest.TestCase):
  def test_jpg_file_conversion(self):
    out_file = grayscalelib.convert_file_to_grayscale(TEST_JPG_FILE)
    actual = Image.open(out_file)
    expected = Image.open(EXPECTED_CONVERTED_JPG_FILE)
    self.assertIsNone(ImageChops.difference(actual, expected).getbbox())


  def test_png_file_conversion(self):
    out_file = grayscalelib.convert_file_to_grayscale(TEST_PNG_FILE)
    actual = Image.open(out_file)
    expected = Image.open(EXPECTED_CONVERTED_PNG_FILE)
    self.assertIsNone(ImageChops.difference(actual, expected).getbbox())


  def test_stream_jpg_conversion(self):
    img_stream = self._load_to_StringIO(TEST_JPG_FILE)
    actual = grayscalelib.convert_to_grayscale(img_stream)
    actual.seek(0)
    expected = StringIO(open(EXPECTED_CONVERTED_JPG_FILE).read())
    expected.seek(0)
    self.assertEqual(actual.read(), expected.read())


  def test_nonrgb_file_conversion_raises_valueerror(self):
    self.assertRaises(ValueError,
        grayscalelib.convert_file_to_grayscale, EXPECTED_CONVERTED_JPG_FILE)


  def _load_to_StringIO(self, filename):
    """Helper method to load a file into a StringIO object."""
    f = open(filename)
    stringio = StringIO(f.read())
    f.close()
    return stringio


if __name__ == '__main__':
  unittest.main()
