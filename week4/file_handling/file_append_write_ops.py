
def fileread(target,ops):
    myfile=open(target,ops)
    print(myfile.read())
    myfile.close()

#append the file
myfile2=open("E:\\Target_Lead\\Learn-Python\\resources\\demo.txt","a")
myfile2.write("\n Last line of the file")
myfile2.close()
fileread("E:\\Target_Lead\\Learn-Python\\resources\\demo.txt","r")

#over write the file
myfile=open("E:\\Target_Lead\\Learn-Python\\resources\\demo.txt","w")
myfile.write("\n Deleted the content")
myfile.close()
fileread("E:\\Target_Lead\\Learn-Python\\resources\\demo.txt","r")

#Create a new file if it does not exist:
mynewfile=open("E:\\Target_Lead\\Learn-Python\\resources\\mynewfie.txt","w")
mynewfile.write("This file created using python")
mynewfile.close()

fileread("E:\\Target_Lead\\Learn-Python\\resources\\mynewfie.txt","r")

# a new empty file is created! when we excuted the program second time it will throw error fle existst
#f = open("myfile.txt", "x")
#f.write("file new")
#f.close()
#fileread("myfile.txt","r")



