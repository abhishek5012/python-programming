import csv
name_lis=["NAME","SURNAME","AGE","CONTACT_NO.","E-MAIL_ID"]
def write_info(info_list):
    with open("StudentsS_information.csv","a",newline='')as csv_file:
        writer=csv.writer(csv_file)
        if csv_file.tell()==0:
            writer.writerow(["STUDENT NO.","NAME","SURNAME","AGE","CONTACT_NO.","E-MAIL_ID"])
        writer.writerow(info_list)# puts the list

i=1
condition=True
while condition:
    
        stu_info=input("               ENTER THE INFORMATION OF THE STUDENT :\n\nFORMAT IS \n[NAME SURNAME AGE CONTACT_NO. E-MAIL_ID]\n")
        student_info_list=stu_info.split(" ")
        print("*********************************##########*****#############***********************************************************")
        print("THE ABOVE INFORMATION OF THE STUDENT NO.{} IS:\n STUDENT NO.: {}\n NAME :{}\n SURNAME : {}\n AGE :{}\n CONTACT_NO :{}\n E-MAIL_ID :{}".format(i,i,student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3],student_info_list[4]))
        print("*********************************##########*****#############***********************************************************")
        choice=input(" RECHECK THE INFORMATION OF THE STUDENT :\n IF CORRECT ENTER(YES) TO SAVE\n IF INCORRECT ENTER (NO TO DELETE)\n")
        choice_ch=choice.lower()
        if choice_ch=="yes":
            student_info_list.insert(0,i)
            write_info(student_info_list)
            i=i+1
            choice_check=input("TYPE (YES) TO CONTINUE TO ENTER THE INFORMATION OR TYPE (NO) TO END\n")
            choice__check=choice_check.lower()
            if choice__check=="yes":
                condition=True
            elif choice__check=="no":
                condition=False
            else:
                condition=False
        elif choice_ch=="no":
            with open("student_delete.txt","a")as f:
                f.write(str(student_info_list))
                f.write("\n")

comp=True
while comp:
    print("*********************************##########*****#############***********************************************************")
    d=input("IF YOU WANT TO RETRIEVE THE DELETED INFOMATION TYPE (YES) IF NOT TYPE (NO)")
    print("*********************************##########*****#############***********************************************************")
 
    if d.lower()=="yes":
        li=[]
        bi=[]
        with open("student_delete.txt","r")as f:
            for q in f:
                print(q)
        print("*********************************##########*****#############***********************************************************")
        p=int(input("ENTER THE LINE NUMBER YOU WANT TO RETRIEVE :  "))
        with open("student_delete.txt","r")as f:
            content=f.readlines()
            li=[x.strip() for x in content]
            c=(p-1)
            print(li[c])
        print("\n")
        f=input("THIS IS THAT INFOMATION YOU WANT TO RETRIEVE (YES/NO):\n")    
        if f.lower()=="yes" :
            print("*********************************##########*****#############***********************************************************")
            a=input("WANT TO ADD THE SAME INFORMATION TYPE(YES) OR TO CHANGE THE INFORMATION TYPE (NO) :\n")
            bi=li[c]
            bi=bi.strip("[")
            bi=bi.strip("]")
            bi=bi.split(",")
            if a.lower()=="yes":
                
                bi.insert(0,i)
                write_info(bi)
                i+=1
                bi=str(bi)
                
            elif a.lower()=="no":
                print("*********************************##########*****#############***********************************************************")
                print("THE PREVIOUS INFORMATION IS :",bi)
                stu_info=input("ENTER THE NEW INFORMATION  :\nFORMAT IS \n[NAME SURNAME AGE CONTACT_NO. E-MAIL_ID]\n")
                print("\n")   
                student_info_list=stu_info.split(" ")
                
                print("THE PREVIOUS INFORMATION IS :",bi)
                print("*********************************##########*****#############***********************************************************")
                print("THE NEW INFORMATION YOU WANT TO RETRIEVE IS:\n STUDENT NO.: {}\n NAME :{}\n SURNAME : {}\n AGE :{}\n CONTACT_NO :{}\n E-MAIL_ID :{}".format(i,i,student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3],student_info_list[4]))
                choice=input(" RECHECK THE RETRIEVED INFORMATION  :\n IF CORRECT ENTER(YES) TO SAVE\n IF INCORRECT ENTER (NO TO DELETE)\n")
                choice_ch=choice.lower()
                if choice_ch=="yes":
                    
                    student_info_list.insert(0,i)
                    write_info(student_info_list)
                    i+=1
                    
                elif choice_ch=="no":
                    
                    print("*********************************##########*****#############***********************************************************")
                    print("\n      PLEASE REENTER THE INFORMATION CORRECTLY :")    
        else:
            print("*********************************##########*****#############***********************************************************")
     
            print("\n   SELECT THE CORRECT INFORMATION ")
        comp=True

    else:
        print("*********************************##########*****#############***********************************************************")
        print("OKAY ! GO IT WITH THIS INFORMATION")
        comp=False
print("\n")    
print("*********************************##########*****#############***********************************************************")

print("YOUR ENTERRED INFORMATION IS SAVED  IN THE DATABASE!!")
    
