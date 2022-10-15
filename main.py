import os
import time
from rich.progress import track
blogList = os.listdir("posts")
os.system("rm -rf html/*")

for post in track(blogList):
    if post[-3:] == ".md":
        os.system("markmap posts/"+post+" &")

blogList = os.listdir("posts")
for post in track(blogList):
    if post == ".DS_Store": continue
    elif post[-5:] == ".html" :
        os.system("cp posts/"+post+" html/"+post)  
os.system("cp basic.md index.md")
#清空主页
f = open("index.md", "a")
f.write("\n")
for post in track(blogList):
    if post == ".DS_Store": continue
    elif post[-5:] == ".html": f.write("["+post[:-5]+"](html/"+post+")\n\n")
f.close()
