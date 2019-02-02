
##### 由于是项目开始之后才加入公司的，事前没能和设计沟通UI资源文件需要用英文字母来命名。因为设计把整个项目所有的切图都切好了（每个图标都有1倍图、2倍图、3倍图，加起来估计有几百张），让设计或者开发改都是个不小的工作量。

![image.png](https://upload-images.jianshu.io/upload_images/741440-78872496dfee9372.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


作为一个合格的码农，我想应该从技术角度出发解决问题。复杂问题简单化，我们先做个需求分析：
- 拿到.png文件
- 把中文前缀转拼音
- 保持后缀不变，重命名文件

ok，马上打开了Google，找库、找函数、学语法。

- 如何拿到.png文件？ -> 导入```import os, sys``` 两个系统库才能调用系统函数
``` py
os.listdir()#  遍历文件 
os.path.splitext(oldFile)[0] # 取得文件前缀
os.path.splitext(oldFile)[-1] # 取得文件后缀 
```
- 如何把中文前缀转拼音？->利用别人写好的开源库
```py
from pypinyin import pinyin, lazy_pinyin, Style # github开源的中文转拼音库，感谢该库的贡献者
```
- 如何保持后缀不变，重命名文件？ -> 到了这步只是书写业务逻辑而已了，语法直接看文档即可。http://www.runoob.com/python/python-tutorial.html




##### 与大家分享一下这个小脚本，因为第一次写python，肯定很low。希望大家多多赐教。
用法：
- 先按照依赖包，终端执行 ```pip3 install pypinyin```
- 把代码复制,生成```*.py```文件
- ```cd```到UI资源文件路径下，执行```python3 *.py```
```py
import os, sys
from pypinyin import pinyin, lazy_pinyin, Style
 
tmp = [] # 用来保存中文转拼音后的数组
print("\n 开始转换 ")
for oldFile in os.listdir(): # os.listdir():得到当前目录下所有的文件. 
   isPNG = ".png" in os.path.splitext(oldFile)[-1] # 判断文件类型
   if(isPNG == False):
        print("这是" + os.path.splitext(oldFile)[-1]+"格式" + ",不是PNG我不转")
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

```

ps: 写脚本的过程，被python缩进这种奇葩语法吓尿了。都10086年了，还有这么低级的语法要求。。。


#####  转换结果如下：
如果想要中文转英文的话可以接入有道词典的API接口，不过就算翻译成英文也只是死板的翻译不会那么智能。
![image.png](https://upload-images.jianshu.io/upload_images/741440-6d82ea52f6e0ca75.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
