# Watermark App

This is a simple Python application built using Tkinter for adding watermarks to images. Users can drag and drop images onto the application, browse for images and watermarks, customize watermark position and size, and download the watermarked images.

## Features

- Drag and drop images onto the application
- Browse for images and watermarks
- Customize watermark position (top left, top right, bottom left, bottom right)
- Customize watermark size
- Download watermarked images

## How to Use

1. Run the `main.py` file.
2. Drag and drop images onto the application or click the "Browse" button to select images.
3. Click the "Browse" button next to "Add your watermark here" to select a watermark image.
4. Adjust the watermark position and size in the settings if needed.
5. Click "Add Watermark" to apply the watermark to the images.
6. Click "Download" to save the watermarked images to your computer.

## Requirements

- Python 3.11.8 # the application might work with other versions but has been tested and confirmed to work with Python 3.11.8
- tkinter
- Pillow

## Screenshots

### Default Settings
![Screenshot_App](https://github.com/imakim03/watermark_app/assets/143851315/1915357b-37a3-4a26-a15d-bb0ed3916592)
![Default_settings](https://github.com/imakim03/watermark_app/assets/143851315/ac8113e7-5913-40db-ab9e-d7e52f05bd4e)
Description: This screenshot shows the image made with the app's default settings applied.

### Changed Settings
![Screenshot_app_with_modified_settings](https://github.com/imakim03/watermark_app/assets/143851315/bd29368b-2a37-44d6-ad8e-fda59395054e)
![Changed Settings](https://github.com/imakim03/watermark_app/assets/143851315/7b0a9fc1-5a81-47b6-b75f-3e1691533e21)
Description: In this screenshot, the settings have been modified as follows: the size of the watermark has been adjusted to 50% of the size of the image, and it has been positioned in the bottom left corner.

## License

MIT License

Copyright (c) 2024 Imane Kimissi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
