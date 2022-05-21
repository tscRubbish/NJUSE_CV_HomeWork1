# NJUSE_CV_HomeWork1

## 作业目录

- element：人脸装饰的组件图片，内有图片处理程序，需要用处理程序element_process.py将目标组件处理成target.png
- originPic：原图
- resultPic：处理结果

## 作业文件

- Pic_face.py：对指定图片的人脸进行标注，并识别标注人脸关键点
- video_face.py：对视频的人脸进行标注，并识别标注人脸关键点
- whiten.py：对图片人脸进行磨皮和美白
- video_beauty：对视频人脸进行磨皮
- face_thin：图片人脸瘦脸
- facePaint.py：简单的图片数字化妆(口红)
- decorate.py：图片的人脸装饰(发饰，眼镜)
- video_decorate.py：视频的人脸装饰
- haarcascade_frontalface_default.xml：默认的正脸级联分类器
- shape_predictor_68_face_landmarks.dat：人脸68关键点模型

## 代码依赖

主要环境Python3.8(部分代码不是)

主要依赖如下：

- opencv 4.5.5
- face_recognition 1.3.0
- dlib 19.21.0
- scipy 

可通过如下pip命令安装opencv，face_recognition,dlib图形库

```
pip install python
pip install dlib-bin
pip install face_recognition
```

如果pip install face_recognition报错，可能是需要安装cmake依赖

```
pip install cmake
```

## 代码运行

如果想更换处理图片，请在代码中找到图片\视频输入路径变量，修改输入路径

同理，更换输出路径，请在代码中找到图片\视频输出路径变量，修改输出路径

## 注意

代码均经过本地调试运行，如果有依赖相关报错或者程序相关报错，请助教联系QQ：2010075010或邮箱2010075010@qq.com，以尽量避免不必要的误会。

