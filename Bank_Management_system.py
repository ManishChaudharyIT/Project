import mysql.connector as c
con=c.connect(host="localhost",user="root",passwd="Manish@$125",database="Project")
# This is only for checking connected with database or not
'''if con.is_connected():
    print("yes this is connected with data base")'''
cursor=con.cursor()
acc=101


while True:
    print("*"*170)
    print(""*25,end='')
    print("\t\t \t \t\t\t\t\t Bank Management")
    print("*"*170)
    print("Please Enter Your Choice\n")

    choice=int(input("1-> Open Account\n2-> Cash Withdrawal\n3-> Cash Deposit\n4-> Account Statement\n5-> Update Account\n6-> Exit\n"))
    

#here are choice

    
    if choice==1:
        name=input("Enter Name of Account Holder:")
        balance=int(input("Enter Opening Balance:"))
        mobile=input("Enter the Registered Mobile Number:")
        query="Insert into  Bank values({},'{}',{},'{}')".format(acc,name,balance,mobile)
        acc=acc+1
        cursor.execute(query)
        con.commit()
        print("Account Open Successfully.......\n")
    
    
    if choice==2:
        account=int(input("enter the account number"))
        query="select *from Bank where account_No={}".format(account)
        cursor.execute(query)
        data=cursor.fetchone()
        if cursor.rowcount>0:
            ammount=int(input("Enter Withdrawal Ammount:"))
            if ammount <=data[2]:
                print("Transaction Completed..Available Balance is",data[2]-ammount)
            else:
                print("Insufficient fund or Account Number Not Matched")

    
    if choice==3:
        query="select *from Bank where account_No={}".format(account)
        cursor.execute(query)
        data=cursor.fetchone()
        if cursor.rowcount>0:
            print("="*170)
            print("Account Details are:")
            print("Account Number=",data[0])
            print("Name of Account Holder=",data[1])
            print("Account Balance=",data[2])
            print("Registered Mobile Number=",data[3])
            print("="*170)
        
    
    if choice==4:
        account=int(input("Enter the Account Number"))
        query="select *from Bank where account_No={}".format(account)
        cursor.execute(query)
        data=cursor.fetchone()
        if cursor.rowcount>0:
            print("="*170)
            print("Account Details are:")
            print("Account Number=",data[0])
            print("Name of Account Holder=",data[1])
            print("Account Balance=",data[2])
            print("Registered Mobile Number=",data[3])
            print("="*170)
        else:
            print(" Account Number Not Matched or not found......\n\n\n")
    
    
    if choice==5:
        account=int(input("Enter the Account Number"))
        query="select *from Bank where account_No={}".format(account)
        cursor.execute(query)
        data=cursor.fetchone()
        if cursor.rowcount>0:
             
            print("="*170)
            print("Account Details are:")
            print("Account Number=",data[0])
            print("Name of Account Holder=",data[1])
            print("Account Balance=",data[2])
            print("Registered Mobile Number=",data[3])
            print("="*170)
        else:
            print(" Account Number Not Matched or not found......\n\n\n")    
    
    
    if choice==6:
        break
