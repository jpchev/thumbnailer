import os

def setVips():
    import sys
    vipshome = os.environ['VIPS_HOME']
       
    pathSeparator = ';' if os.name == 'nt' else ':'
    os.environ['PATH'] = vipshome + pathSeparator + os.environ['PATH']
    print('path =', os.getenv('PATH'))

if 'VIPS_HOME' in os.environ:
    setVips()
    
import pyvips as vips

def thumbnail(input_filename, output_filename, width, height):
    try:
        image = vips.Image.pdfload(input_filename, page=0)
    except:
        image = vips.Image.new_from_file(input_filename)
        
    thumbnail = image.thumbnail_image(width, height=height)
    # This method can save images in any format supported by vips.
    # The format is selected from the filename suffix. 
    thumbnail.write_to_file(output_filename, Q=100)