import os
with open('myfile.txt','w+') as myfile:
    myfile.writelines("Hello, Basic file writing.\nHope you are doing well.\n")

with open('myfile.txt','r+',) as myfile:
    print(myfile.read())

print(os.getcwd())

for i in os.walk(os.getcwd()):
    print(i)

for dirpath,dirs,files in os.walk(os.getcwd()):
    for file in files:
        print(os.path.join(dirpath, file))

