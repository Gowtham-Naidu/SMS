from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
import time
import os
import tempfile
class billclass:
    def __init__(self,root):
        self.root=root
        self.root.attributes('-fullscreen', True)
        self.root.title("STORE MANAGEMENT SYSTEM | Develpoed by Gowtham")
        
        self.cart_list=[]
        self.chk_print=0
        
        #title
        self.icon_title=PhotoImage(file='images/logo1.png')
        title=Label(self.root,text="Store Management System",image=self.icon_title,font=("times new roman",40,"bold"),bg="#010c49",fg="white",anchor="w",padx=20,compound=LEFT).place(x=0,y=0,relwidth=1,height=70)
        
        #button logout
        self.logotlogo = PhotoImage(file='images/button_logout.png')
        Button_logout=Button(self.root,text="Logout",command=self.logout,image=self.logotlogo,border=0,cursor="hand2",bg='#010c49',activebackground='#010c49').place(x=1350,y=1)

        #time_tab==hedder
        self.lbl_clock=Label(self.root,bd=5,relief=RIDGE,text="Welcome to Store Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman",15),bg="black",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)
#####################################################################
        #product_frame1
        #variables
        self.var_search=StringVar()


        product_frame1=Frame(self.root,bd=4,relief=RIDGE,bg='white')
        product_frame1.place(x=6,y=110,width=410,height=700)

        #title_product
        pro_title=Label(product_frame1,text="All Products",font=('goudy old style',20,'bold'),bg='#262626',fg='white').pack(side=TOP,fill=X)

        #product_frame2_search_frame
        product_frame2=Frame(product_frame1,bd=4,relief=RIDGE,bg='white')
        product_frame2.place(x=2,y=42,width=398,height=90)

        #tilte_lbl_search_product
        lbl_search_pro=Label(product_frame2,text="Search Product |By Name",font=('goudy old style',15,'bold'),bg='white',fg='green').place(x=2,y=5)

        lbl_search=Label(product_frame2,text="Product Name",font=('goudy old style',15,'bold'),bg='white').place(x=5,y=45)
        
        txt_search=Entry(product_frame2,textvariable=self.var_search,font=('goudy old style',15),bg='yellow').place(x=130,y=47,width=150,height=22)
        
        #button_search
        button_search=Button(product_frame2,command=self.search,text="Search",cursor="hand2",font=('goudy old style',15),bg="#2196f3",fg="white").place(x=285,y=45,width=100,height=25)

        #button_showall
        button_search=Button(product_frame2,command=self.show,text="Show All",cursor="hand2",font=('goudy old style',15),bg="#083531",fg="white").place(x=285,y=10,width=100,height=25)


        
        #tree_view
        product_frame3 =Frame(product_frame1,bd=3,relief=RIDGE)
        product_frame3 .place(x=2,y=140,width=398,height=520)


        #scroll=y
        scrolly=Scrollbar(product_frame3 ,orient=VERTICAL)
        #scroll=x
        scrollx=Scrollbar(product_frame3 ,orient=HORIZONTAL)



        #treeview=table
        self.product_table=ttk.Treeview(product_frame3,columns=('pid','name','price','qty','status'),yscrollcommand=scrolly,xscrollcommand=scrollx)
        self.product_table.config(cursor='hand2')
        #scrollbar packing
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.product_table.xview,cursor='hand2')
        scrolly.config(command=self.product_table.yview,cursor='hand2')

        self.product_table.heading('pid',text='PID NO.')    
        self.product_table.heading('name',text='NAME')
        self.product_table.heading('price',text='PRICE')
        self.product_table.heading('qty',text='QTY')
        self.product_table.heading('status',text='STATUS')

        
        
        self.product_table['show']='headings'

        self.product_table.column('pid',width=50)    
        self.product_table.column('name',width=100)
        self.product_table.column('price',width=100)
        self.product_table.column('qty',width=40)
        self.product_table.column('status',width=90)
       
        

        self.product_table.pack(fill=BOTH,expand=1)
        self.product_table.bind('<ButtonRelease-1>',self.get_data)

        #lbl_note
        lbl_note=Label(product_frame1,text='NOTE:"Enter 0 Qunatity to remove product from the cart"',font=('goudy old style',12),anchor='w',bg='white',fg='red').pack(side=BOTTOM,fill=X)

 ##########################################################################       

        #custorem_frame
        #variables
        self.var_cname=StringVar()
        self.var_contact=StringVar()

        customer_frame=Frame(self.root,bd=4,relief=RIDGE,bg='white')
        customer_frame.place(x=420,y=110,width=570,height=700)

        #customer_title
        cus_title=Label(customer_frame,text="Customer Details",font=('goudy old style',15),bg='lightgray').pack(side=TOP,fill=X)

        #lbl_name
        lbl_name=Label(customer_frame,text="Name",font=('goudy old style',15),bg='white').place(x=5,y=35)
        
        txt_name=Entry(customer_frame,textvariable=self.var_cname,font=('goudy old style',13),bg='yellow').place(x=65,y=35,width=190)
        
        #lbl_contact
        lbl_contact=Label(customer_frame,text="Contact No.",font=('goudy old style',15),bg='white').place(x=270,y=35)
        
        txt_contact=Entry(customer_frame,textvariable=self.var_contact,font=('goudy old style',13),bg='yellow').place(x=380,y=35,width=130)
        
