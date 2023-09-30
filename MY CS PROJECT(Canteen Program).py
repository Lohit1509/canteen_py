###CS PROJECT WORK ON CANTEEN MANAGEMENT SYSTEM 


import mysql.connector as mc
import time
import os
#******Customer Details******
def Customer_Details():
    con = mc.connect(host='localhost', user='root', passwd='LIKEABOSS', database='CANTEEN')

    if con.is_connected():
        cursor = con.cursor()
        
        Id = input("Enter the Canteen Management ID:")
        Pass = input("Enter the Canteen Management Password:")
        
        # Check staff credentials in the database
        query = "SELECT * FROM Staff WHERE Staff_ID = %s AND Password = %s"
        cursor.execute(query, (Id, Pass))
        staff = cursor.fetchone()
        
        if staff:
            while True:
                print("\t\t\t\t\t\t\tWhat Can you Do With Customer Details\n\n")
                print("\t\t\t\t\t\t\t1 - Add New Customer")
                print("\t\t\t\t\t\t\t2 - Show Customer Details")
                print("\t\t\t\t\t\t\t3 - Search Customer Detail")
                print("\t\t\t\t\t\t\t4 - Remove a Customer")
                print("\t\t\t\t\t\t\t5 - Modify Customer Detail")
                print("\t\t\t\t\t\t\t6 - Number of Customers in Canteen")
                print("\t\t\t\t\t\t\t7 - Get Back To Main Menu\n\n")
                ch = int(input("\t\t\t\t\t\t\tEnter Your Choice : "))
                if ch == 1:
                    Add_New_Customer()
                elif ch == 2:
                    Show_Customer_Details()
                elif ch == 3:
                    Search_Customer_Details()
                elif ch == 4:
                    Delete_A_Customer()
                elif ch == 5:
                    Modify_Customer_Details()
                elif ch == 6:
                    No_Of_Customers()
                elif ch == 7:
                    print("\n")
                    Main_Program()
                    break
                else:
                    print("Invalid Choice Try Again...!!!\n")
        else:
            print("\n")
            print("--->Wrong ID or Password\n")
        
        cursor.close()
        con.close()
    else:
        print("Error in database connection.")


# Function to update staff passwords
def update_staff_passwords():
    # Connect to the MySQL database
    con = mc.connect(host='localhost', user='root', passwd='LIKEABOSS', database='CANTEEN')
    
    if con.is_connected():
        cursor = con.cursor()
        
        # Update the password for staff with ID "12127"
        update_query_1 = "UPDATE Staff SET Password = %s WHERE Staff_ID = %s"
        new_password_1 = "NEWPASSWORD"  # Replace with the new password
        staff_id_1 = "12127"
        cursor.execute(update_query_1, (new_password_1, staff_id_1))
        
        # Update the password for staff with ID "LOHIT"
        update_query_2 = "UPDATE Staff SET Password = %s WHERE Staff_ID = %s"
        new_password_2 = "ANOTHERPASSWORD"  # Replace with the new password
        staff_id_2 = "LOHIT"
        cursor.execute(update_query_2, (new_password_2, staff_id_2))
        
        con.commit()
        print("Passwords updated successfully.")
    else:
        print("Error in database connection.")
    
    cursor.close()
    con.close()


    
def Add_New_Customer():
    con=mc.connect(host='localhost',user='root',passwd='LIKEABOSS',database='CANTEEN')
    if con.is_connected()==False:
        print("Error in connection\n")
    cur=con.cursor()
    Id=input("Enter New Customer_ID:")
    time.sleep(1)
    st="Select * from Customers where Customer_ID='{}'".format(Id)
    cur.execute(st)
    data=cur.fetchone()
    if data==None:
        nm=input("Enter Your Name:")
        time.sleep(1)
        Add_New_Customer.PSWD=input("Set a Password for This Customer_ID:")
        time.sleep(1)
        st="Insert into Customers values('{}',{},'{}')".format(Id,Add_New_Customer.PSWD,nm)
        cur.execute(st)
        con.commit()
        con.close()
        print("Customer Details Inserted Successfully")
        time.sleep(1)
        input("Press Enter to continue.....!!!!\n")
        time.sleep(1)
    
    
    else:
        print("Customer_ID Already Exists....!!!\n")
        time.sleep(1)
        

