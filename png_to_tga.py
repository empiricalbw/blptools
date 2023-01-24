import os, sys
import PIL.BlpImagePlugin
from PIL import Image

for infile in sys.argv[1:]:
    f, _ = os.path.splitext(infile)
    outfile = f + '.tga'
    try:
        print('Processing %s...' % infile)
        with Image.open(infile) as im:
            im.save(outfile)
    except PIL.BlpImagePlugin.BLPFormatError as e:
        print(e)
    except OSError:
        print('cannot convert', infile)
