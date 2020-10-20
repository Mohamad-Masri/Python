import sys
import os
import cv2
import whole_face

# ?  تغير منطقة العمل للمسار الذى يوجد فيه البرنامج
# ?  XML حتى يمكننا العثور على ملفات ال
SCRIPT_PATH = sys.path[0]
os.chdir(SCRIPT_PATH)

# ? ثوابت
SOURCE_VIDEO = "E:\karim\intro.mp4"
OUTPUT_VIDEO = "e:/karim/face.mp4"
GLASSES_PATH = '../images/bg.png'
CROWN_PATH = '../images/crown0.png'


# ? XML تجهيز ملفات ال
face_xml_classifier = os.path.join(os.path.dirname(cv2.__file__),
                                   "data", "haarcascade_frontalface_default.xml")
eyepair_xml_classifier = "../xml/haarcascade_mcs_eyepair_big.xml"


# ? انشاء المحددات
fd = whole_face.FaceDetector(face_xml_classifier)
pd = whole_face.PairDetector(eyepair_xml_classifier)


# ? الاوقات المميزة فى الفيديو الاصلى والمراد احداث تغيير ما ابتدءا منها
times = {'g': 12.050  # وقت ظهور النظارة
         , 'c': 18.4  # وقت ظهور التاج
         , 'stop': 31  # وقت التوقف عن عرض الاشياء السابقة
         }

# ? تجهيز الصور
# ? ==> -1 : تعنى ان الصورة تحتوى على طبقة رابعة شفافة
# ? وبالتالى باستخدام هذه القيمة
# ? من ان تقوم بحذف تلك الطبقة الشفافة opencv فاننا نمنع

crown_transparent = cv2.imread(CROWN_PATH, -1)
glasses_transparent = cv2.imread(GLASSES_PATH, -1)

#?###############  دوال مساعدة  #################


def put_crown(crown_image, image, face_rects):
    '''
    image: الصورة الاصلية
    '''
    # ? تناول كل مستطيلات الوجوه الموجودة
    for (x, y, w, h) in face_rects:

        # ? للتوضيح فقط
        # cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 0), 2)

        # ? احداثيات التاج
        x1 = x
        x2 = x + w
        y1 = y - h // 2
        y2 = y

        # ? التأكد من أن التاج لن يتجاوز ابعاد الصورة
        if y1 < 0:
            continue

        roi_crown = image[y1:y2, x1:x2]  # ? منطقة التركيز والتعديل

        # ? تغيير ابعاد التاج وفقا لابعاد مستطيل الوجة
        # ? اذا كان الوجة قريب فالمستطيل كبير وبالتالى يتم تكبير حجم التاج
        width_crown = x2 - x1
        height_crown = y2 - y1
        crown_image = cv2.resize(crown_image,
                                 (width_crown, height_crown))

        mask_crown = crown_image[..., -1]  # ? الطبقة الشفافة
        bgr_crown = crown_image[..., 0:-1]  # ? كل الطبقات عد الطبقة الشفافة

        # ? اقتطاع منطقة التاج من منطقة التعديل
        back = cv2.bitwise_and(roi_crown, roi_crown,
                               mask=cv2.bitwise_not(mask_crown))

        # cv2.imshow('back', back)

        # ? ازالة الخلفية البيضاء من التاج
        front = cv2.bitwise_and(bgr_crown, bgr_crown, mask=mask_crown)
        # cv2.imshow('front', front)

        # ? دمج الصورتين
        final = cv2.add(front, back)

        #! roi_crown = final  لا تستخدمي
        #! لأن ذلك لن يغير منطقة التعديل
        #! وانما سيجعل متغير يهمل قيمته ويساوى قيمة متغير اخر
        roi_crown[...] = final


