from pyzbar.pyzbar import decode
from PIL import Image

def decode_barcode(image_path):
    # Open image file
    with open(image_path, 'rb') as img_file:
        # Load image
        img = Image.open(img_file)
        # Decode barcode
        decoded_objects = decode(img)
        if decoded_objects:
            # If barcode is detected, return the data
            return decoded_objects[0].data.decode('utf-8')
        else:
            return "No barcode detected"