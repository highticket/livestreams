# -*- coding: utf-8 -*-
"""
One Minute Python

Convert Screenshot Images to PDF

"""

# import Image function from package PIL
from PIL import Image
import os

# Screenshot Directory
screenshot_dir = r'C:/Users/test_user/Documents/output/screenshots/'
screenshots = os.listdir(screenshot_dir)

for shot in screenshots:
    # define the filepaths. Input and output.
    image_path = screenshot_dir + shot
    pdf_shot = shot.replace('png', 'pdf')
    destination_path = screenshot_dir + pdf_shot
     
    # Capture the image using PIL.Image
    image = Image.open(image_path)
    
    # Save the image as a PDF to the 
    image.save(destination_path, 'PDF')