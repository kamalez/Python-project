def View_tickets(name):
    fp=open("tickets.txt","r")
    lis=fp.readlines()
    tickets=[]
    for line in lis:
        temp=[n for n in line.strip().split(" ")]
        if(temp[0]==name):
            print(" ".join(temp[1:]))
    fp.close()

def Book_tickets(name):
    fp=open("tickets.txt","a+")
    lis=fp.readlines()
    t_source=input("Enter the Source: ")
    t_des=input("Enter the Destination: ")
    t_n=input("Enter the Number of passengers: ")
    fp.write("\n" + name +" "+ t_source +" "+ t_des +" "+ t_n)
    fp.close()

def Add_train():
    fp=open("trains.txt","r")
    lis=fp.readlines()
    trains=[]
    for line in lis:
        temp=[n for n in line.strip().split(" ")]
        trains.append(temp)
    temp=[n for n in input("Enter the detials of the train: ").strip().split(" ")]
    trains.append(temp)
    fp.close()
    fp=open("trains.txt",'w')
    for each in trains:
        fp.write(" ".join(each)+"\n")
    fp.close()

def Display_train():
    fp=open("trains.txt","r")
    lis=fp.readlines()
    for line in lis:
        print(line)
    fp.close()

def Update_train():
    fp=open("trains.txt","r")
    lis=fp.readlines()
    trains=[]
    for line in lis:
        temp=[n for n in line.strip().split(" ")]
        trains.append(temp)
    Display_train()
    temp=input("Enter the train number to Update: ")
    for i in range(len(trains)):
        if trains[i][0]==temp:
            temp_values=[n for n in input("Enter the new Values of the train: ").strip().split(" ")]
            trains[i]=temp_values
    fp.close()
    fp=open("trains.txt",'w')
    for each in trains:
        fp.write(" ".join(each)+"\n")
    fp.close()

def Delete_train():
    fp=open("trains.txt","r")
    lis=fp.readlines()
    trains=[]
    for line in lis:
        temp=[n for n in line.strip().split(" ")]
        trains.append(temp)
    Display_train()
    temp=input("Enter the train number to Deleted: ")
    fp.close()
    fp=open("trains.txt",'w')
    for each in trains:
        if each[0]!=temp:
            fp.write(" ".join(each)+"\n")
    fp.close()

def pull():
    db=[]
    
    fp=open("db.txt",'r')
    lis=fp.readlines()
    for line in lis:
        line=[n for n in line.strip().split(" ")]
        dic={}
        dic["Name"]=line[0]
        dic["User_id"]=line[1]
        dic["Address"]=line[2]
        dic["Email_id"]=line[3]
        dic["Mobile_no"]=line[4]
        dic["dob"]=line[5]
        dic["age"]=line[6]
        dic["Gender"]=line[7]
        db.append(dic)
    fp.close()
    return list(db)


def check(temp,t_pass):
    fp=open("user.txt",'r')
    lis=fp.readlines()
    for line in lis:
        i,j=line.strip().split(" ")
        if (i==temp and j==t_pass):
            fp.close()
            return False
    fp.close()
    return True


def Uname():
    flag=True
    while(flag):
        temp=input("Enter the User Name: ")
        present=False
        fp=open("user.txt",'r')
        lis=fp.readlines()
        for line in lis:
            i,j=line.strip().split(" ")
            if (i==temp):
                fp.close()
                present=True
        fp.close()
        if(temp.isalpha() and present==False):
            flag=False
    return temp

def Pass():
    flag=True
    while(flag):
        temp=input("The password must contain minimum 1 uppercase, 1 Lowercase and 1 number\nEnter the password: ")
        cap=0
        small=0
        num=0
        wrong=0
        for i in temp:
            if(ord(i)>=65 and ord(i)<=90):
                cap+=1
            elif(ord(i)>=97 and ord(i)<=122):
                small+=1
            elif(ord(i)>=48 and ord(i)<=57):
                num+=1
            else:
                wrong+=1
        if(cap>0 and small>0 and num>0 and wrong==0):
            flag=False
    return temp


def create_dic():
    dic={}
    dic["Name"]=input("Enter the name: ")
    dic["User_id"]=Uname()
    dic["Address"]=input("Enter the Adress: ")
    dic["Email_id"]=input("Enter the email id: ")
    dic["Mobile_no"]=input("Enter the mobile number: ")
    dic["dob"]=(input("Year of birth: "))
    dic["age"]=str(2018-int(dic["dob"]))
    dic["Gender"]=input("Enter the gender M for male and F for female: ")
    dic["Password"]=Pass()
    fp=open("user.txt",'a')
    fp.write("\n"+str(dic["User_id"])+" "+str(dic["Password"]))
    fp.close()
    fp=open("db.txt",'a')
    fp.write("\n"+" ".join(dic.values()))
    fp.close()
    

flag=True
db=pull()
while(flag):
    choice=input("\nSelect the Choice:\n\
    1 for Customer login\n\
    2 for New User\n\
    3 for Admin Login\n\
    4 for Exit\n\
    Enter the Choice: ")
    if(choice=="1"):
        flag1=True
        while(flag1):
            temp=input("Enter the username: ")
            t_pass=input("Enter the password: ")
            flag1=check(temp,t_pass)
        print("Loged in")
        User_flag=True
        while(User_flag):
            User_choice=input("Enter the the Choice:\n\
                1 for View tickets\n\
                2 for Book tickets\n\
                Enter the Choice: ")
            if(User_choice=="1"):
                View_tickets(temp)
            elif(User_choice=="2"):
                Book_tickets(temp)
            else:
                User_flag=False
    elif(choice=="2"):
        create_dic()
        db=pull()
        print("User Successfully created")
    elif(choice=="3"):
        Admin_name=input("Enter the Admin Username: ")
        Admin_pass=input("Enter the Admin Password: ")
        Admin_flag=True
        while(Admin_flag):
            if(Admin_name=="admin" and Admin_pass=="admin"):
                Admin_choice=input("\nEnter the choice:\n\
                1 for Add Train Detials\n\
                2 for View Train Detials\n\
                3 for Update Train Detials\n\
                4 for Delete train Detials\n\
                Enter the Admin Choice: ")
                if (Admin_choice=="1"):
                    Add_train()
                elif (Admin_choice=="2"):
                    Display_train()
                elif (Admin_choice=="3"):
                    Update_train()
                elif (Admin_choice=="4"):
                    Delete_train()
                else:
                    Admin_flag=False
    else:
        flag=False
    
    



















    