def Show_Customer_Details():
    con=mc.connect(host='localhost',user='root',passwd='LIKEABOSS',database='Canteen')
    if con.is_connected()==False:
        print("Error in connection\n")
    cur=con.cursor()
    st="Select * from Customers"
    cur.execute(st)
    data=cur.fetchall()
    print("Name\t\t\tCustomer_ID\t\t\tPassword")
    time.sleep(1)
    for record in data:
        print(record[2],'\t\t\t',record[0],'\t\t\t',record[1])
        time.sleep(1)
    con.close()
    input("Press Enter to continue.....!!!!\n")
    time.sleep(1)
    

def Search_Customer_Details():
    con=mc.connect(host='localhost',user='root',passwd='LIKEABOSS',database='Canteen')
    if con.is_connected()==False:
        print("Error in connection\n")
        time.sleep(1)
    cur=con.cursor()
    nm=input("Enter Customer_Name to be Searched:")
    time.sleep(1)
    st="Select * from Customers where Customer_Name='{}'".format(nm)
    cur.execute(st)
    data=cur.fetchone()
    if data==None:
        print("Record not Found...!!!")
        time.sleep(1)
    else:
        print("Customer_ID",    "PASSWORD",    "NAME")
        time.sleep(1)
        print(data)
        time.sleep(1)
        print("Customer Found")
        time.sleep(1)
    con.close()
    time.sleep(1)
    input("Press Enter to continue.....!!!!\n")
    time.sleep(1)
    
    

def Delete_A_Customer():
    con=mc.connect(host='localhost',user='root',passwd='LIKEABOSS',database='Canteen')
    if con.is_connected()==False:
        print("Error in connection\n")
        time.sleep(1)
    cur=con.cursor()
    Id=input("Enter Customer_ID to be Deleted:")
    time.sleep(1)
    st="Select * from Customers where Customer_ID='{}'".format(Id)
    cur.execute(st)
    data=cur.fetchone()
    if data==None:
        time.sleep(1)
        print("Record not Found...!!!")
        time.sleep(1)
    else:
        string="Delete from Customers where Customer_ID='{}'".format(Id)
        cur.execute(string)
    con.commit()
    print("Customer Removed Successfully")
    time.sleep(1)
    con.close()
    input("Press Enter to continue.....!!!!\n")
    time.sleep(1)
    

def Modify_Customer_Details():
    con=mc.connect(host='localhost',user='root',passwd='LIKEABOSS',database='Canteen')
    if con.is_connected()==False:
        print("Error in connection\n")
        time.sleep(1)
    cur=con.cursor()
    Id=input("Enter Customer_ID to be Modified:")
    time.sleep(1)
    st="Select * from Customers where Customer_ID='{}'".format(Id)
    cur.execute(st)
    data=cur.fetchone()
    if data==None:
        time.sleep(1)
        print("Customer not Found...!!!")
        time.sleep(1)
    else:
        time.sleep(1)
        print("Choices:\n1-Modify Name\n2-Modify Password\n***Customer_ID Can Not Be Modified***")
        time.sleep(1)
        choice=int(input("Enter your Choice"))
        time.sleep(1)
        if choice==1:
            nm=input("Enter new Name : ")
            time.sleep(1)
            st="update Customers set Customer_Name='{}' where Customer_ID='{}'".format(nm,Id)
            cur.execute(st)
            con.commit()
            time.sleep(1)
            print("Customer Details Modified Successfully")
            time.sleep(1)
        elif choice==2:
            time.sleep(1)
            pas=input("Enter existing Password:")
            time.sleep(1)
            if pas==Add_New_Customer.PSWD:
                time.sleep(1)
                Pass=input("Enter new Password:")
                time.sleep(1)
                st="update Customers set Password={} where Customer_ID='{}'".format(Pass,Id)
                cur.execute(st)
                con.commit()
                print("Customer Details Modified Successfully")
            else:
                time.sleep(1)
                print("Wrong Password Enter Correct one")
        else:
            time.sleep(1)
            print("Invalid Choice....!!!!\n")
    con.close()
    input("Press Enter to continue.....!!!!\n")
    

