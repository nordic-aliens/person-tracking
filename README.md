# Person Tracking - Yolov3 + DeepSORT


#### Conda environment
```bash
# Tensorflow CPU
conda env create -f conda-cpu.yml
conda activate tracker-cpu
```

#### Install Requirements
```bash
# TensorFlow CPU
pip install -r requirements.txt
```

### Download Yolo weights

```
wget https://pjreddie.com/media/files/yolov3.weights -O weights/yolov3.weights
```

### Load weights

```
python load_weights.py
```

### Running the Object Tracker
```
# Webcam 
python object_tracker.py --video 0 --output ./data/video/results.avi
```
