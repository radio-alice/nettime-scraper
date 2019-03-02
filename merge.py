import os
import shutil

with open('ALL.txt','wb+') as wfd:
    for f in os.listdir('messages/'):
        with open('messages/' + f,'rb') as fd:
            shutil.copyfileobj(fd, wfd)