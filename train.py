import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':

    model=YOLO(model=r'/Users/likexin/Desktop/yolov11n_project/ultralytics/ultralytics/cfg/models/11/yolov11-CBAM.yaml')
    model.train(data=r'/Users/likexin/Desktop/Airplane_defect_photos/Airplane_defect_photos_data.yaml',
                imgsz=640,
                epochs=100,
                #batch=3,
               # workers=5,
                 
project='/Users/likexin/Desktop/Airplane_defect_photos/airplane_defect_images'
                )