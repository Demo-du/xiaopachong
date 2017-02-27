import re
import urllib
def getHtml(url):
    page=urllib.urlopen(url)
    html=page.read()
    return html
def getImg(html):
    reg=r'src="(.*?\.jpg)" '
    imgre=re.compile(reg)
    imglist=re.findall(imgre,html)
    x=0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl, '%s.jpg'%x)
        x+=1
a=getHtml("http://tieba.baidu.com/p/4636443879")
getImg(a)
