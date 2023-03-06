""" 
Optical Character Recognition(OCR) for selected part of the screen
use win+shift+s select the region and run the code the text will be automatically copied to the clipboard
"""
from PIL import ImageGrab
import pyperclip
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'E:\Program Files\Tesseract-OCR\tesseract'
text=(pytesseract.image_to_string(ImageGrab.grabclipboard(), lang='eng'))
test=("".join(line.strip() for line in text))
# print(text)
pyperclip.copy(text)



