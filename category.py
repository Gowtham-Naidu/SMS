from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class categoryclass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("STORE MANAGEMENT SYSTEM | Develpoed by Gowtham")
        self.root.config(bg='white')
        self.root.focus_force()

        #variables
        self.var_cat_id=StringVar()
        self.var_name=StringVar()


        #title
        lbl_title=Label(self.root,text='Manage Product Category',font=('goudy old style',30),bg='#184a45',fg='white',bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=5)

        #name
        lbl_name=Label(self.root,text='Enter Category Name',font=('goudy old style',30),bg='white').place(x=50,y=100)

        #name_entry
        txt_name=Entry(self.root,textvariable=self.var_name,font=('goudy old style',18),bg='yellow').place(x=50,y=170,width=300)

        #add_button
        button_add=Button(self.root,text='ADD',command=self.add,font=('goudy old style',15),bg='#4caf50',fg='white',cursor='hand2').place(x=360,y=170,width=150,height=30)

        #delet_button
        button_delet=Button(self.root,text='DELETE',command=self.delete,font=('goudy old style',15),bg='red',fg='white',cursor='hand2').place(x=520,y=170,width=150,height=30)
        
        #category Details_showtable_creation

        cat_frame=Frame(self.root,bd=3,relief=RIDGE)
        cat_frame.place(x=700,y=100,width=380,height=100)


        #scroll=y
        scrolly=Scrollbar(cat_frame,orient=VERTICAL)
        #scroll=x
        scrollx=Scrollbar(cat_frame,orient=HORIZONTAL)



        #treeview=table
        self.category_table=ttk.Treeview(cat_frame,columns=('cid','name'),yscrollcommand=scrolly,xscrollcommand=scrollx)
        self.category_table.config(cursor='hand2')
        #scrollbar packing
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.category_table.xview,cursor='hand2')
        scrolly.config(command=self.category_table.yview,cursor='hand2')

        self.category_table.heading('cid',text='CID')    
        self.category_table.heading('name',text='NAME')
        
        
        
        
        self.category_table['show']='headings'

        self.category_table.column('cid',width=90)    
        self.category_table.column('name',width=100)
        
       
        

        self.category_table.pack(fill=BOTH,expand=1)
        self.category_table.bind('<ButtonRelease-1>',self.get_data)

        #images
        self.im1=Image.open('images/category.jpg')
        self.im1=self.im1.resize((1000,250))
        self.im1=ImageTk.PhotoImage(self.im1)
        
        self.lbl_im1=Label(self.root,image=self.im1,bd=10,relief=RIDGE,bg='black')
        self.lbl_im1.place(x=50,y=220)
        self.show()
        ####################################################################################

    # add function
    def add(self):
      con=sqlite3.connect(database=r'sms.db')
      cur=con.cursor()
      try:
        if self.var_name.get()=='':
          messagebox.showerror('Error','Category Must be required',parent=self.root)
        else:
          cur.execute('select * from category where name=?',(self.var_name.get(),))
          rows=cur.fetchone()
          if rows!=None:
            messagebox.showerror('Error','Category already present,try diffrent',parent=self.root)

          else:
            cur.execute('insert into category (name) values(?)',(
                      self.var_name.get(),
            ))
            con.commit()
            messagebox.showinfo('Success','Category Addedd Successfully',parent=self.root)
            self.show()
      except Exception as msg:
        messagebox.showerror('ERROR',f'Error due to : {str(msg)}',parent=self.root)


    #data_show
    def show(self):
      con=sqlite3.connect(database=r'sms.db')
      cur=con.cursor()
      try:
        cur.execute('select * from category')
        rows=cur.fetchall()
        self.category_table.delete(*self.category_table.get_children())
        for row in rows:
          self.category_table.insert('',END,values=row)
      except Exception as msg:
        messagebox.showerror('ERROR',f'Error due to : {str(msg)}',parent=self.root)

     #to get data
    def get_data(self,ev):
        f=self.category_table.focus()
        content=(self.category_table.item(f))
        row=content['values']
        #print(row)
        self.var_cat_id.set(row[0])
        self.var_name.set(row[1])


    #delete
    def delete(self):
      con=sqlite3.connect(database=r'sms.db')
      cur=con.cursor()
      try:
        if self.var_name.get()=='':
          messagebox.showerror('Error','Category Name Must be required',parent=self.root)
        else:
          cur.execute('select * from category where name=?',(self.var_name.get(),))
          row=cur.fetchone()
          if row==None:
            messagebox.showerror('Error','Invalid Category Name',parent=self.root)

          else:
            op=messagebox.askyesno('Confirm','Do you really want to delete?',parent=self.root)
            if op==True:
              cur.execute('delete from category where name=?',(self.var_name.get(),))
              con.commit()
              messagebox.showinfo('Delete','Category Deleted Successfully',parent=self.root)
              self.show()
              self.var_cat_id.set(' ')
              
      except Exception as msg:
        messagebox.showerror('ERROR',f'Error due to : {str(msg)}',parent=self.root)
if __name__=='__main__':
  root=Tk()
  obj=categoryclass(root)
  root.mainloop()