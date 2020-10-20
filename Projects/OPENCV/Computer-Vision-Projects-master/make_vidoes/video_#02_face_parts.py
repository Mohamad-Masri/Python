import sys
import os
import cv2
from whole_face import *

SCRIPT_PATH = sys.path[0]
os.chdir(SCRIPT_PATH)

SOURCE_VIDEO = "E:\karim\intro.mp4"
OUTPUT_VIDEO = "e:/karim/face.mp4"


# ? Preparing XML Cascades
face_xml_classifier = os.path.join(os.path.dirname(cv2.__file__),
                                   "data", "haarcascade_frontalface_default.xml")

eyes_xml_classifier = os.path.join(os.path.dirname(cv2.__file__),
                                   "data", "haarcascade_eye.xml")

#! must add SCRIPT_PATH so the script can find the xml file
#! https://github.com/opencv/opencv_contrib/tree/master/modules/face/data/cascades
nose_xml_classifier = "../xml/haarcascade_mcs_nose.xml"

mouth_xml_classifier = "../xml/haarcascade_mcs_mouth.xml"


# ? Initializing Detectors
fd = FaceDetector(face_xml_classifier)
ed = EyesDetector(eyes_xml_classifier)
nd = NoseDetector(nose_xml_classifier)
md = MouthDetector(mouth_xml_classifier)

# ? reading source video
video = cv2.VideoCapture(SOURCE_VIDEO)
fps = video.get(cv2.CAP_PROP_FPS)

# ? the times(measured in seconds) in the video where face parts should be detected
times = {'m': 20.5  # mouth
         , 'n': 18.2  # nose
         , 'e': 16.5  # eye
         , 'f': 5.5  # face
         , 'stop': 33.8}

# ? create output video
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
out = cv2.VideoWriter(OUTPUT_VIDEO, fourcc, fps, (1280, 720))
print("Writing...")


while True:
    ret, frame = video.read()
    if not ret:
        break

    # ? for debugging perpose
    # nh = 360
    # r = nh / frame.shape[0]
    # nw = int(frame.shape[1] * r)
    # frame = cv2.resize(frame, (nw, nh),  interpolation=cv2.INTER_AREA)
    # ? multiply (time X fps) to get the corresponding frame index
    if video.get(cv2.CAP_PROP_POS_FRAMES) >= times['f'] * fps:
        face_rects, ROI = fd.detect_faces(frame, return_ROI=True)
        fd.draw(frame, face_rects)

        if video.get(cv2.CAP_PROP_POS_FRAMES) >= times['e'] * fps:
            eyes_rects = ed.detect_eyes(ROI)
            ed.draw(eyes_rects, ROI)

        if video.get(cv2.CAP_PROP_POS_FRAMES) >= times['n'] * fps:
            nose_rects = nd.detect_nose(ROI)
            nd.draw(nose_rects, ROI)

        if video.get(cv2.CAP_PROP_POS_FRAMES) >= times['m'] * fps:
            mouth_rects = md.detect_mouth(ROI)
            md.draw(mouth_rects, ROI)

    # ? for debugging perpose
    # cv2.imshow("video", frame)
    # if cv2.waitKey(1) & 0xff == ord('q'):
    #     break

    out.write(frame)

print("Done")  # writing the output video
