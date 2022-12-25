from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class supplierclass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("STORE MANAGEMENT SYSTEM | Develpoed by Gowtham")
        self.root.config(bg='white')

        self.root.focus_force()

        #all variables
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()

        self.var_sup_invoice=StringVar()
        self.var_name=StringVar()
        self.var_contact=StringVar()
        
        #searchframe

        searchframe=LabelFrame(self.root,text="Search Employee",bg='white',font=('gody old style',12,'bold'),bd=2,relief=RIDGE)
        searchframe.place(x=250,y=20,width=600,height=70)

        #search_supplier_combobox
        lbl_search=Label(searchframe,text='Search By Incoice No.',bg='white',font=('gody old style',12))
        lbl_search.place(x=10,y=10)
       

        #text_searchbox
        txt_search = Entry(searchframe,textvariable=self.var_searchtxt,font=("goudy old style",15),bg='yellow',fg='black').place(x=200,y=10)

        #search_button
        Button_search = Button(searchframe,command=self.search,text='Search',font=("goudy old style",15),cursor='hand2',bg='#4caf50',fg='white').place(x=410,y=9,width=150,height=30)


        #Supplier_title
        title=Label(self.root,text='Supplier Details',font=('goudy old style',15),bg='#0f4d7d',fg='white').place(x=50,y=100,width=1000)

        #row1
        #lbl_supplier_invoice
        Label_supplier_invoice=Label(self.root,text='Invoice No.',font=('goudy old style',15),bg='white').place(x=50,y=150)

        #txt _esupplier_invoice
        txt_supplier_invoice=Entry(self.root,textvariable=self.var_sup_invoice,font=('goudy old style',15),bg='yellow').place(x=150,y=150,width=180)

        
        


        #row2
        #lbl_supplier_name
        Label_name=Label(self.root,text='Name',font=('goudy old style',15),bg='white').place(x=50,y=190)

        
        #txt_supplier_name
        txt_name=Entry(self.root,textvariable=self.var_name,font=('goudy old style',15),bg='yellow').place(x=150,y=190,width=180)

       

        #row3
        #lbl_contact
        Label_contact=Label(self.root,text='Contact',font=('goudy old style',15),bg='white').place(x=50,y=230)

        

        #txt_contact
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=('goudy old style',15),bg='yellow').place(x=150,y=230,width=180)

        #row4
  

       
       
        


        #button add
        Button_add = Button(self.root,command=self.add,text='Save',font=("goudy old style",15),cursor='hand2',bg='#2196f3',fg='white').place(x=500,y=305,width=110,height=28)

        #button update
        Button_update = Button(self.root,command=self.update,text='Update',font=("goudy old style",15),cursor='hand2',bg='#4caf50',fg='white').place(x=620,y=305,width=110,height=28)

        #button delete
        Button_delete= Button(self.root,command=self.delete,text='Delete',font=("goudy old style",15),cursor='hand2',bg='#f44336',fg='white').place(x=740,y=305,width=110,height=28)

        #button clear
        Button_clear = Button(self.root,command=self.clear,text='Clear',font=("goudy old style",15),cursor='hand2',bg='#607d8b',fg='white').place(x=860,y=305,width=110,height=28)


        #supplier Details_showtable_creation

        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=350,relwidth=1,height=150)


        #scroll=y
        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        #scroll=x
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)



        #treeview=table
        self.suppliertable=ttk.Treeview(emp_frame,columns=('invoice','name','contact'),yscrollcommand=scrolly,xscrollcommand=scrollx)
        self.suppliertable.config(cursor='hand2')
        #scrollbar packing
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.suppliertable.xview,cursor='hand2')
        scrolly.config(command=self.suppliertable.yview,cursor='hand2')

        self.suppliertable.heading('invoice',text='INVOICE NO.')    
        self.suppliertable.heading('name',text='NAME')
        self.suppliertable.heading('contact',text='CONTACT')
        
        
        
        self.suppliertable['show']='headings'

        self.suppliertable.column('invoice',width=90)    
        self.suppliertable.column('name',width=100)
        self.suppliertable.column('contact',width=100)
       
        

        self.suppliertable.pack(fill=BOTH,expand=1)
        self.suppliertable.bind('<ButtonRelease-1>',self.get_data)

        self.show()

