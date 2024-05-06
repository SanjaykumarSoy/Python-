age= int(input("enter age="))
name= input("enter name=")
while( age!=0):
     if(age>=18):
        print(name,"is eligible to vote")
     else:
         print(name," is not eligible to vote")
     age= int(input("enter age="))
     name= input("enter name=")
print("end of program")    
