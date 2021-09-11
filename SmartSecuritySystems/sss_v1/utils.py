import cv2
from datetime import datetime
import json
import matplotlib.pyplot as plt
import numpy
import os

from django.conf import settings
from .models import RawVideo, Video

def get_video_metadata(raw_video):
    # load COCO labels
    labels = open(os.path.dirname(os.path.realpath(__file__)) + '/yolov3-coco/coco-labels', 'r').read().strip().split('\n')

    # load DNN and layers using config and weights
    net = cv2.dnn.readNetFromDarknet(os.path.dirname(os.path.realpath(__file__)) + '/yolov3-coco/yolov3.cfg', os.path.dirname(os.path.realpath(__file__)) + '/yolov3-coco/yolov3.weights')

    layers = net.getLayerNames()
    layers = [layers[uol[0] - 1] for uol in net.getUnconnectedOutLayers()]

    try:
        # try to read video file
        capture = cv2.VideoCapture(raw_video.file.path)
        metadata = {'process': {}, 'metadata': {}, 'timestamps': [], 'objects': {}}
    
        # get simple video metadata
        metadata['metadata']['pk'] = raw_video.pk
        metadata['metadata']['date'] = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        frames = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
        fps = int(capture.get(cv2.CAP_PROP_FPS))
        duration = frames / fps

        metadata['metadata']['frames'] = frames
        metadata['metadata']['fps'] = fps
        metadata['metadata']['duration'] = duration

        height = None
        width = None

        timestamp = 0

        # loop over intervals of time
        while timestamp <= numpy.floor(duration):
            # set video position and read a frame
            capture.set(cv2.CAP_PROP_POS_FRAMES, int(timestamp * fps))
            loaded, frame = capture.read()

            if not loaded:
                break

            if width is None or height is None:
                height = frame.shape[0]
                width = frame.shape[1]

                metadata['metadata']['resolution'] = {"height": height, "width": width}

            # pass data through DNN
            blob = cv2.dnn.blobFromImage(frame, 1 / 255, (416, 416), swapRB=True, crop=False)
            net.setInput(blob)
            outputs = net.forward(layers)
        
            confidences = []
            class_ids = []

            # process outputs
            for output in outputs:
                for detection in output:
                    scores = detection[5:]
                    class_id = numpy.argmax(scores)
                    confidence = scores[class_id]

                    # filter out weak detections
                    if confidence > 0.5:
                        confidences.append(float(confidence))
                        class_ids.append(class_id)

            # update response
            objects = [labels[id] for id in class_ids]
            metadata['timestamps'].append({'objects': objects, 'confidences': confidences})

            for object in objects:
                if object not in metadata['objects']:
                    metadata['objects'][object] = []

                if timestamp not in metadata['objects'][object]:
                    metadata['objects'][object].append(timestamp)

            timestamp += 1

        capture.release()

        metadata['process']['success'] = True
        metadata['process']['threshold'] = 0.5

    except:
        metadata['process']['success'] = False

    finally:
        # output as dict
        return metadata

def get_video_thumbnail(raw_video):
    capture = cv2.VideoCapture(raw_video.file.path)
    loaded, frame = capture.read()

    thumbnail = cv2.resize(frame, (116, 65))

    path = os.path.join(settings.MEDIA_ROOT, 'thumbnail' + str(raw_video.pk) + '.png')
    cv2.imwrite(path, thumbnail)
    
    return 'thumbnail' + str(raw_video.pk) + '.png'

def get_video_labels(metadata):
    x = []
    y = []

    labels = []

    for i, object in enumerate(metadata['objects']):
        labels.append(object)
        
        for timestamp in metadata['objects'][object]:
            x.append(timestamp)
            y.append(i)
    
    plt.scatter(x, y, color='b', alpha=0.75)
    plt.title('Objects Detected')
    plt.xlabel('Timestamp (s)')
    plt.yticks(range(len(labels)), labels)

    path = os.path.join(settings.MEDIA_ROOT, 'labels' + str(metadata['metadata']['pk']) + '.png')
    plt.savefig(path)

    return 'labels' + str(metadata['metadata']['pk']) + '.png'