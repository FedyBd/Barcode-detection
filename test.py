from ultralytics import YOLO
import numpy as np
from PIL import Image
from pyzbarrrr import decode_barcode

image_path = r'C:\Users\MED Fedi BOUABID\Downloads\433013359_2499290346918767_1266951130628748003_n.jpg'


# Load the pre-trained model
model = YOLO(r'runs\detect\train\weights\best.pt')
results = model.predict(source=image_path, conf=0.25)

print(results[0].boxes.xyxy)

# Assuming results[0].boxes.xyxy is a torch.Tensor
boxes_tensor = results[0].boxes.xyxy

# Convert torch.Tensor to NumPy array
boxes_numpy = boxes_tensor.cpu().detach().numpy()

# Extract the coordinates from the NumPy array
coordinates = boxes_numpy[0]  # Assuming there's only one box, adjust if necessary

# Now you can access individual coordinates
x1, y1, x2, y2 = coordinates

image = Image.open(image_path)

# Extract the coordinates
x1, y1, x2, y2 = coordinates

# Crop the image
cropped_image = image.crop((x1, y1, x2, y2))

# Save the cropped image
cropped_image_path = r'uploads\cropped_image.jpg'
cropped_image.save(cropped_image_path)

# Optionally, you can display the cropped image
cropped_image.show()

#decode and print the barcode
barcode_data = decode_barcode(cropped_image_path)
print("Barcode data:", barcode_data)

