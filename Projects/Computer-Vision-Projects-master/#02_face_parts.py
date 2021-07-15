import sys
import os
import cv2
from make_vidoes.whole_face import *

SCRIPT_PATH = sys.path[0]
os.chdir(SCRIPT_PATH)

# ? Preparing XML Cascades
face_xml_classifier = os.path.join(os.path.dirname(cv2.__file__),
                                   "data", "haarcascade_frontalface_default.xml")

eyes_xml_classifier = os.path.join(os.path.dirname(cv2.__file__),
                                   "data", "haarcascade_eye.xml")

#! must add SCRIPT_PATH so the script can find the xml file
#! https://github.com/adobe/SimpleSensor/tree/master/simplesensor/collection_modules/demographic_camera/classifiers/haarcascades
nose_xml_classifier = "xml/haarcascade_mcs_nose.xml"

mouth_xml_classifier = "xml/haarcascade_mcs_mouth.xml"

khan = cv2.imread('images\khan.jpg')
kids = cv2.imread('images\kids.jpg')


fd = cv2.CascadeClassifier(face_xml_classifier)
ed = cv2.CascadeClassifier(eyes_xml_classifier)
nd = cv2.CascadeClassifier(nose_xml_classifier)
md = cv2.CascadeClassifier(mouth_xml_classifier)


def draw(image, rects, color=(0, 255, 0)):
    for x, y, w, h in rects:
        cv2.rectangle(image, (x, y), (x+w, y+h), color, 2)


def mark_parts_in(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_rects = fd.detectMultiScale(image=gray,
                                     scaleFactor=1.15,
                                     minNeighbors=5,
                                     minSize=(30, 30))

    draw(image, face_rects)

    ROI = [image[y:y+h, x:x+w] for x, y, w, h in face_rects]

    for roi in ROI:
        roi_grey = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        roi_grey = cv2.GaussianBlur(roi_grey, (31, 31), 0)

        eye_rects = ed.detectMultiScale(image=roi_grey,
                                        scaleFactor=1.15,
                                        minNeighbors=10,
                                        minSize=(20, 20),
                                        maxSize=(70, 70))

        # ? eye_rects relative to the whole image
        # ? face_X + eye_X, face_Y + eye_Y, face_X + eye_X + eye_W, face_Y + eye_Y + eye_H
        draw(roi, eye_rects, (0, 0, 255))

        nose_rects = nd.detectMultiScale(image=roi_grey,
                                         scaleFactor=1.05,
                                         minNeighbors=8,
                                         minSize=(10, 10))

        draw(roi, nose_rects, (255, 0, 0))

        mouth_rects = md.detectMultiScale(image=roi_grey,
                                          scaleFactor=1.05,
                                          minNeighbors=8,
                                          minSize=(50, 50),
                                          maxSize=(120, 120))

        draw(roi, mouth_rects, (0, 255, 255))


# mark_parts_in(khan)
# cv2.imshow("Khan", khan)
# cv2.waitKey(0)

# mark_parts_in(kids)
# cv2.imshow("Kids", kids)
# cv2.waitKey(0)

# ? ===================================================
fd = FaceDetector(face_xml_classifier)
ed = EyesDetector(eyes_xml_classifier)
nd = NoseDetector(nose_xml_classifier)
md = MouthDetector(mouth_xml_classifier)


def mark_parts_in(image):
    face_rects, ROI = fd.detect_faces(image, return_ROI=True)
    fd.draw(image, face_rects)

    eyes_rects = ed.detect_eyes(ROI)
    ed.draw(eyes_rects, ROI)

    nose_rects = nd.detect_nose(ROI)
    nd.draw(nose_rects, ROI)

    mouth_rects = md.detect_mouth(ROI)
    md.draw(mouth_rects, ROI)

    cv2.imshow("Detected", image)
    cv2.waitKey(0)


mark_parts_in(khan)
mark_parts_in(kids)
# ? ===================================================
