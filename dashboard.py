from tkinter import *
from PIL import Image,ImageTk
from employee import employeeclass
from supplier import supplierclass
from category import categoryclass
from product import  productclass
from sales import salesclass
import sqlite3
from tkinter import messagebox
import os
import time
class sms:
    def __init__(self,root):
        self.root=root
        self.root.attributes('-fullscreen', True)
        self.root.title("STORE MANAGEMENT SYSTEM | Develpoed by Gowtham")
        
        #title
        self.icon_title=PhotoImage(file='images/logo1.png')
        title=Label(self.root,text="Store Management System",image=self.icon_title,font=("times new roman",40,"bold"),bg="#010c49",fg="white",anchor="w",padx=20,compound=LEFT).place(x=0,y=0,relwidth=1,height=70)
        
        #button logout
        self.logotlogo = PhotoImage(file='images/button_logout.png')
        Button_logout=Button(self.root,text="Logout",command=self.logout,image=self.logotlogo,border=0,cursor="hand2",bg='#010c49',activebackground='#010c49').place(x=1350,y=1)

        #time_tab==hedder
        self.lbl_clock=Label(self.root,border=5,relief=RIDGE,text="Welcome to Store Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman",15),bg="#4d636d",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        #left_menu
        self.leftmenulogo = PhotoImage(file="images\logo2.png")

        leftmenu=Frame(self.root,bg="white",bd=5,relief=RIDGE)
        leftmenu.place(x=0,y=102,width=200,height=565)

        Label_menulogo=Label(leftmenu,image=self.leftmenulogo)
        Label_menulogo.pack(side=TOP,fill=X)

        #lable menu left
        Lable_menu=Label(leftmenu,text="Menu",font=("times new roman",20),bg="#009688").pack(side=TOP,fill=X)
    
       #button_employee
        self.Employeelogo = PhotoImage(file='images\point.png')
        button_employee=Button(leftmenu,text="Employee",image=self.Employeelogo,command=self.emplopyee,compound=LEFT,bg='#FFEBCD',padx=5,anchor='w',font=("times new roman",20,"bold"),bd=3,cursor='hand2').pack(side=TOP,fill=X)

       #button_supplier
        self.supplierlogo = PhotoImage(file="images\supplylogo.png")
        button_employee=Button(leftmenu,text="Supplier",command=self.supplier,image=self.supplierlogo,compound=LEFT,bg='pink',padx=5,anchor='w',font=("times new roman",20,"bold"),bd=3,cursor='hand2').pack(side=TOP,fill=X)
    
      #button_category
        self.categorylogo = PhotoImage(file='images\categorylogo.png')
        button_category=Button(leftmenu,text="Category",command=self.category,image=self.categorylogo,compound=LEFT,bg='pink',padx=5,anchor='w',font=("times new roman",20,"bold"),bd=3,cursor='hand2').pack(side=TOP,fill=X)

      #button_Product
        self.Productlogo = PhotoImage(file='images\productlogo.png')
        button_Product=Button(leftmenu,text="Product",command=self.product,image=self.Productlogo,compound=LEFT,bg='pink',padx=5,anchor='w',font=("times new roman",20,"bold"),bd=3,cursor='hand2').pack(side=TOP,fill=X)

      #button_Sales
        self.saleslogo = PhotoImage(file='images\saleslogo.png')
        button_Sales=Button(leftmenu,text="Sales",command=self.sales  ,image=self.saleslogo,compound=LEFT,bg='pink',padx=5,anchor='w',font=("times new roman",20,"bold"),bd=3,cursor='hand2').pack(side=TOP,fill=X)

      #button_exit
        self.exitlogo = PhotoImage(file='images\exitlogo.png')
        button_exit=Button(leftmenu,text="Exit",image=self.exitlogo,compound=LEFT,bg='pink',padx=5,anchor='w',font=("times new roman",20,"bold"),bd=3,cursor='hand2').pack(side=TOP,fill=X)

      #content_employee
        self.lable_employee=Label(self.root,text='Total Employees\n[ 0 ]',bd=5,relief=SOLID,bg='orange',fg='white',font=('goudy old style',20,"bold"))
        self.lable_employee.place(x=300,y=120,height=150,width=300)

     #content_supplier
        self.lable_supplier=Label(self.root,text='Total Suppliers\n[ 0 ]',bd=5,relief=SOLID,bg='orange',fg='white',font=('goudy old style',20,"bold"))
        self.lable_supplier.place(x=650,y=120,height=150,width=300)

     #content_category
        self.lable_category=Label(self.root,text='Total Categories\n[ 0 ]',bd=5,relief=SOLID,bg='orange',fg='white',font=('goudy old style',20,"bold"))
        self.lable_category.place(x=1000,y=120,height=150,width=300)

     #content_product
        self.lable_product=Label(self.root,text='Total Products\n[ 0 ]',bd=5,relief=SOLID,bg='orange',fg='white',font=('goudy old style',20,"bold"))
        self.lable_product.place(x=300,y=300,height=150,width=300)

     #content_sales
        self.lable_sales=Label(self.root,text='Total Sales\n[ 0 ]',bd=5,relief=SOLID,bg='orange',fg='white',font=('goudy old style',20,"bold"))
        self.lable_sales.place(x=650,y=300,height=150,width=300)

     #fotter
        self.fotter=Label(self.root,border=5,relief=RIDGE,text='SMS-Store Management System | Developed by Gowtham\nFor any Technical Issue Contact : 1234567891',font=('times new roman',12),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X)
        
        self.update_content()
