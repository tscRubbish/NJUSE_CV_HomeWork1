import face_recognition
from PIL import Image,ImageDraw
import cv2
import numpy

def facePicPaint(img):
    #opencv转PIL
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 转换代码
    #img=i[:,:,::-1]

    face_landmarks = face_recognition.face_landmarks(img)

    pil_image = Image.fromarray(img)
    for face_landmark in face_landmarks:
        d = ImageDraw.Draw(pil_image, 'RGBA')

        # 绘制眉毛
        # d.polygon(face_landmark['left_eyebrow'], fill=(68, 54, 39, 128))
        # d.polygon(face_landmark['right_eyebrow'], fill=(68, 54, 39, 128))
        # d.line(face_landmark['left_eyebrow'], fill=(68, 54, 39, 150), width=5)
        # d.line(face_landmark['right_eyebrow'], fill=(68, 54, 39, 150), width=5)

        # 绘制嘴唇
        d.polygon(face_landmark['top_lip'], fill=(150, 0, 0, 128))
        d.polygon(face_landmark['bottom_lip'], fill=(150, 0, 0, 128))
        d.line(face_landmark['top_lip'], fill=(150, 0, 0, 64), width=8)
        d.line(face_landmark['bottom_lip'], fill=(150, 0, 0, 64), width=8)

        # 绘制眼睛
        # d.polygon(face_landmark['left_eye'], fill=(255, 255, 255, 30))
        # d.polygon(face_landmark['right_eye'], fill=(255, 255, 255, 30))

        # 绘制眼线
        # d.line(face_landmark['left_eye'] + [face_landmark['left_eye'][0]],fill=(0, 0, 0, 110),width=6)
        # d.line(face_landmark['right_eye'] + [face_landmark['right_eye'][0]],fill=(0, 0, 0, 110),width=6)

    # PIL转opencv
    cv_img = cv2.cvtColor(numpy.array(pil_image), cv2.COLOR_RGB2BGR)  # 转换代码
    return cv_img

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

#设置保存视频路径和编码,fps等设置
out=cv2.VideoWriter("resultPic/06FacePaint.avi",cv2.VideoWriter_fourcc('D','I','V','X'),fps,(frame_width,frame_height))
cnt=0
while (True):
    ret,img=video.read()
    cnt+=1
    #print("now frame:{}".format(cnt))
    if cnt>frames:
        break

    aft_img=facePicPaint(img)
    #因为展示图片来演示视频很慢，所以注释掉，如果想查看每帧的处理效果，可以去掉注释
    #cv2.imshow("Image",aft_img)
    #out0.write(img)
    out.write(aft_img)

    #按q结束视频
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()  # 释放摄像头
out.release()
cv2.destroyAllWindows()