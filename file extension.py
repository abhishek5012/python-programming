fn=input("enter the file name :")
f=fn.split(".")
c=f[-1]
if c=="py":
   print("the extension of the file is : python") 
elif c=="doc" or c=="docs":
    print("the extension of the file is : document")
elif c=="txt":
    print("the extension of the file is : text")
elif c=="html":
    print("the extension of the file is : html")
elif c=="c":
    print("the extension of the file is : c ")
elif c=="c++":
    print("the extension of the file is : c++ ")
elif c=="css":
    print("the extension of the file is : css ")
elif c=="php":
    print("the extension of the file is : php")
elif c=="java":
    print("the extension of the file is : javascript")
else :
    print("the extension  of this file is not able to remembered")