#===================================================================================

    # add function
    def add(self):
      con=sqlite3.connect(database=r'sms.db')
      cur=con.cursor()
      try:
        if self.var_sup_invoice.get()=='':
          messagebox.showerror('Error','Invoice No. Must be required',parent=self.root)
        else:
          cur.execute('select * from supplier where invoice=?',(self.var_sup_invoice.get(),))
          row=cur.fetchone()
          if row!=None:
            messagebox.showerror('Error','Invoice No. already assigned,try diffrent',parent=self.root)

          else:
            cur.execute('insert into supplier (invoice,name,contact) values(?,?,?)',(
                      self.var_sup_invoice.get(),
                      self.var_name.get(),
                      self.var_contact.get(),
            ))
            con.commit()
            messagebox.showinfo('Success','supplier Addedd Successfully',parent=self.root)
            self.show()
      except Exception as msg:
        messagebox.showerror('ERROR',f'Error due to : {str(msg)}',parent=self.root)
      
    #data_show
    def show(self):
      con=sqlite3.connect(database=r'sms.db')
      cur=con.cursor()
      try:
        cur.execute('select * from supplier')
        rows=cur.fetchall()
        self.suppliertable.delete(*self.suppliertable.get_children())
        for row in rows:
          self.suppliertable.insert('',END,values=row)
      except Exception as msg:
        messagebox.showerror('ERROR',f'Error due to : {str(msg)}',parent=self.root)

    #to get data
    def get_data(self,ev):
        f=self.suppliertable.focus()
        content=(self.suppliertable.item(f))
        row=content['values']
        #print(row)
        self.var_sup_invoice.set(row[0])
        self.var_name.set(row[1])
        self.var_contact.set(row[2])
        
       

    #update
    def update(self):
      con=sqlite3.connect(database=r'sms.db')
      cur=con.cursor()
      try:
        if self.var_sup_invoice.get()=='':
          messagebox.showerror('Error','Invoice Must be required',parent=self.root)
        else:
          cur.execute('select * from supplier where invoice=?',(self.var_sup_invoice.get(),))
          row=cur.fetchone()
          if row==None:
            messagebox.showerror('Error','Invalid Invoice No.',parent=self.root)

          else:
            where_con=self.var_sup_invoice.get()
            cur.execute("update supplier set name=?,contact=? where invoice=?",(
                      
                      self.var_name.get(),
                      self.var_contact.get(),
                      self.var_sup_invoice.get(),
            ))
            con.commit()
            messagebox.showinfo('Success','Supplier Updated Successfully',parent=self.root)
            self.show()
      except Exception as msg:
        messagebox.showerror('ERROR',f'Error due to : {str(msg)}',parent=self.root)


    #delete
    def delete(self):
      con=sqlite3.connect(database=r'sms.db')
      cur=con.cursor()
      try:
        if self.var_sup_invoice.get()=='':
          messagebox.showerror('Error','Invoice No. Must be required',parent=self.root)
        else:
          cur.execute('select * from supplier where invoice=?',(self.var_sup_invoice.get(),))
          row=cur.fetchone()
          if row==None:
            messagebox.showerror('Error','Invalid Invoice No.',parent=self.root)

          else:
            op=messagebox.askyesno('Confirm','Do you really want to delete?',parent=self.root)
            if op==True:
              cur.execute('delete from supplier where invoice=?',(self.var_sup_invoice.get(),))
              con.commit()
              messagebox.showinfo('Delete','Supplier Deleted Successfully',parent=self.root)
              self.clear()
      except Exception as msg:
        messagebox.showerror('ERROR',f'Error due to : {str(msg)}',parent=self.root)
        

    #clear
    def clear(self):
        self.var_sup_invoice.set('')
        self.var_name.set('')
        self.var_contact.set('')
        self.var_searchtxt.set('')
        self.show()



    #search
    def search(self):
      con=sqlite3.connect(database=r'sms.db')
      cur=con.cursor()
      try:
        if self.var_searchtxt.get()=='':
          messagebox.showerror('Error','Invoice No. should be required',parent=self.root)
        else:
          cur.execute('select * from supplier where invoice=?',(self.var_searchtxt.get(),))
          rows=cur.fetchone()
          if rows!=None:
            self.suppliertable.delete(*self.suppliertable.get_children())
            self.suppliertable.insert('',END,values=rows)
          else:
            messagebox.showerror('Error','No Record Found',parent=self.root)
      except Exception as msg:
        messagebox.showerror('ERROR',f'Error due to : {str(msg)}',parent=self.root)





if __name__=='__main__':
  root=Tk()
  obj=supplierclass(root)
  root.mainloop()