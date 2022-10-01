import os
from rich.progress import track
blogList = os.listdir("posts")
os.system("rm -rf html/*")
for post in track(blogList):
    if post == ".DS_Store": continue
    if post[-5:] == ".html" :
        os.system("cp posts/"+post+" html/"+post)  
os.system("cp basic.md index.md")
#清空主页
f = open("index.md", "a")
f.write("\n")
for post in track(blogList):
    if post == ".DS_Store": continue
    f.write("["+post[:-5]+"](html/"+post[:-5]+".html)\n\n")
f.close()
os.system("pandoc -s -f gfm -t html5 --mathjax --css=style.css index.md -o index.html")
