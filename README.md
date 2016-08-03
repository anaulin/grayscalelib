# grayscalelib

## Overview

A tiny library that lets you convert an RGB image to grayscale.

The library can accept either a filename (returning the filename of the converted file),
or an image that has been loaded into a StringIO object (returning a new StringIO
object with the converted image).

```python
convert_file_to_grayscale(filename)
# returns filename of the resulting grayscale file

convert_to_grayscale(stringIOBuffer)
# returns a new StringIO with the converted image
```

The grayscale conversion algorithm used is the luminosity method, as described in https://en.wikipedia.org/wiki/Grayscale#Colorimetric_.28luminance-preserving.29_conversion_to_grayscale

``grayscalelib`` supports JPG and PNG files as inputs. (It might support other
files, as supported by ``pillow``, the library used for image decoding, but it has
only been tested with JPG and PNG files. See ``pillow``'s [[format documentation][http://pillow.readthedocs.io/en/3.3.x/handbook/image-file-formats.html]]
for details.)

``grayscalelib`` has only been tested with Python 2.7

## Installation and usage
To install `grayscalelib`'s requirements:

```bash
$ pip install -r requirements.txt
```

To see an example of usage, see ``example.py``, which you can execute as
follows:
```bash
$ python example.py testdata/test_image.jpg 
```

To run the library's tests, from the repository's root directory run:

```bash
$ python grayscalelib_test.py
```
