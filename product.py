from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class productclass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("STORE MANAGEMENT SYSTEM | Develpoed by Gowtham")
        self.root.config(bg='white')
        self.root.focus_force()
        #################################variables
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()

        self.cat_list=[]
        self.sup_list=[]
        self.fetch_cat_sup()

        self.var_pid=StringVar()
        self.var_cat=StringVar()
        self.var_sup=StringVar()
        self.var_name=StringVar()
        self.var_prize=StringVar()
        self.var_qty=StringVar()
        self.var_status=StringVar()
        

        ################################
        #product_frame

        product_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        product_frame.place(x=10,y=10,width=450,height=480)

        #title
        title=Label(product_frame,text='Manage Product Details',font=('goudy old style',18),bg='#0f4d7d',fg='white').pack(side=TOP,fill=X)

        #category_lbl
        lbl_category=Label(product_frame,text='Category',font=('goudy old style',18),bg='white').place(x=5,y=60)

        #supplier_lbl
        lbl_supplier=Label(product_frame,text='Supplier',font=('goudy old style',18),bg='white').place(x=5,y=110)

        #product_name-lbl
        lbl_product=Label(product_frame,text='Product Name',font=('goudy old style',18),bg='white').place(x=5,y=160)
        #prize_lbl
        lbl_prize=Label(product_frame,text='Prize',font=('goudy old style',18),bg='white').place(x=5,y=210)

        #quantity_lbl
        lbl_quantity=Label(product_frame,text='Quantity',font=('goudy old style',18),bg='white').place(x=5,y=260)

        #status_lbl
        lbl_status=Label(product_frame,text='Status',font=('goudy old style',18),bg='white').place(x=5,y=310)


        #entery_fileds_for_above
        cmb_cat=ttk.Combobox(product_frame,textvariable=self.var_cat,cursor='hand2',values=self.cat_list,state='readonly',justify=CENTER,font=('gody old style',15))
        cmb_cat.place(x=150,y=60,width=200)
        cmb_cat.current(0)



        cmb_sup=ttk.Combobox(product_frame,textvariable=self.var_sup,cursor='hand2',values=self.sup_list,state='readonly',justify=CENTER,font=('gody old style',15))
        cmb_sup.place(x=150,y=110,width=200)
        cmb_sup.current(0)
        #name
        txt_name=Entry(product_frame,textvariable=self.var_name,bg='yellow',font=('gody old style',15)).place(x=150,y=160,width=200)
        
        txt_price=Entry(product_frame,textvariable=self.var_prize,bg='yellow',font=('gody old style',15)).place(x=150,y=210,width=200)

        txt_qty=Entry(product_frame,textvariable=self.var_qty,bg='yellow',font=('gody old style',15)).place(x=150,y=260,width=200)

        cmb_satus=ttk.Combobox(product_frame,textvariable=self.var_status,cursor='hand2',values=('Active','Inactive'),state='readonly',justify=CENTER,font=('gody old style',15))
        cmb_satus.place(x=150,y=310,width=200)
        cmb_satus.current(0)

        #button add
        Button_add = Button(product_frame,command=self.add,text='Save',font=("goudy old style",15),cursor='hand2',bg='#2196f3',fg='white').place(x=10,y=400,width=100,height=40)

        #button update
        Button_update = Button(product_frame,command=self.update,text='Update',font=("goudy old style",15),cursor='hand2',bg='#4caf50',fg='white').place(x=120,y=400,width=100,height=40)

        #button delete
        Button_delete= Button(product_frame,command=self.delete,text='Delete',font=("goudy old style",15),cursor='hand2',bg='#f44336',fg='white').place(x=230,y=400,width=100,height=40)

        #button clear
        Button_clear = Button(product_frame,command=self.clear,text='Clear',font=("goudy old style",15),cursor='hand2',bg='#607d8b',fg='white').place(x=340,y=400,width=100,height=40)

        #searchframe

        searchframe=LabelFrame(self.root,text="Search Employee",bg='white',font=('gody old style',12,'bold'),bd=2,relief=RIDGE)
        searchframe.place(x=480,y=10,width=600,height=80)

        #search_product_combobox
        cmb_search=ttk.Combobox(searchframe,textvariable=self.var_searchby,cursor='hand2',values=('select','category','supplier','name'),state='readonly',justify=CENTER,font=('gody old style',15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        #text_searchbox
        txt_search = Entry(searchframe,textvariable=self.var_searchtxt,font=("goudy old style",15),bg='yellow',fg='black').place(x=200,y=10)

        #search_button
        Button_search = Button(searchframe,command=self.search,text='Search',font=("goudy old style",15),cursor='hand2',bg='#4caf50',fg='white').place(x=410,y=9,width=150,height=30)


        #product Details_showtable_creation

        p_frame=Frame(self.root,bd=3,relief=RIDGE)
        p_frame.place(x=480,y=100,width=600,height=390)


        #scroll=y
        scrolly=Scrollbar(p_frame,orient=VERTICAL)
        #scroll=x
        scrollx=Scrollbar(p_frame,orient=HORIZONTAL)



        #treeview=table
        self.product_table=ttk.Treeview(p_frame,columns=('pid','supplier','category','name','price','qty','status'),yscrollcommand=scrolly,xscrollcommand=scrollx)
        self.product_table.config(cursor='hand2')
        #scrollbar packing
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.product_table.xview,cursor='hand2')
        scrolly.config(command=self.product_table.yview,cursor='hand2')

        self.product_table.heading('pid',text='EID')    
        self.product_table.heading('category',text='CATEGORY')
        self.product_table.heading('supplier',text='SUPPLIER')
        self.product_table.heading('name',text='NAME')
        self.product_table.heading('price',text='PRICE')
        self.product_table.heading('qty',text='QTY')
        self.product_table.heading('status',text='STATUS')
        
        
        self.product_table['show']='headings'

        self.product_table.column('pid',width=90)    
        self.product_table.column('category',width=100)
        self.product_table.column('supplier',width=100)
        self.product_table.column('name',width=100)
        self.product_table.column('price',width=100)
        self.product_table.column('qty',width=100)
        self.product_table.column('status',width=100)
       
        self.product_table.pack(fill=BOTH,expand=1)
        self.product_table.bind('<ButtonRelease-1>',self.get_data)

        self.show()
       


    #===================================================================================

    # function to fetch category and supplier
    def fetch_cat_sup(self):
        self.cat_list.append('Empty')
        self.sup_list.append('Empty')
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
            cur.execute('select name from category')
            cat=cur.fetchall()
            if len(cat)>0:
                del self.cat_list[:]
                self.cat_list.append('Select')
                for i in cat:
                    self.cat_list.append(i[0])
            
            cur.execute('select name from supplier')
            sup=cur.fetchall()
            if len(sup)>0:
                del self.sup_list[:]
                self.sup_list.append('Select')
                for i in sup:
                    self.sup_list.append(i[0])
            

        except Exception as msg:
            messagebox.showerror('ERROR',f'Error due to : {str(msg)}',parent=self.root)

    # add function
    def add(self):
      con=sqlite3.connect(database=r'sms.db')
      cur=con.cursor()
      try:
        if self.var_cat.get()=='Select' or self.var_cat.get()=='Empty' or self.var_sup.get()=='Select' or self.var_name.get()=='':
          messagebox.showerror('Error','All Fields be required',parent=self.root)
        else:
          cur.execute('select * from product where name=?',(self.var_name.get(),))
          row=cur.fetchone()
          if row!=None:
            messagebox.showerror('Error','Product already Present,try diffrent',parent=self.root)

          else:
            cur.execute('insert into product (category,supplier,name,price,qty,status) values(?,?,?,?,?,?)',(
                      self.var_cat.get(),
                      self.var_sup.get(),
                      self.var_name.get(),
                      self.var_prize.get(),
                      self.var_qty.get(),
                      self.var_status.get(),
            ))
            con.commit()
            messagebox.showinfo('Success','Product Addedd Successfully',parent=self.root)
            self.show()
      except Exception as msg:
        messagebox.showerror('ERROR',f'Error due to : {str(msg)}',parent=self.root)
      
    #data_show
    def show(self):
      con=sqlite3.connect(database=r'sms.db')
      cur=con.cursor()
      try:
        cur.execute('select * from product')
        rows=cur.fetchall()
        self.product_table.delete(*self.product_table.get_children())
        for row in rows:
          self.product_table.insert('',END,values=row)
      except Exception as msg:
        messagebox.showerror('ERROR',f'Error due to : {str(msg)}',parent=self.root)

    #to get data
    def get_data(self,ev):
        f=self.product_table.focus()
        content=(self.product_table.item(f))
        row=content['values']

        self.var_pid.set(row[0]),
        self.var_cat.set(row[2]),
        self.var_sup.set(row[1]),
        self.var_name.set(row[3]),
        self.var_prize.set(row[4]),
        self.var_qty.set(row[5]),
        self.var_status.set(row[6]),
        

    #update
    def update(self):
      con=sqlite3.connect(database=r'sms.db')
      cur=con.cursor()
      try:
        if self.var_pid.get()=='':
          messagebox.showerror('Error','Please Select Product from List',parent=self.root)
        else:
          cur.execute('select * from product where pid=?',(self.var_pid.get(),))
          row=cur.fetchone()
          if row==None:
            messagebox.showerror('Error','Invalid Product',parent=self.root)

          else:
            where_con=self.var_pid.get()
            cur.execute("update product set category=?,supplier=?,name=?,price=?,qty=?,status=? where pid=?",(
                      
                      
                    self.var_cat.get(),
                    self.var_sup.get(),
                    self.var_name.get(),
                    self.var_prize.get(),
                    self.var_qty.get(),
                    self.var_status.get(),
                    self.var_pid.get(),
            ))
            con.commit()
            messagebox.showinfo('Success','Product Updated Successfully',parent=self.root)
            self.show()
      except Exception as msg:
        messagebox.showerror('ERROR',f'Error due to : {str(msg)}',parent=self.root)


    #delete
    def delete(self):
      con=sqlite3.connect(database=r'sms.db')
      cur=con.cursor()
      try:
        if self.var_pid.get()=='':
          messagebox.showerror('Error','Select Product From the List',parent=self.root)
        else:
          cur.execute('select * from product where pid=?',(self.var_pid.get(),))
          row=cur.fetchone()
          if row==None:
            messagebox.showerror('Error','Invalid Product',parent=self.root)

          else:
            op=messagebox.askyesno('Confirm','Do you really want to delete?',parent=self.root)
            if op==True:
              cur.execute('delete from product where pid=?',(self.var_pid.get(),))
              con.commit()
              messagebox.showinfo('Delete','Product Deleted Successfully',parent=self.root)
              self.clear()
      except Exception as msg:
        messagebox.showerror('ERROR',f'Error due to : {str(msg)}',parent=self.root)
        

    #clear
    def clear(self):
        self.var_cat.set('Select')
        self.var_sup.set('Select')
        self.var_name.set('')
        self.var_prize.set('')
        self.var_qty.set('')
        self.var_status.set('Active')
        self.var_pid.set('')
        self.var_searchtxt.set('')
        self.var_searchby.set('select')
        self.show()



    #search
    def search(self):
      con=sqlite3.connect(database=r'sms.db')
      cur=con.cursor()
      try:
        if self.var_searchby.get()=='select':
          messagebox.showerror('Error','Select Search By Opetion',parent=self.root)
        elif self.var_searchtxt.get()=='':
          messagebox.showerror('Error','Search input should be required',parent=self.root)
        else:
          cur.execute('select * from product where '+self.var_searchby.get()+" like '%"+self.var_searchtxt.get()+"%'")
          rows=cur.fetchall()
          if len(rows)!=0:
            self.product_table.delete(*self.product_table.get_children())
            for row in rows:
              self.product_table.insert('',END,values=row)
          else:
            messagebox.showerror('Error','No Record Found',parent=self.root)
      except Exception as msg:
        messagebox.showerror('ERROR',f'Error due to : {str(msg)}',parent=self.root)


    



if __name__=='__main__':
  root=Tk()
  obj=productclass(root)
  root.mainloop()