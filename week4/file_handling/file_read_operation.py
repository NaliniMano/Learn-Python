#myfile=open("demo.txt","r")
myfile=open("E:\\Target_Lead\\Learn-Python\\resources\\demo.txt","r")
print(myfile.read())
myfile.close
myfile2=open("E:\\Target_Lead\\Learn-Python\\resources\\demo.txt","r")

print(myfile2.readline()) # read first line of the files
for lines in myfile2:
      print(lines)