import face_recognition
from PIL import Image,ImageDraw
import cv2

#设置图片路径
img=face_recognition.load_image_file("originPic/01.jpg")

face_landmarks=face_recognition.face_landmarks(img)

pil_image=Image.fromarray(img)
for face_landmark in face_landmarks:
    d=ImageDraw.Draw(pil_image,'RGBA')

    # 绘制眉毛
    #d.polygon(face_landmark['left_eyebrow'], fill=(68, 54, 39, 128))
    #d.polygon(face_landmark['right_eyebrow'], fill=(68, 54, 39, 128))
    #d.line(face_landmark['left_eyebrow'], fill=(68, 54, 39, 150), width=5)
    #d.line(face_landmark['right_eyebrow'], fill=(68, 54, 39, 150), width=5)

    # 绘制嘴唇
    d.polygon(face_landmark['top_lip'], fill=(150, 0, 0, 128))
    d.polygon(face_landmark['bottom_lip'], fill=(150, 0, 0, 128))
    d.line(face_landmark['top_lip'], fill=(150, 0, 0, 64), width=8)
    d.line(face_landmark['bottom_lip'], fill=(150, 0, 0, 64), width=8)

    # 绘制眼睛
    #d.polygon(face_landmark['left_eye'], fill=(255, 255, 255, 30))
    #d.polygon(face_landmark['right_eye'], fill=(255, 255, 255, 30))

    # 绘制眼线
    #d.line(face_landmark['left_eye'] + [face_landmark['left_eye'][0]],fill=(0, 0, 0, 110),width=6)
    #d.line(face_landmark['right_eye'] + [face_landmark['right_eye'][0]],fill=(0, 0, 0, 110),width=6)


#pil_image.show()
#设置保存路径
pil_image.save('resultPic/01FacePaint.jpg')