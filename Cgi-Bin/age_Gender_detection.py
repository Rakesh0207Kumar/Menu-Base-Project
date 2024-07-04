#!/usr/bin/env python3

import cgi
import cgitb
import cv2 as cv
import numpy as np
import os
import json

cgitb.enable()

print("Content-Type: application/json")
print()

# Load pre-trained models
ageProto = "age_deploy.prototxt"
ageModel = "age_net.caffemodel"
genderProto = "gender_deploy.prototxt"
genderModel = "gender_net.caffemodel"

ageNet = cv.dnn.readNet(ageModel, ageProto)
genderNet = cv.dnn.readNet(genderModel, genderProto)

MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)

ageList = ['(0 - 2)', '(4 - 6)', '(8 - 12)', '(15 - 20)', '(25 - 32)', '(38 - 43)', '(48 - 53)', '(60 - 100)']
genderList = ['Male', 'Female']

# Get form data
form = cgi.FieldStorage()
fileitem = form['image']

if fileitem.filename:
    # Save uploaded image
    filepath = os.path.join('/tmp', os.path.basename(fileitem.filename))
    with open(filepath, 'wb') as f:
        f.write(fileitem.file.read())

    # Read the image
    frame = cv.imread(filepath)
    frameFace, bboxes = getFaceBox(genderNet, frame)

    if not bboxes:
        print(json.dumps({"error": "No face detected"}))
        exit()

    for bbox in bboxes:
        face = frame[bbox[1]:bbox[3], bbox[0]:bbox[2]]

        # Prepare input blob for gender detection
        blob = cv.dnn.blobFromImage(face, 1, (227, 227), MODEL_MEAN_VALUES, swapRB=False)
        genderNet.setInput(blob)
        genderPreds = genderNet.forward()
        gender = genderList[genderPreds[0].argmax()]

        # Prepare input blob for age detection
        ageNet.setInput(blob)
        agePreds = ageNet.forward()
        age = ageList[agePreds[0].argmax()]

        result = {"gender": gender, "age": age}
        print(json.dumps(result))

else:
    print(json.dumps({"error": "No file uploaded"}))
