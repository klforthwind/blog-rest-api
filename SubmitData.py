import markdown2
import datetime
import time
from PSQL import *

import os

def get_file_data(filename):
    if os.path.exists(filename):
        fp = open(filename, "r")
        content = fp.read()
        fp.close()
        return content

url = input("Enter url: ")
title = input("Enter title: ")
numOfTags = input("Enter number of tags: ")

tag = []
for x in range(int(numOfTags)) :
    tag.append(input("Enter a tag: "))
    
numOfSources = input("Enter number of sources: ")
source = []
for x in range(int(numOfSources)) :
    source.append(input("Enter a source: "))

link = input("Enter file name: ")
content = get_file_data(link)

html = markdown2.markdown(content)

ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

pushData(url,title,tag,source,html,st)

