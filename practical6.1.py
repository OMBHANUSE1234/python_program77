import os
file1=open("abc.txt",'w')
contents=file1.write("Welcome to python programming!!!")
file1.close()
file1=open("abc.txt",'r')
read1=file1.read()
print(read1)
file1.close()

files=os.listdir('python')
file2=open("python/xyz.txt",'w')
file2.close()
print("files:",files)

# os.rename('python/xyz.txt','python/ur_file.txt')
#
# os.remove("python/ur_file.txt")

with open('xyz.txt','w+') as f:
    line=f.readline()
    print(line)

    val=f.tell()
    f.seek(val)