def No_Of_Customers():
    con=mc.connect(host='localhost',user='root',passwd='LIKEABOSS',database='Canteen')
    if con.is_connected()==False:
        time.sleep(1)
        print("Error in connection\n")
        time.sleep(1)
    cur=con.cursor()
    st="Select * from Customers"
    cur.execute(st)
    data=cur.fetchall()
    count=cur.rowcount
    time.sleep(1)
    print("Number of Customers in Canteen:",count)
    time.sleep(1)
    con.close()
    input("Press Enter to Continue....!!!!\n")
    time.sleep(1)

    

#___MAIN_HEADING___ 
def WELCOME_SCREEN():
    print("\t\t\t\t\t\t\t*************************************************************")
    print("\t\t\t\t\t\t\t******************KONARK CANTEEN JODHPUR ********************")
    print("\t\t\t\t\t\t\t*************************************************************")
    time.sleep(1)
    print("\n")
    print("\n")
    print("\t\t\t\t\t\t\t*************************************************************")
    print("\t\t\t\t\t\t\t*************WELCOME TO CANTEEN MANAGEMENT SYSTEM************")
    print("\t\t\t\t\t\t\t*************************************************************\n")
    time.sleep(1)
    print("\n")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tCreated by  --->  LOHIT JHAJHRIA\n\n\n")
    localtime=time.asctime(time.localtime(time.time()))
    time.sleep(1)
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t",localtime)
    time.sleep(1)
    print("\n\n\n")
    

#******Products Available*****
def Products_Available():
    con=mc.connect(host='localhost',user='root',passwd='LIKEABOSS',database='Canteen')
    if con.is_connected()==False:
        time.sleep(1)
        print("Error in connection")
    cur=con.cursor()
    st="Select * from Products"
    cur.execute(st)
    data=cur.fetchall()
    time.sleep(1)
    print("Product Code\t\tProduct Name\t\tProduct Price")
    for record in data:
        time.sleep(1)
        print(record[0],'\t\t\t',record[1],'\t\t\t',record[2])    
    con.close()
    time.sleep(1)
    input("Press Enter To Continue....!!!\n")
    
    
#******Update Product Details******
def Update_Product_Details():
    #__main__
    Id=input("Enter the Canteen Management ID:")
    Pass=input("Enter the Canteen Management Password:")
    if Id=="12127" and Pass=="LOHIT":
        print("1-Enter A new Product Details\n2-Update a Currently Existing Product\n3-Get Back To Main Menu")
        choice=int(input("Enter Your Choice:"))
        if choice==1:
            Add_A_New_Product()
        elif choice==2:
            Update_Product_Detail()
        elif choice==3:
            Main_Program()
        else:
            print("Invalid Choice....!!!\n")
    
def Add_A_New_Product():
    con=mc.connect(host='localhost',user='root',passwd='LIKEABOSS',database='Canteen')
    if con.is_connected()==False:
        print("Error in connection")
    cur=con.cursor()
    PC=int(input("Enter New Product_Code:"))
    st="Select * from Products where Product_Code={}".format(PC)
    cur.execute(st)
    data=cur.fetchone()
    if data==None:
        pn=input("Enter Product Name:")
        price=int(input("Enter Price for this Product:"))
        quantity=int(input("Enter Quantity Of This Product"))
        string="select * from Products where Product_Name='{}'".format(pn)
        cur.execute(string)
        dat=cur.fetchone()
        if dat==None:
            st="Insert into Products values('{}',{},'{}',{})".format(PC,pn,price,quantity)
            cur.execute(st)
            con.commit()
            con.close()
            print("Product Details Inserted Successfully")
            input("Press Enter to continue.....!!!!")
        else:
            print("Product Already Exists By a Different Product Code....!!!")
    else:
        print("Product Already Exists....!!!")

def Update_Product_Detail():
    con=mc.connect(host='localhost',user='root',passwd='LIKEABOSS',database='Canteen')
    if con.is_connected()==False:
        print("Error in connection")
    cur=con.cursor()
    PC=int(input("Enter Product Code for The Product to be Updated:"))
    st="Select * from Products where Product_Code={}".format(PC)
    cur.execute(st)
    data=cur.fetchone()
    if data==None:
        print("Product not Found...!!\n")
    else:
        print("Choices:\n1-Modify Product Name\n2-Modify Product Price\n3-Modify Product Quantity\n***Product_Code Can Not Be Modified***")
        choice=int(input("Enter your Choice"))
        if choice==1:
            pn=input("Enter new Product Name:")
            st="update Products set Product_Name='{}' where Product_Code={}".format(pn,PC)
            cur.execute(st)
            con.commit()
            print("Product Details Updated Successfully\n")
        elif choice==2:
            price=input("Enter new Price:")
            st="update Products set Product_Price={} where Product_Code={}".format(price,PC)
            cur.execute(st)
            con.commit()
            print("Product Details Updated Successfully\n")
        elif choice==3:
            quantity=input("Enter new Quantity:")
            st="update Products set Quantity={} where Product_Code={}".format(quantity,PC)
            cur.execute(st)
            con.commit()
            print("Product Details Updated Successfully\n")
        else:
            print("Invalid Choice....!!!!\n")
        con.close()
        