##########################################################################
        #cal_fram_cart_frame
        #varables
        self.var_cla_input=StringVar()

        cal_cart_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        cal_cart_frame.place(x=420,y=250,width=570,height=360)
        
        #cal_frame
        cal_frame=Frame(cal_cart_frame,bd=9,relief=RIDGE,bg='white')
        cal_frame.place(x=5,y=10,width=268,height=340)

        #calculator
        txt_cal_input=Entry(cal_frame,textvariable=self.var_cla_input,font=('arial',15,"bold"),width=21,bd=10,relief=GROOVE,state='readonly',justify=RIGHT)
        txt_cal_input.grid(row=0,columnspan=4)

        btn_7=Button(cal_frame,command=lambda:self.get_input(7),text='7',font=('arial',15,"bold"),bd=5,width=4,pady=10,cursor="hand2",bg="#c7605e").grid(row=1,column=0)
        btn_8=Button(cal_frame,command=lambda:self.get_input(8),text='8',font=('arial',15,"bold"),bd=5,width=4,pady=10,cursor="hand2",bg="#c7605e").grid(row=1,column=1)
        btn_9=Button(cal_frame,command=lambda:self.get_input(9),text='9',font=('arial',15,"bold"),bd=5,width=4,pady=10,cursor="hand2",bg="#c7605e").grid(row=1,column=2)
        button_sum=Button(cal_frame,text='+',command=lambda:self.get_input('+'),font=('arial',15,"bold"),bd=5,width=4,pady=10,cursor="hand2",bg="#c7605e").grid(row=1,column=3)

        btn_4=Button(cal_frame,text='4',command=lambda:self.get_input(4),font=('arial',15,"bold"),bd=5,width=4,pady=10,cursor="hand2",bg="#c7605e").grid(row=2,column=0)
        btn_5=Button(cal_frame,text='5',command=lambda:self.get_input(5),font=('arial',15,"bold"),bd=5,width=4,pady=10,cursor="hand2",bg="#c7605e").grid(row=2,column=1)
        btn_6=Button(cal_frame,text='6',command=lambda:self.get_input(6),font=('arial',15,"bold"),bd=5,width=4,pady=10,cursor="hand2",bg="#c7605e").grid(row=2,column=2)
        button_sub=Button(cal_frame,text='-',command=lambda:self.get_input('-'),font=('arial',15,"bold"),bd=5,width=4,pady=10,cursor="hand2",bg="#c7605e").grid(row=2,column=3)

        btn_1=Button(cal_frame,text='1',command=lambda:self.get_input(1),font=('arial',15,"bold"),bd=5,width=4,pady=10,cursor="hand2",bg="#c7605e").grid(row=3,column=0)
        btn_2=Button(cal_frame,text='2',command=lambda:self.get_input(2),font=('arial',15,"bold"),bd=5,width=4,pady=10,cursor="hand2",bg="#c7605e").grid(row=3,column=1)
        btn_3=Button(cal_frame,text='3',command=lambda:self.get_input(3),font=('arial',15,"bold"),bd=5,width=4,pady=10,cursor="hand2",bg="#c7605e").grid(row=3,column=2)
        button_mul=Button(cal_frame,text='*',command=lambda:self.get_input('*'),font=('arial',15,"bold"),bd=5,width=4,pady=10,cursor="hand2",bg="#c7605e").grid(row=3,column=3)

        btn_0=Button(cal_frame,text='0',command=lambda:self.get_input(0),font=('arial',15,"bold"),bd=5,width=4,pady=15,cursor="hand2",bg="#c7605e").grid(row=4,column=0)
        btn_c=Button(cal_frame,text='C',command=self.Clear_cal,font=('arial',15,"bold"),bd=5,width=4,pady=15,cursor="hand2",bg="#c7605e").grid(row=4,column=1)
        btn_equl=Button(cal_frame,text='=',command=self.perform_cal,font=('arial',15,"bold"),bd=5,width=4,pady=15,cursor="hand2",bg="#c7605e").grid(row=4,column=2)
        button_div=Button(cal_frame,text='/',command=lambda:self.get_input('/'),font=('arial',15,"bold"),bd=5,width=4,pady=15,cursor="hand2",bg="#c7605e").grid(row=4,column=3)
        
        #tree_view
        cart_frame =Frame(cal_cart_frame,bd=3,relief=RIDGE)
        cart_frame .place(x=280,y=8,width=280,height=350)

        #total_product_lbl
        self.cart_title=Label(cart_frame,text="Cart \t Total Product: [0]",font=('goudy old style',15),bg='#f44336')
        self.cart_title.pack(side=TOP,fill=X)



        #scroll=y
        scrolly=Scrollbar(cart_frame ,orient=VERTICAL)
        #scroll=x
        scrollx=Scrollbar(cart_frame ,orient=HORIZONTAL)



        #treeview=table
        self.cart_table=ttk.Treeview(cart_frame,columns=('pid','name','price','qty'),yscrollcommand=scrolly,xscrollcommand=scrollx)
        self.cart_table.config(cursor='hand2')
        #scrollbar packing
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.cart_table.xview,cursor='hand2')
        scrolly.config(command=self.cart_table.yview,cursor='hand2')

        self.cart_table.heading('pid',text='PID')    
        self.cart_table.heading('name',text='NAME')
        self.cart_table.heading('price',text='PRICE')
        self.cart_table.heading('qty',text='QTY')
        

        
        
        self.cart_table['show']='headings'

        self.cart_table.column('pid',width=40)    
        self.cart_table.column('name',width=90)
        self.cart_table.column('price',width=90)
        self.cart_table.column('qty',width=30)
      
       
        

        self.cart_table.pack(fill=BOTH,expand=1)
        self.cart_table.bind('<ButtonRelease-1>',self.get_data_cart) #bind method

        #add_cart_frame
        #varables
        self.var_pid=StringVar()
        self.var_pname=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_stock=StringVar()



        add_cart_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        add_cart_frame.place(x=420,y=700,width=570,height=110)

        #pname
        lbl_pname=Label(add_cart_frame,text="Product Name",font=('times new roman',15),bg='white').place(x=5,y=5)

        txt_pname=Entry(add_cart_frame,textvariable=self.var_pid,font=('times new roman',15),bg='yellow',state='readonly').place(x=5,y=35,width=190,height=22)

        #price
        lbl_p_price=Label(add_cart_frame,text="Price per Qty",font=('times new roman',15),bg='white').place(x=230,y=5)

        txt_p_price=Entry(add_cart_frame,textvariable=self.var_price,font=('times new roman',15),bg='yellow',state='readonly').place(x=230,y=35,width=150,height=22)
        
        #qty
        lbl_p_qty=Label(add_cart_frame,text="Quantity",font=('times new roman',15),bg='white').place(x=390,y=5)

        txt_p_qty=Entry(add_cart_frame,textvariable=self.var_qty,font=('times new roman',15),bg='yellow').place(x=390,y=35,width=160,height=22)
        
        #stock
        self.lbl_instock=Label(add_cart_frame,text="In Stock",font=('times new roman',15),bg='white')
        self.lbl_instock.place(x=5,y=70)

        #clear_button
        button_clear=Button(add_cart_frame,text="Clear",command=self.clear_cart,font=('times new roman',15,'bold'),bg='gray',cursor="hand2").place(x=230,y=70,width=150,height=30)

        #add
        button_add=Button(add_cart_frame,command=self.add_uodate_cart,text="Add | Update Cart",font=('times new roman',15,'bold'),bg='orange',cursor="hand2").place(x=385,y=70,width=180,height=30)