#=================================================================================================================================================================================================================================================
    #emplopyee_fun
    def emplopyee(self):
      self.new_win=Toplevel(self.root)
      self.new_obj=employeeclass(self.new_win)
    
    #supplier_fun
    def supplier(self):
      self.new_win=Toplevel(self.root)
      self.new_obj=supplierclass(self.new_win)

    #category_fun
    def category(self):
      self.new_win=Toplevel(self.root)
      self.new_obj=categoryclass(self.new_win)

    #product_fun
    def product(self):
      self.new_win=Toplevel(self.root)
      self.new_obj=productclass(self.new_win)
    
    #sales_fun
    def sales(self):
      self.new_win=Toplevel(self.root)
      self.new_obj=salesclass(self.new_win)
    
    
    #to config lbls in dashboard
    def update_content(self):
      con=sqlite3.connect(database=r'sms.db')
      cur=con.cursor()
      try:
        cur.execute('select * from product')
        product=cur.fetchall()
        self.lable_product.config(text=f'Total Products\n[ {str(len(product))} ]')
        
        cur.execute('select * from supplier')
        supplier=cur.fetchall()
        self.lable_supplier.config(text=f'Total Suppliers\n[ {str(len(supplier))} ]')
        
        cur.execute('select * from category')
        categories=cur.fetchall()
        self.lable_category.config(text=f'Total Categories\n[ {str(len(categories))} ]')
        
        cur.execute('select * from employee')
        employee=cur.fetchall()
        self.lable_employee.config(text=f'Total Employees\n[ {str(len(employee))} ]')
        
        #to update sales
        bill=len(os.listdir('bill'))
        self.lable_sales.config(text=f'Total Sales\n [{str(bill)}]')
       
        #time and date
        time_=time.strftime("%I:%M:%S")
        date_=time.strftime("%d-%m-%y")
        self.lbl_clock.config(text=f"Welcome to Store Management System\t\t Date: {str(date_)}\t\t Time: {str(time_)}")
        self.lbl_clock.after(200,self.update_content)
      except Exception as msg:
        messagebox.showerror('ERROR',f'Error due to : {str(msg)}',parent=self.root)


    #logout function
    def logout(self):
      self.root.destroy()
      os.system("python login.py")


if __name__=='__main__':
  root=Tk()
  obj=sms(root)
  root.mainloop()