Description:
  This project aims to develop a deep learning model able to detect a barcode in a given image. The model behind it is Tiny YOLO 8, which a light version of YOLO 8 with less hidden layers in the neural network architecture. This helps significantly reduce the inference time, although its predictive accuracy is lower than YOLO 8 itself. For real time applications, this trade-off can be accepted in most cases.


Here are the 3 steps for this project :

1- Implement Tiny YOLO 8 with pretrained weights. Using transfer learning, train a model on a set of ~6000 barcodes images.
2- Use the model trained for inference on a new image.
3- Use pyzbar to decode the barcode image.
