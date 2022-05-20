import cv2

#设置图片路径
picpath="originPic/01.jpg"
img=cv2.imread(picpath)

#美颜程度value
value=20
cos_image = cv2.bilateralFilter(img, value, value * 2, value / 2)
#模糊化
#cos_image=cv2.blur(cos_image,(3,3))
#设置保存路径
cv2.imwrite("resultPic/01Beauty.jpg",cos_image)
cv2.waitKey(0)
cv2.destroyAllWindows()