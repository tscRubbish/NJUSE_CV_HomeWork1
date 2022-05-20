import cv2
import dlib

#设置图片路径
picpath="originPic/02.jpg"
img=cv2.imread(picpath)
gray_pic=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#cv2.imshow("01gray",gray_pic)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

# OpenCV人脸识别分类器
classifier = cv2.CascadeClassifier(
    ".\haarcascade_frontalface_default.xml"
)
#dlib面部检测
detector = dlib.get_frontal_face_detector()
# 使用官方提供的模型构建特征提取器
predictor = dlib.shape_predictor('./shape_predictor_68_face_landmarks.dat')

dets = detector(img, 1)
# 使用enumerate 函数遍历序列中的元素以及它们的下标
# 下标k即为人脸序号
# left：人脸左边距离图片左边界的距离 ；right：人脸右边距离图片左边界的距离
# top：人脸上边距离图片上边界的距离 ；bottom：人脸下边距离图片上边界的距离
for k, d in enumerate(dets):
    print("dets{}".format(d))
    print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
        k, d.left(), d.top(), d.right(), d.bottom()))

    # 使用predictor进行人脸关键点识别 shape为返回的结果
    shape = predictor(img, d)
    # 获取第一个和第二个点的坐标（相对于图片而不是框出来的人脸）
    print("Part 0: {}, Part 1: {} ...".format(shape.part(0), shape.part(1)))

    # 绘制特征点
    for index, pt in enumerate(shape.parts()):
        print('Part {}: {}'.format(index, pt))
        pt_pos = (pt.x, pt.y)
        cv2.circle(img, pt_pos, 1, (255, 0, 0), 2)
        # 利用cv2.putText输出1-68
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str(index + 1), pt_pos, font, 0.3, (0, 0, 255), 1, cv2.LINE_AA)


#cv2.imshow("Image",gray_pic)
faceRects=classifier.detectMultiScale(gray_pic,scaleFactor=1.2,minNeighbors=10,minSize=(32,32))
if len(faceRects):
    for faceRect in faceRects:
        x,y,w,h=faceRect
        print('Face ({},{}) , ({},{})'.format(x, y,x+h,y+w))

        cv2.rectangle(img,(x,y),(x+h,y+w),(0,255,0),2)

#设置保存路径
cv2.imwrite("resultPic/02FaceRectPoint.jpg",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
