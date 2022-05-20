import cv2
import dlib

# OpenCV人脸识别分类器
classifier = cv2.CascadeClassifier(
    ".\haarcascade_frontalface_default.xml"
)
#dlib面部检测
detector = dlib.get_frontal_face_detector()
# 使用官方提供的模型构建特征提取器
predictor = dlib.shape_predictor('./shape_predictor_68_face_landmarks.dat')

#识别图片人脸并标记
def faceIndentifyPicture(img):
    gray_pic = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    dets = detector(img, 1)
    # 使用enumerate 函数遍历序列中的元素以及它们的下标
    # 下标k即为人脸序号
    # left：人脸左边距离图片左边界的距离 ；right：人脸右边距离图片左边界的距离
    # top：人脸上边距离图片上边界的距离 ；bottom：人脸下边距离图片上边界的距离
    for k, d in enumerate(dets):
        #print("dets{}".format(d))
        #print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
        #    k, d.left(), d.top(), d.right(), d.bottom()))

        # 使用predictor进行人脸关键点识别 shape为返回的结果
        shape = predictor(img, d)
        # 获取第一个和第二个点的坐标（相对于图片而不是框出来的人脸）
        #print("Part 0: {}, Part 1: {} ...".format(shape.part(0), shape.part(1)))

        # 绘制特征点
        for index, pt in enumerate(shape.parts()):
            #print('Part {}: {}'.format(index, pt))
            pt_pos = (pt.x, pt.y)
            cv2.circle(img, pt_pos, 1, (255, 0, 0), 2)
            # 利用cv2.putText输出1-68
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img, str(index + 1), pt_pos, font, 0.3, (0, 0, 255), 1, cv2.LINE_AA)

    faceRects = classifier.detectMultiScale(gray_pic, scaleFactor=1.2, minNeighbors=7, minSize=(32, 32))
    if len(faceRects):
        for faceRect in faceRects:
            x, y, w, h = faceRect

            cv2.rectangle(img, (x, y), (x + h, y + w), (0, 255, 0), 2)

    return img

#设置视频路径
video=cv2.VideoCapture(r"originPic/06.MOV")
frame_width = int(video.get(3))
frame_height = int(video.get(4))
#帧率
fps = video.get(cv2.CAP_PROP_FPS)
# 总帧数(frames)
frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
print("帧数："+str(fps))
print("总帧数："+str(frames))
print("视屏总时长："+"{0:.2f}".format(frames/fps)+"秒")

#因为本地打不开MOV后缀，转化为avi
#out0=cv2.VideoWriter("06.avi",cv2.VideoWriter_fourcc('D','I','V','X'),10,(frame_width,frame_height))
#设置保存视频路径和编码,fps等设置
out=cv2.VideoWriter("resultPic/06FaceRectPoint.avi",cv2.VideoWriter_fourcc('D','I','V','X'),fps,(frame_width,frame_height))
cnt=0
while (True):
    ret,img=video.read()
    cnt+=1
    #print("now frame:{}".format(cnt))
    if cnt>frames:
        break

    aft_img=faceIndentifyPicture(img)
    #因为展示图片来演示视频很慢，所以注释掉，如果想查看每帧的处理效果，可以去掉注释
    #cv2.imshow("Image",aft_img)
    #out0.write(img)
    out.write(aft_img)

    #按q结束视频
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()  # 释放摄像头
out.release()
#out0.release()
cv2.destroyAllWindows()  # 释放窗口资源