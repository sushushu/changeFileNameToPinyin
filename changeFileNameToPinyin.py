import os, sys
from pypinyin import pinyin, lazy_pinyin, Style

tmp = [] # 用来保存中文转拼音后的数组
print("\n 开始转换 ")
for oldFile in os.listdir(): # os.listdir():得到当前目录下所有的文件.
    isPNG = ".png" in os.path.splitext(oldFile)[-1] # 判断文件类型
    if(isPNG == False):
        print("这是" + os.path.splitext(oldFile)[-1]+"格式" + ",不是png我不转")
        pass
    else:
        tmp = lazy_pinyin(os.path.splitext(oldFile)[0]) # os.path.splitext(oldFile)[0]: 拿到文件前缀;  lazy_pinyin(): 把中文转成拼音是一个第三方库pinyin的函数
        newFile = ""
        for j in tmp:
            newFile += j # 因为上面中文转拼音之后会变成一个list,所有需要拼接起来
        newFile += os.path.splitext(oldFile)[-1] # 新文件名拼接上后缀
        os.rename(oldFile,newFile) # 调用系统函数os.rename(,)开始重命名
        print(oldFile + "  ->  " + newFile)
print("\n finish！ ")