##############################################################################################################
#billing_arear
        bill_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        bill_frame.place(x=1000,y=110,height=410,width=520)

        #bill_title
        bill_title=Label(bill_frame,text="Customer Bill Area",font=('goudy old style',20,"bold"),bg='#f44336',fg="white").pack(side=TOP,fill=X)

        scrolly=Scrollbar(bill_frame,orient=VERTICAL,cursor="hand2")
        scrolly.pack(side=RIGHT,fill=Y)

        self.txt_bill_area=Text(bill_frame,yscrollcommand=scrolly.set)
        self.txt_bill_area.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.txt_bill_area.yview)


        #billing_buttons
        bill_menu_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        bill_menu_frame.place(x=1000,y=520,height=290,width=520)

        #lbl_ammount
        self.lbl_ammonut=Label(bill_menu_frame,text="Bill Amount \n[0]",font=('goudy old style',15,"bold"),bg="blue",fg="white",bd=2,relief=RIDGE)
        self.lbl_ammonut.place(x=2,y=130,width=140,height=90)

        #lbl_discount
        self.lbl_discount=Label(bill_menu_frame,text="Discount \n[5%]",font=('goudy old style',15,"bold"),bg="#8bc34A",fg="white",bd=2,relief=RIDGE)
        self.lbl_discount.place(x=174,y=130,width=140,height=90)

        #lbl_netpay
        self.lbl_netpay=Label(bill_menu_frame,text="Net Pay \n[0]",font=('goudy old style',15,"bold"),bg="#607d8B",fg="white",bd=2,relief=RIDGE)
        self.lbl_netpay.place(x=340,y=130,width=160,height=90)

        #button_print
        button_print=Button(bill_menu_frame,command=self.print_bill,text="Print",font=('times new roman',15,'bold'),bg='lightgreen',cursor="hand2").place(x=2,y=230,width=140,height=50)

        #button_clear
        button_clear_all=Button(bill_menu_frame,command=self.clear_all,text="Clear All",font=('times new roman',15,'bold'),bg='gray',cursor="hand2").place(x=174,y=230,width=140,height=50)
        
        #button_generate
        button_genrate=Button(bill_menu_frame,command=self.generate_bill,text="Gen/Save Bill",font=('times new roman',15,'bold'),bg='#009688',cursor="hand2").place(x=340,y=230,width=160,height=50)

        #fotter
        self.fotter=Label(self.root,border=5,relief=RIDGE,text='SMS-Store Management System | Developed by Gowtham\nFor any Technical Issue Contact : 1234567891',font=('times new roman',10),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X)

        self.show()
        #self.bill_top()
        self.update_date_time()
