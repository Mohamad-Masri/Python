import cv2
from os import path

khan = cv2.imread('images\khan.jpg')
kids = cv2.imread('images\kids.jpg')


xml_classifier = path.join(path.dirname(cv2.__file__),
                           "data", "haarcascade_frontalface_default.xml")


def detect_faces(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_calssifier = cv2.CascadeClassifier(xml_classifier)
    rects = face_calssifier.detectMultiScale(image=gray,
                                             scaleFactor=1.15,
                                             minNeighbors=5,
                                             minSize=(30, 30))

    return rects


def draw(image, rects, title=None):
    print("=" * 30)
    print("i found {} people.".format(len(rects)).title())
    print("=" * 30)

    for x, y, w, h in rects:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    if title:
        cv2.imshow(title, image)
        cv2.waitKey(0)


cv2.imshow("Khan", khan)
cv2.waitKey(0)
draw(khan, detect_faces(khan), "Khan")

cv2.imshow("Kids", kids)
cv2.waitKey(0)
draw(kids, detect_faces(kids), "Kids")
