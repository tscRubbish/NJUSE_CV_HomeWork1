from PIL import Image
img = Image.open('glasses.png')
img = img.convert("RGBA")

datas = img.getdata()
newData = []
for item in datas:
    if item[0] == 0 and item[1] == 0 and item[2] == 0: #背景色为黑色 的像素点
        newData.append((0, 0, 0, 0))  # 把A值设置为0
    else:
        newData.append(item)

img.putdata(newData)
img.save("target.png", "PNG")  # 保存下来
