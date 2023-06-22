#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install mysql-connector-python')


# In[1]:


import mysql.connector


# In[ ]:


mydb=mysql.connector.connect(
host="localhost", 
user="root",
password="",
database="ems"
)

    
def add_employee():
    
    
    cursor=mydb.cursor()
    id1=int(input("\nEmployee Id:"))
    name=input("Employee Name:")
    dept=input("Enter Department:")
    salary=input("Enter Salary:")
    mail=input("Enter Email-id:")
    query="INSERT INTO EMPLOYEE(emp_id,emp_name,emp_dept,emp_salary,email) VALUES(%s,%s,%s,%s,%s)"
    values=(id1,name,dept,salary,mail)
    cursor.execute(query,values)
    mydb.commit()
    print("\nEmployee details added successfully!\n")
    cursor.close()
def sort_employee():
    cursor=mydb.cursor()
    print("\n1.Sort by Name\n2.Sort by Salary\n3.Sort by Department")
    choice=int(input("\nEnter your choice:"))
    if choice==1:
        query="SELECT * from EMPLOYEE ORDER BY emp_name"
        cursor.execute(query)
        result=cursor.fetchall()
        if result:
            print("\nEmployees details sorting by Name..")
            print("------------------------------------")
            for row in result:
                print("Name:",row[1])
                print("Salary:",row[2])
                print("Department:",row[3])
                print("E-mail:",row[4])
                print("------------------")
        else:
            print("No employee details in the table!")
    elif choice==2:
        query="SELECT * from EMPLOYEE ORDER BY emp_salary DESC"
        cursor.execute(query)
        result=cursor.fetchall()
        if result:
            print("\nEmployee details sorting by Salary")
            print("------------------------------------")
            for row in result:
                print("\nName:",row[1])
                print("Salary:",row[2])
                print("------------------")
        else:
            print("No employee data available!")
    elif choice==3:
        query="SELECT * from EMPLOYEE ORDER BY emp_dept"
        cursor.execute(query)
        result=cursor.fetchall()
        if result:
            print("\nEmployee details sorting by Department")
            print("------------------------------------")
            for row in result:
                print("\nName:",row[1])
                print("Department:",row[3])
                print("------------------")
        else:
            print("No employee data available!")
        cursor.close()
def filter_employee():
    cursor=mydb.cursor()
    print("\n1.Filter by Salary\n2.Fiter By department")
    choice=int(input("Enter your choice:"))
    if choice==1:
        minrange=float(input("Enter minimum salary range:"))
        maxrange=float(input("Enter maximum salary range:"))
        query="SELECT emp_name,emp_salary FROM EMPLOYEE where emp_salary BETWEEN %s and %s"
        values=(minrange,maxrange)
        cursor.execute(query,values)
    
        result=cursor.fetchall()
        if result:
            print("Employees with salary in given range")
            print("------------------------------------")
            for row in result:
                print("Name:",row[0])
                print("Salary:",row[1])
                print("------------------")
        else:
            print("No employees in this salary range!")
    elif choice==2:
        dept=input("Enter the Department:")
        query="SELECT emp_name,emp_dept FROM EMPLOYEE WHERE emp_dept=%s"
        data=(dept,)
        cursor.execute(query,data)
        result=cursor.fetchall()
        if result:
            print("\nEmployee details of department of",dept)
            print("-----------------------------------")
            for row in result:
                print("Name:",row[0])
                print("Department:",row[1])
                print("---------------------")
        else:
            print("No employees in this department!")
    else:
        print("\nInvalid choice!")
    cursor.close()
def update_employee():
    cursor=mydb.cursor()
    id1=int(input("Enter Employee Id:"))
    list_query="SELECT * FROM EMPLOYEE WHERE emp_id=%s"
    data=(id1,)
    cursor.execute(list_query,data)
    result=cursor.fetchall()
    if result:
        print("\nEmployee details:")
        print("-----------------\n")
        for row in result:
            print("Employee id:",row[0])
            print("Employee name:",row[1])
            print("Salary:",row[2])
            print("Department:",row[3])
            print("Email-id:",row[4])
            print("------------------")
    else:
        print("No matching employees found!")
    print("\nChoose the data that you want to update")
    print("1.Employee name\n2.Department\n3.Salary\n4.Emai-id\n5.Exit")
    choice=int(input("\nEnter your choice:"))
    if choice==1:
        name=input("\nEnter the new name:")
        query="UPDATE EMPLOYEE SET emp_name = %s WHERE emp_id = %s"
        values=(name,id1)
        cursor.execute(query,values)
        mydb.commit()
        print("\nEmployee name updated successfully!")
    elif choice==2:
        dept=input("\nEnter the new department name:")
        query="UPDATE employee SET emp_dept = %s WHERE emp_id = %s"
        values=(dept,id1)
        cursor.execute(query,values)
        mydb.commit()
        print("\nDepartment name updated successfully!")
    elif choice==3:
        salary=float(input("\nEnter the new salary:"))
        query="UPDATE employee SET emp_salary = %s WHERE emp_id = %s"
        values=(salary,id1)
        cursor.execute(query,values)
        mydb.commit()
        print("\nSalary updated successfully!")
    elif choice==4:
        mail=input("\nEnter the new email-id:")
        query="UPDATE employee SET email = %s WHERE emp_id = %s"
        values=(mail,id1)
        cursor.execute(query,values)
        mydb.commit()
        print("\nEmail-id updated successfully!")
    elif choice==5:
        sys.exit()
    else:
        print("\nInvalid choice!")
    cursor.close()
def delete_employee():
    cursor=mydb.cursor()
    id1=int(input("Enter Employee Id:"))
    query="DELETE from EMPLOYEE WHERE emp_id = %s"
    value=(id1,)
    cursor.execute(query,value)
    mydb.commit()
    print("\nEmployee details deleted successfully!")
    cursor.close()
def employee_details():
    cursor=mydb.cursor()
    query="SELECT * FROM EMPLOYEE"
    cursor.execute(query)
    result=cursor.fetchall()
    if result:
        print("\nEmployee details:")
        print("-----------------\n")
        for row in result:
            print("Employee id:",row[0])
            print("Employee name:",row[1])
            print("Salary:",row[2])
            print("Department:",row[3])
            print("Email-id:",row[4])
            print("------------------")
    else:
        print("No matching employees found!")
    cursor.close()
if __name__=="__main__":
    while True:
        print("\nEmployee Management system..")
        print("-------------------------------")
        print("\n---MENU---\n")
        print("1.Add new Employee")
        print("2.Update existing Employee details")
        print("3.Sort Employee details")
        print("4.Filter Employee details")
        print("5.Delete an Employee")
        print("6.List Employee details")
        print("7.Exit")
        ch=int(input("Enter your choice: "))
        if ch==1:
            add_employee()
        elif ch==2:
            update_employee()
        elif ch==3:
            sort_employee()
        elif ch==4:
            filter_employee()
        elif ch==5:
            delete_employee()
        elif ch==6:
            print("List of all employee details")
            print("----------------------------")
            employee_details()
        elif ch==7:
            break
        else:
            print("Invalid choice!Enter again!")


# 

# In[ ]:




