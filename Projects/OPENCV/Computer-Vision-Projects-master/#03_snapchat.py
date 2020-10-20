import sys
import os
import cv2
from make_vidoes import whole_face

# ?  تغير منطقة العمل للمسار الذى يوجد فيه البرنامج
# ?  XML حتى يمكننا العثور على ملفات ال
SCRIPT_PATH = sys.path[0]
os.chdir(SCRIPT_PATH)


# ? ثوابت
GLASSES_PATH = 'images/bg.png'
CROWN_PATH = 'images/crown0.png'
SOURCE_PATH = './images/fahd.jpg'

# ? XML تجهيز ملفات ال
face_xml_classifier = os.path.join(os.path.dirname(cv2.__file__),
                                   "data", "haarcascade_frontalface_default.xml")
eyepair_xml_classifier = "xml/haarcascade_mcs_eyepair_big.xml"


# ? انشاء المحددات
fd = whole_face.FaceDetector(face_xml_classifier)
pd = whole_face.PairDetector(eyepair_xml_classifier)


# ? تجهيز الصور
# ? ==> -1 : تعنى ان الصورة تحتوى على طبقة رابعة شفافة
# ? وبالتالى باستخدام هذه القيمة
# ? من ان تقوم بحذف تلك الطبقة الشفافة opencv فاننا نمنع

crown_transparent = cv2.imread(CROWN_PATH, cv2.IMREAD_UNCHANGED)
cv2.imshow('crown', crown_transparent)
glasses_transparent = cv2.imread(GLASSES_PATH, -1)
cv2.imshow('glasses', glasses_transparent)

fahd = cv2.imread(SOURCE_PATH)
cv2.imshow('image', fahd)
cv2.waitKey(0)
cv2.destroyAllWindows()
# fahd = cv2.GaussianBlur(fahd, (5, 5), 0)


#?###############  دوال مساعدة  #################

def put_crown(crown_image, image, face_rects):

    # ? تناول كل مستطيلات الوجوه الموجودة
    for (x, y, w, h) in face_rects:

        # ? للتوضيح فقط
        # ? المستطيل المحيط بالوجه
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 0), 2)

        # ? احداثيات التاج
        x1 = x
        x2 = x + w
        y1 = y - h // 2
        y2 = y

        # ? التأكد من أن التاج لن يتجاوز ابعاد الصورة
        if y1 < 0:
            continue

        roi_crown = image[y1:y2, x1:x2]  # ? منطقة التركيز والتعديل
        cv2.imshow('roi_crown', roi_crown)
        # ? تغيير ابعاد التاج وفقا لابعاد مستطيل الوجة
        # ? اذا كان الوجة قريب فالمستطيل كبير وبالتالى يتم تكبير حجم التاج
        width_crown = x2 - x1
        height_crown = y2 - y1
        crown_image = cv2.resize(crown_image,
                                 (width_crown, height_crown))

        mask_crown = crown_image[..., -1]  # ? الطبقة الشفافة
        cv2.imshow('mask_crown', mask_crown)

        bgr_crown = crown_image[..., 0:-1]  # ? كل الطبقات عد الطبقة الشفافة
        cv2.imshow('bgr_crown', bgr_crown)

        # ? اقتطاع منطقة التاج من منطقة التعديل
        back = cv2.bitwise_and(roi_crown, roi_crown,
                               mask=cv2.bitwise_not(mask_crown))

        cv2.imshow('bc', back)

        # ? ازالة الخلفية البيضاء من التاج
        front = cv2.bitwise_and(bgr_crown, bgr_crown, mask=mask_crown)
        cv2.imshow('fc', front)

        # ? دمج الصورتين
        final = cv2.add(front, back)
        cv2.imshow('final_crown', final)
        #! roi_crown = final  لا تستخدمي
        #! لأن ذلك لن يغير منطقة التعديل
        #! وانما سيجعل متغير يهمل قيمته ويساوى قيمة متغير اخر
        roi_crown[...] = final


def put_glasses(glasses_image, ALL_ROI, eyepairs):

    # ? تناول كل مستطيلات العيون الموجودة
    #! eyepairs = [[[17, 29, 63, 15]], ...]
    for pair, ROI in zip(eyepairs, ALL_ROI):

        # ? ربما تكون المجموعة فارغة وبالتالى لابد من التاكد من ذلك منعا للخطأ
        if len(pair) == 0:
            continue

        # ? pair: (عبارة عن مجموعة ثنائية الابعاد (لها قوسين
        (ex, ey, ew, eh) = pair[0]

        # ? للتوضيح فقط
        # ? تحديد المستطيل المحيط بالعينين
        cv2.rectangle(ROI, (ex, ey),
                      (ex + ew, ey + eh), (255, 0, 0), 2)

        # ? احداثيات العيون
        x1 = int(ex - ew / 10)
        x2 = int(x1 + ew + ew / 5)
        y1 = int(ey - eh / 4)
        y2 = int(y1 + 1.5 * eh)

        roi_w, roi_h = ROI.shape[:2]
        if x1 < 0 or x2 > roi_w or y1 < 0 or y2 > roi_h:
            continue

        roi_glasses = ROI[y1:y2, x1:x2]  # ? منطقة التركيز والتعديل
        cv2.imshow('roi_glasses', roi_glasses)

        # ? تغيير ابعاد النظارة وفقا لابعاد مستطيل العيون
        # ? اذا كانت العيون قريبة فالمستطيل كبير وبالتالى يتم تكبير حجم النظارة
        width_glasses = x2 - x1
        height_glasses = y2 - y1
        glasses_image = cv2.resize(glasses_image,
                                   (width_glasses, height_glasses))

        # ? الطبقة الشفافة
        mask_glasses = glasses_image[..., -1]
        cv2.imshow('mask_glasses', mask_glasses)

        # ? كل الطبقات عد الطبقة الشفافة
        bgr_glasses = glasses_image[..., 0:-1]
        cv2.imshow('bgr_glasses', bgr_glasses)

        # ? للتوضيح فقط
        # ? حدود النظارة باللون الأصفر
        cv2.rectangle(ROI, (x1, y1), (x2, y2), (0, 255, 255), 2)

        # ? اقتطاع منطقة النظارة من منطقة التعديل
        back = cv2.bitwise_and(roi_glasses, roi_glasses,
                               mask=cv2.bitwise_not(mask_glasses))

        cv2.imshow('back', back)

        # ? ازالة الخلفية البيضاء من النظارة
        front = cv2.bitwise_and(bgr_glasses, bgr_glasses, mask=mask_glasses)
        cv2.imshow('front', front)

        # ? دمج الصورتين
        final = cv2.add(front, back)
        cv2.imshow('fianl_glasses', final)
        #! roi_glasses = final  لا تستخدمي
        #! لأن ذلك لن يغير منطقة التعديل
        #! وانما سيجعل متغير يهمل قيمته ويساوى قيمة متغير اخر
        roi_glasses[...] = final


# ? التعرف على الوجه والعينين
face_rects, ROI = fd.detect_faces(fahd, return_ROI=True)
pair_rects = pd.detect_pair(ROI)

# ? تركيب النظارة والتاج
put_glasses(glasses_transparent, ROI, pair_rects)
cv2.imshow('image', fahd)
cv2.waitKey(0)
cv2.destroyAllWindows()
put_crown(crown_transparent, fahd, face_rects)

# ? عرض النتيجة النهائية
cv2.imshow('image', fahd)
cv2.waitKey(0)
