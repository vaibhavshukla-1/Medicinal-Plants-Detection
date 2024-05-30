from pathlib import Path

import cv2
import torch
import sys
import os
# import torch.backends.cudnn as cudnn
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'ml_models')))
from models.experimental import attempt_load
from utils.datasets import LoadStreams, LoadImages
from utils.general import check_img_size, check_requirements, check_imshow, non_max_suppression, apply_classifier, \
    scale_coords, xyxy2xywh, strip_optimizer, set_logging, increment_path
from utils.plots import plot_one_box
from utils.torch_utils import select_device, load_classifier, time_synchronized, TracedModel


class DetectImage:

    @staticmethod
    def detect(source, weights='C:/Users/Vaibhav Shukla/Desktop/major project/best.pt', view_img=False,
               save_txt=False, imgsz=640, trace=False, device='cpu', augment=False, conf_thres=0.25, iou_thres=0.45):

        webcam = source.isnumeric() or source.endswith('.txt') or source.lower().startswith(
            ('rtsp://', 'rtmp://', 'http://', 'https://'))

        # Initialize
        set_logging()
        device = select_device(device)
        half = device.type != 'cpu'  # half precision only supported on CUDA

        # Load model
        model = attempt_load(weights, map_location=device)  # load FP32 model
        stride = int(model.stride.max())  # model stride
        imgsz = check_img_size(imgsz, s=stride)  # check img_size

        if trace:
            model = TracedModel(model, device, imgsz)

        if half:
            model.half()  # to FP16

        # Set Dataloader
        if webcam:
            # cudnn.benchmark = True  # set True to speed up constant image size inference
            dataset = LoadStreams(source, img_size=imgsz, stride=stride)
        else:
            dataset = LoadImages(source, img_size=imgsz, stride=stride)

        # Get names
        names = model.module.names if hasattr(model, 'module') else model.names

        class_names = []

        for path, img, im0s, vid_cap in dataset:
            img = torch.from_numpy(img).to(device)
            img = img.half() if half else img.float()  # uint8 to fp16/32
            img /= 255.0  # 0 - 255 to 0.0 - 1.0
            if img.ndimension() == 3:
                img = img.unsqueeze(0)

            # Inference
            with torch.no_grad():  # Calculating gradients would cause a GPU memory leak
                pred = model(img, augment)[0]

            # Apply NMS
            pred = non_max_suppression(pred, conf_thres, iou_thres, classes=None, agnostic=False)

            # Process detections
            for det in pred:
                if len(det):
                    for *xyxy, _, cls in det:
                        class_names.append(names[int(cls)])

        return class_names