###################functions######################################################
    def get_input(self,num):
        xnum=self.var_cla_input.get()+str(num)
        self.var_cla_input.set(xnum)

    def Clear_cal(self):
        self.var_cla_input.set('') 

    def perform_cal(self):
        result=self.var_cla_input.get() 
        self.var_cla_input.set(eval(result))   



    #show fuction
    def show(self):
      con=sqlite3.connect(database=r'sms.db')
      cur=con.cursor()
      try:
        #self.cart_table=ttk.Treeview(cart_frame,columns=('pid','name','price','qty','status'),yscrollcommand=scrolly,xscrollcommand=scrollx)
        cur.execute("select pid,name,price,qty,status from product where status='Active'")
        rows=cur.fetchall()
        self.product_table.delete(*self.product_table.get_children())
        for row in rows:
          self.product_table.insert('',END,values=row)
      except Exception as msg:
        messagebox.showerror('ERROR',f'Error due to : {str(msg)}',parent=self.root)


    #search
    def search(self):
      con=sqlite3.connect(database=r'sms.db')
      cur=con.cursor()
      try:
        if self.var_search.get()=='':
          messagebox.showerror('Error','Search input should be required',parent=self.root)
        else:
          cur.execute("select pid,name,price,qty,status from product where name like '%"+ self.var_search.get()+"%' and status='Active'")
          rows=cur.fetchall()
          if len(rows)!=0:
            self.product_table.delete(*self.product_table.get_children())
            for row in rows:
              self.product_table.insert('',END,values=row)
          else:
            messagebox.showerror('Error','No Record Found',parent=self.root)
      except Exception as msg:
        messagebox.showerror('ERROR',f'Error due to : {str(msg)}',parent=self.root)


    #to get data
    def get_data(self,ev):
        f=self.product_table.focus()
        content=(self.product_table.item(f))
        row=content['values']
        
        self.var_pid.set(row[1])
        self.var_pname.set(row[0])
        self.var_price.set(row[2])
        self.lbl_instock.config(text=f'In Stock [{str(row[3])}]')
        self.var_stock.set(row[3])
        self.var_qty.set('1')
    
    #to get_data_cart
    def get_data_cart(self,ev):
        f=self.cart_table.focus()
        content=(self.cart_table.item(f))
        row=content['values']
        
        self.var_pid.set(row[1])
        self.var_pname.set(row[0])
        self.var_price.set(row[2])
        self.lbl_instock.config(text=f'In Stock [{str(row[4])}]')
        self.var_stock.set(row[4])
        self.var_qty.set(row[3])

    #cart add function
    def add_uodate_cart(self):
        if self.var_pid.get()=='':
            messagebox.showerror('Error','Please Select Product From The List')
        elif self.var_qty.get()=='':
            messagebox.showerror('Error','Quantity is Required!!!',parent=self.root)
        elif int(self.var_qty.get())>int(self.var_stock.get()):
            messagebox.showerror('Error','Invalid Quantity!!!',parent=self.root)
        else:
            #price_cal=float(int(self.var_qty.get())*float(self.var_price.get()))
            price_cal=self.var_price.get()
            
            #print(price_cal)
            #pid,name,price,qty,stock
            cart_data=[self.var_pname.get(),self.var_pid.get(),price_cal,self.var_qty.get(), self.var_stock.get()]
            
            #print(self.cart_list)
            #updatecart checking
            present='no'
            index_=0
            for row in self.cart_list:
                if self.var_pid.get()==row[1]:
                    present='Yes'
                    break
                index_+=1
            #print(present,index_)
            if present=='Yes':
                op=messagebox.askyesno('Confirm','Product already Present\nDo you want to Update| Remove from the cart List',parent=self.root)
                if op==True:
                    if self.var_qty.get()=='0':
                            self.cart_list.pop(index_)
                    else:
                        #self.cart_list[index_][2]=price_cal #price update
                        self.cart_list[index_][3]=self.var_qty.get() #qty update
            else:
                self.cart_list.append(cart_data)            
            self.show_cart()
            self.bill_updates()
            
            
    #bill updates
    def bill_updates(self):
        self.bill_amnt=0
        self.net_pay=0
        self.discount=0
        for row in self.cart_list:
            self.bill_amnt=self.bill_amnt+(float(row[2])*int(row[3]))
        
        self.discount=(self.bill_amnt*5)/100  ##discount##
        self.net_pay=self.bill_amnt-self.discount 
        
        self.lbl_ammonut.config(text=f'Bill Amnt.\n{str(self.bill_amnt)}')
        self.lbl_netpay.config(text=f'Net Amount.\n{str(self.net_pay)}')
        self.cart_title.config(text=f"Cart \t Total Product: [{str(len(self.cart_list))}]")
   
    #to show data in cart
    def show_cart(self):
        try:
            self.cart_table.delete(*self.cart_table.get_children())
            for row in self.cart_list:
                self.cart_table.insert('',END,values=row)
        except Exception as msg:
            messagebox.showerror('ERROR',f'Error due to : {str(msg)}',parent=self.root)

    #to gen bill
    def generate_bill(self):
        if self.var_cname.get()=='' or self.var_contact.get()=='':
            messagebox.showerror('ERROR','Customer Details are Required',parent=self.root)
        elif len(self.cart_list)==0:
            messagebox.showerror('ERROR','Please Add Product To The Cart',parent=self.root)
        else:
            #bill top
            self.bill_top()
            #bill middle
            self.bill_middle()
            #bill bottom
            self.bill_bottom()
            
            #to save the bill in bill folder
            fp=open(f'bill/{str(self.invoice)}.txt','w')
            fp.write(self.txt_bill_area.get('1.0',END))
            fp.close()
            messagebox.showinfo('Saved','Bill has been generated/saved in Backend',parent=self.root)
            self.chk_print=1
            
    #top part of the bill
    def bill_top(self):
        self.invoice=int(time.strftime('%H%M%S'))+int(time.strftime('%d%m%y')) #to gen invoice number which will be unique
        #print(invoice)
        bill_top_temp=f'''
 \t\txyz-Store
\t Phone No. 912345678,bangalore-560038
{str('='*46)}
 Customer Name: {self.var_cname.get()}
 Ph no.       :{self.var_contact.get()}
 Bill  No. {str(self.invoice)}\t\t\tDate: {str(time.strftime("%d/%m/%y"))}
{str("="*46)}
 Product Name\t\t\tQTY\tPrice
{str("="*46)}
            
        '''
        self.txt_bill_area.delete("1.0",END)      
        self.txt_bill_area.insert('1.0',bill_top_temp)
    
    
    #bottom part of the bill
    def bill_bottom(self):
        bill_bottom_temp=f'''
{str('='*46)}
 Bill Amount\t\t\t\tRs.{self.bill_amnt}
 Discount\t\t\t\tRs.{self.discount}
 Net Pay\t\t\t\tRs.{self.net_pay}
{str("="*46)}\n
    
        '''
        self.txt_bill_area.insert(END,bill_bottom_temp)
    

    #middle part of bill
    def bill_middle(self):
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
            for row in self.cart_list:
                pid=row[0]
                name=row[1]
                qty=int(row[4])-int(row[3])
                
                if int(row[3])==int(row[4]):
                    status='Inactive'
                if int(row[3])!=int(row[4]):
                    status='Active'
                    
                price=float(row[2])*int(row[3])
                price=str(price)
                self.txt_bill_area.insert(END,"\n"+name+"\t\t\t"+ row[3]+"\tRs."+ price)

                #update qty after billing in product table
                cur.execute('update product set qty=?,status=? where pid=?',(
                    qty,
                    status,
                    pid
                    
                ))
                con.commit()
            con.close()
            self.show()
        except Exception as msg:
            messagebox.showerror('ERROR',f'Error due to : {str(msg)}',parent=self.root)

  
    #clear cart
    def clear_cart(self):
        self.var_pid.set('')
        self.var_pname.set('')
        self.var_price.set('')
        self.lbl_instock.config(text=f'In Stock')
        self.var_stock.set('')
        self.var_qty.set('')
     
     
    #clear all
    def clear_all(self):
        del self.cart_list[:]
        self.var_cname.set('')
        self.var_contact.set('')
        self.txt_bill_area.delete('1.0',END)
        self.cart_title.config(text=f"Cart \t Total Product: [0]")
        self.var_search.set('')
        self.clear_cart()
        self.show()
        self.show_cart()
        self.chk_print=0
        
    #to show date and time
    def update_date_time(self):
        time_=time.strftime("%I:%M:%S")
        date_=time.strftime("%d-%m-%y")
        self.lbl_clock.config(text=f"Welcome to Store Management System\t\t Date: {str(date_)}\t\t Time: {str(time_)}")
        self.lbl_clock.after(200,self.update_date_time)
 
     #to print bill
    def print_bill(self):
        if self.chk_print==1:
            messagebox.showinfo('Print','Please Wait While Printing',parent=self.root)         
            #printing
            new_file=tempfile.mkdtemp('.txt')
            open(new_file,'w').write(self.txt_bill_area.get('1.0',END))
            os.startfile(new_file,'Print')

        else:
            messagebox.showerror('Print','Please Generate Bill,To Print the Receipt',parent=self.root)         
            

    #logout
    def logout(self):
        self.root.destroy()
        os.system("python login.py")



if __name__=='__main__':
  root=Tk()
  obj=billclass (root)
  root.mainloop()