#*****Buy A Product*****
def Buy_Product():
    total=0
    ID=input("Enter Your Customer_ID:")
    Pass=input("Enter Your Password:")
    con=mc.connect(host='localhost',user='root',passwd='LIKEABOSS',database='Canteen')
    if con.is_connected()==False:
        print("Error in connection")
    cur=con.cursor()
    st="Select * from Customers where Customer_ID='{}' and Password={}".format(ID,Pass)
    cur.execute(st)
    data=cur.fetchone()
    if data==None:
        print("Customer Doesn't Exist...!!!")
        input("Press Enter to Continue....!!!\n")
        Main_Program()
    else:
        print("Welcome",data[2])    
    input("Press Enter to continue.....!!!!\n")
    while True:
        print("1-Buy Product")
        print("2-Remove Product From Cart")
        print("3-Get Total Amount Summary")
        print("4-Get To Main Menu")
        ch=int(input("Enter Your Choice:"))
        if ch==1:
            product=int(input("Enter Product Code You Want to Buy:"))
            n=int(input("Enter Quantity of Product you want to Buy:"))
            st="Select * from Products where Product_Code={}".format(product)
            cur.execute(st)
            data=cur.fetchone()
            if data==None:
                print("No Product Found With This Product Code...!!!")
            else:
                if data[3]==0:
                    print("Product Unavailable At This Time....!!!")
                    print("We are Sorry for Your Inconvinience")
                else:
                    price=data[2]*n
                    total+=price
                    print(n,"Packets Of",data[1],"Added to Your Cart")
                    quantity=data[3]-n
                    string="update Products set Quantity={} where Product_Code={}".format(quantity,product)
                    cur.execute(string)
                    con.commit()
        elif ch==2:
            prod=int(input("Enter Product Code You Want to Delete:"))
            num=int(input("Enter Quantity of Product you Want to Delete:"))
            st="Select * from Products where Product_Code={}".format(product)
            cur.execute(st)
            data=cur.fetchone()
            if data==None:
                print("No Product Found With This Product Code...!!!")
            else:
                price=data[2]*num
                total-=price
                print(data[1],"Deleted From Your Cart")
                quantity=data[3]+n
                string="update Products set Quantity={} where Product_Code={}".format(quantity,product)
                cur.execute(string)
                con.commit()
           
        elif ch==3:
            print("\nYour Total Amount for the Purchase:",total,"\n")
            print("Please Depossit the Amount in Cash Tray & Collect the Purchased Products from the Basket\n")
            input("Press Enter to continue.....!!!!\n")
            con.close()
            break
        
        elif ch==4:
            con.close()
            Main_Program()
            break
        
        else:
            print("Invalid Input....!!!")

    
    
#_____MAIN_____
def Main_Program():
    #os.system("cls")
    while True:
        WELCOME_SCREEN()
        print("Querys For Canteen Staff Only")
        print("1-Get to Customer Details System")
        print("2-Update Product Details")
        print("3-Update staff password\n\n")

        print("Querys For Customers")
        print("4-See the Products Available in Canteen")
        print("5-To Buy a Product")
        print("6-Exit Canteen Management System\n\n")
        ch=int(input("What Would You Like to Do :\n"))
        if ch==1:
            Customer_Details()
        elif ch==2:
            Update_Product_Details()
        elif ch==3:
            update_staff_passwords()
        elif ch==4:
            Products_Available()
        elif ch==5:
            Buy_Product()
        elif ch==6:
            break
        # invalid input
        else:
            print("Invalid Input....!!!!")
    print("THANK YOU FOR USING CANTEEN MANAGEMENT SYSTEM    \n\n \t\t*******BYE*******")
Main_Program()
