# -*- coding: utf8 -*-
import re

html = """"http://image.suning.cn/uimg/yunxin/yunxinImg/http://image.suning.cn/uimg/yunxin/yunxinImg/head07.png蝶雨17:46:59 上传资料时提示ftp报错
，问下上传的图片格式和大小 http://image.suning.cn/uimg/yunxin/yunxinImg/http://image.suning.cn/uimg/yunxin/yunxinImg/head07.jpg"""

if __name__ == '__main__':
    p = re.compile('http+[^\u4e00-\u9fa5]+|<[^>]+>')
    aa=p.sub("", html)
    print(aa)