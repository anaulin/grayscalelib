# -*- coding: utf-8 -*-
"""Grayscalelib, a tiny Python library to convert images to grayscale.

Example use:
  result_filename = grayscalelib.convert_file_to_grayscale(original_filename)

  result_stringIO = grayscalelib.convert_to_grayscale(original_stringIO)
"""


from PIL import Image
from cStringIO import StringIO

import os


def convert_file_to_grayscale(filename):
  """Converts an RGB image file to grayscale and saves the result to disk.

  If a file with the name intended for our grayscale converted image already
  exists, it will be overwritten.

  Args:
    filename (str): Path to the file to transform.

  Returns:
    str: The filename of the resulting grayscale file.

  Raises:
    IOError: If the specified file can't be found or opened
    ValueError: If the image in the file is not in RGB mode.
  """
  original = Image.open(filename)
  grayscale = _convert_to_grayscale(original)
  out_filename = _get_out_filename(filename)
  grayscale.save(out_filename, format=original.format)
  return out_filename


def convert_to_grayscale(buffer):
  """Converts the image in the given StringIO object to grayscale.

  Args:
    buffer (StringIO): The original image to convert. Must be in RGB mode.

  Returns:
    StringIO: The grayscale version of the original image.

  Raises:
    ValueError: If the provided image is not in RGB mode.
  """
  original = Image.open(buffer)
  grayscale = StringIO()
  _convert_to_grayscale(original).save(grayscale, format=original.format)
  return grayscale


def _convert_to_grayscale(image):
  """Converts the given Image object to grayscale.

  This function implements the core grayscale conversion algorithm, using the
  luminosity method (see https://en.wikipedia.org/wiki/Grayscale for details).
  This method was chosen since it is a common strategy for grayscale conversion
  that yields acceptable results for our purposes.

  Outline of the conversion algorithm:
    1. Convert image to a pixel array.
    2. Iterate through each pixel, computing the equivalent gray value (using a
    weighted average of the original RGB values).
    3. Create the final grayscale image, using the computed gray values and the
    original image's dimensions.

  Args:
    image (PIL.Image): The image to convert.

  Returns:
    PIL.Image: The grayscale result.

  Raises:
    ValueError: If the given image is not in RGB mode.
  """
  if image.mode != 'RGB':
    raise ValueError('Given image is not in RGB mode.')

  pixels = image.load()
  width, height = image.size
  gray_values = []
  for y in range(height):
    for x in range(width):
      r, g, b = pixels[x, y]
      gray_values.append(_get_luminance_avg(r, g, b))
  grayscale_image = Image.new('L', (width, height))
  grayscale_image.putdata(gray_values)
  return grayscale_image


def _get_luminance_avg(r, g, b):
  """Computes a weighted average of the given RGB values.

  Color weights were retrieved from the Wikipedia article on Grayscale
  conversion
  (https://en.wikipedia.org/wiki/Grayscale#Colorimetric_.28luminance-preserving.29_conversion_to_grayscale).

  Args:
    r (int): Red value of the pixel we are averaging.
    g (int): Green value of the pixel we are averaging.
    b (int): Blue value of the pixel we are averaging.

  Returns:
    int: Weighted average of the given RGB values.
  """
  return int(r * 0.2126 + g * 0.7152 + b * 0.0722)


def _get_out_filename(filename):
  """Computes a filename to use for the converted image.

  Args:
    filename (str): Original image filename.

  Returns:
    str: A filename to use for the grayscale version of the image.
  """
  name, extension = os.path.splitext(filename)
  return name + '_grayscale' + extension
