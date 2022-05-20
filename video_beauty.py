import cv2

def facePicBeauty(img):
    # 美颜程度value
    value = 20
    cos_image = cv2.bilateralFilter(img, value, value * 2, value / 2)
    # 模糊化
    # cos_image=cv2.blur(cos_image,(3,3))
    return cos_image

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
out=cv2.VideoWriter("resultPic/06FaceBeauty.avi",cv2.VideoWriter_fourcc('D','I','V','X'),fps,(frame_width,frame_height))
cnt=0
while (True):
    ret,img=video.read()
    cnt+=1
    #print("now frame:{}".format(cnt))
    if cnt>frames:
        break

    aft_img=facePicBeauty(img)
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