from PIL import Image
from cStringIO import StringIO

import os

def convert_file_to_grayscale(filename):
  """Converts an image file to grayscale and saves the result to disk.

  Returns the filename of the grayscale file.
  Raises IOError if the specified file can't be found or opened.
  Raises ValueError if the image in the file is not in RGB mode.
  """
  original = Image.open(filename)
  grayscale = _convert_to_grayscale(original)
  out_filename = _get_out_filename(filename)
  grayscale.save(out_filename, format=original.format)
  return out_filename

def convert_to_grayscale(buffer):
  """Converts the image in the given StringIO object to grayscale.

  Returns a StringIO representation of the grayscale object.
  Raises ValueError if the image in the buffer is not in RGB mode.
  """
  original = Image.open(buffer)
  grayscale = StringIO()
  _convert_to_grayscale(original).save(grayscale, format=original.format)
  return grayscale

def _convert_to_grayscale(image):
  """Converts the given Image object to grayscale.

  Returns the converted image.
  Raises ValueError if the given image is not in RGB mode.
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
  """Returns a weighted average of the given RGB values, as an integer.
  """
  return int(r * 0.2126 + g * 0.7152 + b * 0.0722)

def _get_out_filename(filename):
  name, extension = os.path.splitext(filename)
  return name + '_grayscale' + extension
