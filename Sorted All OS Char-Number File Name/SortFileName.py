import os

mylist = os.listdir('audio_split/')
mylist = sorted(mylist,key=lambda x: int(os.path.splitext(x)[0].replace('chunk-', '')))
for item in mylist:
    print(item)

