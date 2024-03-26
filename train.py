from ultralytics import YOLO
import torch.cuda




if __name__ == '__main__':

    # Check if CUDA (GPU) is available
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print (device)
    # Initialize the YOLO model
    model = YOLO("yolov8n.pt")

    # Train the model with validation
    results = model.train(
        data="config.yaml",
        imgsz=416,        # input image size
        epochs=25,        # number of epochs for training
        batch=16,    # batch size
        device=device,   # use CUDA (GPU) if available
        workers=4
    )