def put_glasses(glasses_image, ALL_ROI, eyepairs):
    '''
    ALL_ROI: مناطق وجود الوجه فى الصورة
    '''
    # ? تناول كل مستطيلات العيون الموجودة
    #! eyepairs = [[[17, 29, 63, 15]], ...]
    for pair, ROI in zip(eyepairs, ALL_ROI):

        # ? ربما تكون المجموعة فارغة وبالتالى لابد من التاكد من ذلك منعا للخطأ
        if len(pair) == 0:
            continue

        # ? pair: (عبارة عن مجموعة ثنائية الابعاد (لها قوسين
        (ex, ey, ew, eh) = pair[0]
        # ? للتوضيح فقط
        # cv2.rectangle(ROI, (ex, ey),
        #               (ex + ew, ey + eh), (255, 0, 0), 2)

        # ? احداثيات العيون
        x1 = int(ex - ew / 10)
        x2 = int(x1 + ew + ew / 5)
        y1 = int(ey - eh / 4)
        y2 = int(y1 + 1.5 * eh)

        roi_w, roi_h = ROI.shape[:2]
        if x1 < 0 or x2 > roi_w or y1 < 0 or y2 > roi_h:
            continue

        roi_glasses = ROI[y1:y2, x1:x2]  # ? منطقة التركيز والتعديل

        # ? تغيير ابعاد النظارة وفقا لابعاد مستطيل العيون
        # ? اذا كانت العيون قريبة فالمستطيل كبير وبالتالى يتم تكبير حجم النظارة
        width_glasses = x2 - x1
        height_glasses = y2 - y1
        glasses_image = cv2.resize(glasses_image,
                                   (width_glasses, height_glasses))

        # ? الطبقة الشفافة
        mask_glasses = glasses_image[..., -1]

        # ? كل الطبقات عد الطبقة الشفافة
        bgr_glasses = glasses_image[..., 0:-1]

        # ? للتوضيح فقط
        # cv2.rectangle(ROI, (x1, y1), (x2, y2), (0, 255, 255), 2)

        # ? اقتطاع منطقة التاج من منطقة التعديل
        back = cv2.bitwise_and(roi_glasses, roi_glasses,
                               mask=cv2.bitwise_not(mask_glasses))

        # cv2.imshow('back', back)

        # ? ازالة الخلفية البيضاء من التاج
        front = cv2.bitwise_and(bgr_glasses, bgr_glasses, mask=mask_glasses)
        # cv2.imshow('front', front)

        # ? دمج الصورتين
        final = cv2.add(front, back)

        #! roi_glasses = final  لا تستخدمي
        #! لأن ذلك لن يغير منطقة التعديل
        #! وانما سيجعل متغير يهمل قيمته ويساوى قيمة متغير اخر
        roi_glasses[...] = final


def write_video():

    # ? قراءة الفيديو الاصلى
    source = cv2.VideoCapture(SOURCE_VIDEO)
    fps = source.get(cv2.CAP_PROP_FPS)
    width = int(source.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(source.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # ? انشاء الفيديو الجديد
    fourcc = cv2.VideoWriter_fourcc(*'MP4V')
    out = cv2.VideoWriter(OUTPUT_VIDEO, fourcc, fps, (width, height))
    print("Writing...")

    while True:
        ret, frame = source.read()
        if not ret:
            break

        # ? للتوضيح فقط
        # nh = 360
        # r = nh / frame.shape[0]
        # nw = int(frame.shape[1] * r)
        # frame = cv2.resize(frame, (nw, nh),  interpolation=cv2.INTER_AREA)

        # ? (قم بضرب رقم اللقطة فى (عدد اللقطات فى الثانية
        # ? لتحصل على الزمن التقريبى لتلك اللقطة فى الفيديو
        indx_frame = source.get(cv2.CAP_PROP_POS_FRAMES)

        if indx_frame >= times['stop'] * fps:
            pass

        elif indx_frame >= times['g'] * fps:
            face_rects, ROI = fd.detect_faces(frame, return_ROI=True)
            pairs_rects = pd.detect_pair(ROI)
            put_glasses(glasses_transparent, ROI, pairs_rects)

            if indx_frame >= times['c'] * fps:
                put_crown(crown_transparent, frame, face_rects)

        # ? للتوضيح فقط
        # cv2.imshow("video", frame)
        # if cv2.waitKey(1) & 0xff == ord('q'):
        #     break

        # ? قم بكتابة اللقطة بعد التعديل للفيديو الجديد
        out.write(frame)

    print("Done")  # تم الانتهاء من انشاء الفيديو


# ? قم بانشاء الفيديو الجديد
write_video()  # writing the output video
