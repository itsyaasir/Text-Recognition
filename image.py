# adds image processing capabilities
from PIL import Image, ImageEnhance

# will convert the image to text string
import pytesseract
# assigning an image from the source path
img = Image.open("image_test/img2.jpg")
# adding some shrpness and contrast to the img
enhancer1 = ImageEnhance.Sharpness(img)
enhancer2 = ImageEnhance.Contrast(img)

img_edit = enhancer1.enhance(20.0)
img_edit = enhancer2.enhance(1.5)

# Save the img
img_edit.save("edited_image.png")
# file path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# converts the image to result and saves it into result variabl.
result = pytesseract.image_to_string(img_edit)

with open('text_result.txt', mode='w') as file:
    file.write(result)
    print("ready")
