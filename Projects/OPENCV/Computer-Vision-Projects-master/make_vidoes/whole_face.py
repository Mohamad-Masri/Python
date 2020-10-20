import cv2


class FaceDetector():
    def __init__(self, xml_classifier):
        self.detector = cv2.CascadeClassifier(xml_classifier)

    def detect_faces(self,
                     image,
                     scaleFactor=1.15,
                     minNeighbors=5,
                     minSize=(30, 30),
                     print_info=False,
                     return_ROI=False):

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        rects = self.detector.detectMultiScale(image=gray,
                                               scaleFactor=scaleFactor,
                                               minNeighbors=minNeighbors,
                                               minSize=minSize)

        if print_info:
            print("=" * 30)
            print("i found {} people.".format(len(rects)).title())
            print("=" * 30)

        if return_ROI:
            ROI = []
            for x, y, w, h in rects:
                ROI.append(image[y:y+h, x:x+w])

            return rects, ROI

        return rects

    def draw(self, image, rects, title=None, pause=False):
        if len(rects) == 0:
            return

        for x, y, w, h in rects:
            try:
                cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
            except:
                continue

        if title:
            cv2.imshow(title, image)
            if pause:
                cv2.waitKey(0)


class EyesDetector():
    def __init__(self, xml_classifier):
        self.eyes_detector = cv2.CascadeClassifier(xml_classifier)

    def detect_eyes(self,
                    ROI,
                    scaleFactor=1.15,
                    minNeighbors=5,
                    minSize=(30, 30),
                    print_info=False):

        rects = []
        for roi in ROI:
            if len(roi.shape) > 2:
                roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

            rects.append(self.eyes_detector.detectMultiScale(image=roi,
                                                             scaleFactor=scaleFactor,
                                                             minNeighbors=minNeighbors,
                                                             minSize=minSize))

        if print_info:
            print("=" * 30)
            print("i found {} pairs.".format(len(rects) // 2).title())
            print("=" * 30)

        return rects

    def draw(self, rects, ROI):
        if len(rects) == 0:
            return
        for roi, (x, y, w, h) in zip(ROI, rects[0]):
            cv2.rectangle(roi, (x, y), (x+w, y+h), (0, 0, 255), 2)


class NoseDetector():
    def __init__(self, xml_classifier):
        self.nose_detector = cv2.CascadeClassifier(xml_classifier)

    def detect_nose(self,
                    ROI,
                    scaleFactor=1.15,
                    minNeighbors=5,
                    minSize=(15, 15),
                    print_info=False):

        rects = []
        for roi in ROI:
            if len(roi.shape) > 2:
                roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

            rects.append(self.nose_detector.detectMultiScale(image=roi,
                                                             scaleFactor=scaleFactor,
                                                             minNeighbors=minNeighbors,
                                                             minSize=minSize))

        if print_info:
            print("=" * 30)
            print("i found {} pairs.".format(len(rects) // 2).title())
            print("=" * 30)

        return rects

    def draw(self, rects, ROI):
        if len(rects) == 0:
            return
        for roi, (x, y, w, h) in zip(ROI, rects[0]):
            cv2.rectangle(roi, (x, y), (x+w, y+h), (255, 0, 0), 2)


class MouthDetector():
    def __init__(self, xml_classifier):
        self.mouse_detector = cv2.CascadeClassifier(xml_classifier)

    def detect_mouth(self,
                     ROI,
                     scaleFactor=1.15,
                     minNeighbors=5,
                     minSize=(15, 15),
                     print_info=False):

        rects = []
        for roi in ROI:
            if len(roi.shape) > 2:
                roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

            rects.append(self.mouse_detector.detectMultiScale(image=roi,
                                                              scaleFactor=scaleFactor,
                                                              minNeighbors=minNeighbors,
                                                              minSize=minSize))

        if print_info:
            print("=" * 30)
            print("i found {} pairs.".format(len(rects) // 2).title())
            print("=" * 30)

        return rects

    def draw(self, rects, ROI):
        if len(rects) == 0:
            return
        for roi, (x, y, w, h) in zip(ROI, rects[0]):
            cv2.rectangle(roi, (x, y), (x+w, y+h), (0, 255, 255), 2)


class PairDetector():
    def __init__(self, xml_classifier):
        self.pairs_detector = cv2.CascadeClassifier(xml_classifier)

    def detect_pair(self,
                    ROI,
                    scaleFactor=1.05,
                    minNeighbors=3,
                    print_info=False):

        rects = []
        for roi in ROI:
            if len(roi.shape) > 2:
                roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

            rects.append(self.pairs_detector.detectMultiScale(image=roi,
                                                              scaleFactor=scaleFactor,
                                                              minNeighbors=minNeighbors))

        if print_info:
            print("=" * 30)
            print("i found {} pairs.".format(len(rects)).title())
            print("=" * 30)

        return rects

    def draw(self, rects, ROI):
        if len(rects) == 0:
            return
        for roi, (x, y, w, h) in zip(ROI, rects[0]):
            cv2.rectangle(roi, (x, y), (x+w, y+h), (190, 243, 108), 2)
