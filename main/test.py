import os

playlist = "D:\Python\Final Proposal\playlist"
list1 = []
list2 = []
for path in os.listdir(playlist):
    if os.path.isfile(os.path.join(playlist,path)):
        list1.append(path)
for i in list1:
    p = "playlist\\"
    i = p+i
    list2.append(i)
print(list2)