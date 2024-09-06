def file_read(file_name):
    myfile=open(file_name,"r")
    print(myfile.read())
    myfile.close()



mynewfile=open("writemodefile.txt","w")
mynewfile.write("Happy Day")
mynewfile.close()
file_read("writemodefile.txt")
