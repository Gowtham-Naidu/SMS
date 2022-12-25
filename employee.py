from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class employeeclass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("STORE MANAGEMENT SYSTEM | Develpoed by Gowtham")
        self.root.config(bg='white')

        self.root.focus_force()

        #all variables
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()

        self.var_emp_id=StringVar()
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_password=StringVar()
        self.var_utype=StringVar()
        self.var_contact=StringVar()
        self.var_salaray=StringVar()
        #searchframe

        searchframe=LabelFrame(self.root,text="Search Employee",bg='white',font=('gody old style',12,'bold'),bd=2,relief=RIDGE)
        searchframe.place(x=250,y=20,width=600,height=70)

        #search_employee_combobox
        cmb_search=ttk.Combobox(searchframe,textvariable=self.var_searchby,cursor='hand2',values=('select','Email','Name','EID','Contact'),state='readonly',justify=CENTER,font=('gody old style',15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        #text_searchbox
        txt_search = Entry(searchframe,textvariable=self.var_searchtxt,font=("goudy old style",15),bg='yellow',fg='black').place(x=200,y=10)

        #search_button
        Button_search = Button(searchframe,command=self.search,text='Search',font=("goudy old style",15),cursor='hand2',bg='#4caf50',fg='white').place(x=410,y=9,width=150,height=30)


        #employee_title
        title=Label(self.root,text='Employee Details',font=('goudy old style',15),bg='#0f4d7d',fg='white').place(x=50,y=100,width=1000)

        #row1
        #lbl_eid
        Label_eid=Label(self.root,text='EID',font=('goudy old style',15),bg='white').place(x=50,y=150)

        #lbl_gender
        Label_gender=Label(self.root,text='Gender',font=('goudy old style',15),bg='white').place(x=350,y=150)

        #lbl_contact
        Label_contact=Label(self.root,text='Contact',font=('goudy old style',15),bg='white').place(x=750,y=150)


        #txt _eid
        txt_eid=Entry(self.root,textvariable=self.var_emp_id,font=('goudy old style',15),bg='yellow').place(x=150,y=150,width=180)

        #cmb_txt_gender_combobox
        cmb_gender=ttk.Combobox(self.root,textvariable=self.var_gender,cursor='hand2',values=('Male','Female','Other'),state='readonly',justify=CENTER,font=('gody old style',15))
        cmb_gender.place(x=500,y=150,width=180)
        cmb_gender.current(0)

        #txt_covtact
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=('goudy old style',15),bg='yellow').place(x=850,y=150,width=180)


        #row2
        #lbl_name
        Label_name=Label(self.root,text='Name',font=('goudy old style',15),bg='white').place(x=50,y=190)

        #lbl_dob
        Label_dob=Label(self.root,text='D.O.B',font=('goudy old style',15),bg='white').place(x=350,y=190)

        #lbl_doj
        Label_eid=Label(self.root,text='D.O.J',font=('goudy old style',15),bg='white').place(x=750,y=190)

        #txt_name
        txt_name=Entry(self.root,textvariable=self.var_name,font=('goudy old style',15),bg='yellow').place(x=150,y=190,width=180)

        #txt_dob
        txt_dob=Entry(self.root,textvariable=self.var_dob,font=('goudy old style',15),bg='yellow').place(x=500,y=190,width=180)

        #txt_doj
        txt_doj=Entry(self.root,textvariable=self.var_doj,font=('goudy old style',15),bg='yellow').place(x=850,y=190,width=180)


        #row3
        #lbl_email
        Label_email=Label(self.root,text='Email',font=('goudy old style',15),bg='white').place(x=50,y=230)

        #lbl_password
        Label_password=Label(self.root,text='Password',font=('goudy old style',15),bg='white').place(x=350,y=230)

        #lbl_utype
        Label_utype=Label(self.root,text='User Type',font=('goudy old style',15),bg='white').place(x=750,y=230)


        #txt_email
        txt_email=Entry(self.root,textvariable=self.var_email,font=('goudy old style',15),bg='yellow').place(x=150,y=230,width=180)

        #txt_password
        txt_password=Entry(self.root,textvariable=self.var_password,font=('goudy old style',15),bg='yellow').place(x=500,y=230,width=180)

        #txt_utype_combobox
        cmb_utype=ttk.Combobox(self.root,textvariable=self.var_utype,cursor='hand2',values=('Admin','Employee'),state='readonly',justify=CENTER,font=('gody old style',15))
        cmb_utype.place(x=850,y=230,width=180)
        cmb_utype.current(0)


        #row4
        #lbl_address
        Label_address=Label(self.root,text='Address',font=('goudy old style',15),bg='white').place(x=50,y=270)

        #lbl_salary
        Label_salary=Label(self.root,text='Salary',font=('goudy old style',15),bg='white').place(x=500,y=270)

        #txt_address
        self.txt_address=Text(self.root,font=('goudy old style',15),bg='yellow').place(x=150,y=270,width=300,height=60)

        #txt_salary
        txt_salary=Entry(self.root,textvariable=self.var_salaray,font=('goudy old style',15),bg='yellow').place(x=600,y=270,width=180)


        #button add
        Button_add = Button(self.root,command=self.add,text='Save',font=("goudy old style",15),cursor='hand2',bg='#2196f3',fg='white').place(x=500,y=305,width=110,height=28)

        #button update
        Button_update = Button(self.root,command=self.update,text='Update',font=("goudy old style",15),cursor='hand2',bg='#4caf50',fg='white').place(x=620,y=305,width=110,height=28)

        #button delete
        Button_delete= Button(self.root,command=self.delete,text='Delete',font=("goudy old style",15),cursor='hand2',bg='#f44336',fg='white').place(x=740,y=305,width=110,height=28)

        #button clear
        Button_clear = Button(self.root,command=self.clear,text='Clear',font=("goudy old style",15),cursor='hand2',bg='#607d8b',fg='white').place(x=860,y=305,width=110,height=28)


        #employee Details_showtable_creation

        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=350,relwidth=1,height=150)


        #scroll=y
        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        #scroll=x
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)



        #treeview=table
        self.EmployeeTable=ttk.Treeview(emp_frame,columns=('eid','name','email','gender','contact','dob','doj','password','utype','salary','address'),yscrollcommand=scrolly,xscrollcommand=scrollx)
        self.EmployeeTable.config(cursor='hand2')
        #scrollbar packing
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.EmployeeTable.xview,cursor='hand2')
        scrolly.config(command=self.EmployeeTable.yview,cursor='hand2')

        self.EmployeeTable.heading('eid',text='EID')    
        self.EmployeeTable.heading('name',text='Name')
        self.EmployeeTable.heading('email',text='EMAIL')
        self.EmployeeTable.heading('gender',text='GENDER')
        self.EmployeeTable.heading('contact',text='CONTACT')
        self.EmployeeTable.heading('dob',text='D.O.B')
        self.EmployeeTable.heading('doj',text='D.O.J')
        self.EmployeeTable.heading('password',text='PASSWORD')
        self.EmployeeTable.heading('utype',text='USER TYPE')
        self.EmployeeTable.heading('salary',text='SALARY')
        self.EmployeeTable.heading('address',text='ADDRESS')
        
        self.EmployeeTable['show']='headings'

        self.EmployeeTable.column('eid',width=90)    
        self.EmployeeTable.column('name',width=100)
        self.EmployeeTable.column('email',width=100)
        self.EmployeeTable.column('gender',width=100)
        self.EmployeeTable.column('contact',width=100)
        self.EmployeeTable.column('dob',width=100)
        self.EmployeeTable.column('doj',width=100)
        self.EmployeeTable.column('password',width=100)
        self.EmployeeTable.column('utype',width=100)
        self.EmployeeTable.column('salary',width=100)
        self.EmployeeTable.column('address',width=100)

        self.EmployeeTable.pack(fill=BOTH,expand=1)
        self.EmployeeTable.bind('<ButtonRelease-1>',self.get_data)

        self.show()

#===================================================================================

    # add function
    def add(self):
      con=sqlite3.connect(database=r'sms.db')
      cur=con.cursor()
      try:
        if self.var_emp_id.get()=='':
          messagebox.showerror('Error','Employee ID Must be required',parent=self.root)
        elif self.var_name.get()=='':
          messagebox.showerror('Error','Employee Name Must be Given',parent=self.root)
        else:
          cur.execute('select * from employee where eid=?',(self.var_emp_id.get(),))
          row=cur.fetchone()
          if row!=None:
            messagebox.showerror('Error','This Employee ID already assigned,try diffrent',parent=self.root)

          else:
            cur.execute('insert into employee (eid,name,email,gender,contact,dob,doj,password,utype,salary) values(?,?,?,?,?,?,?,?,?,?)',(
                      self.var_emp_id.get(),
                      self.var_name.get(),
                      self.var_email.get(),
                      self.var_gender.get(),
                      self.var_contact.get(),
                      self.var_dob.get(),
                      self.var_doj.get(),
                      self.var_password.get(),
                      self.var_utype.get(),
                      self.var_salaray.get(),

            ))
            con.commit()
            messagebox.showinfo('Success','Employee Addedd Successfully',parent=self.root)
            self.show()
      except Exception as msg:
        messagebox.showerror('ERROR',f'Error due to : {str(msg)}',parent=self.root)
      
    #data_show
    def show(self):
      con=sqlite3.connect(database=r'sms.db')
      cur=con.cursor()
      try:
        cur.execute('select * from employee')
        rows=cur.fetchall()
        self.EmployeeTable.delete(*self.EmployeeTable.get_children())
        for row in rows:
          self.EmployeeTable.insert('',END,values=row)
      except Exception as msg:
        messagebox.showerror('ERROR',f'Error due to : {str(msg)}',parent=self.root)

    #to get data
    def get_data(self,ev):
        f=self.EmployeeTable.focus()
        content=(self.EmployeeTable.item(f))
        row=content['values']
    
        self.var_emp_id.set(row[0]),
        self.var_name.set(row[1]),
        self.var_email.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_contact.set(row[4]),
        self.var_dob.set(row[5]),
        self.var_doj.set(row[6]),
        self.var_password.set(row[7]),
        self.var_utype.set(row[8]),
        self.var_salaray.set(row[9]),

    #update
    def update(self):
      con=sqlite3.connect(database=r'sms.db')
      cur=con.cursor()
      try:
        if self.var_emp_id.get()=='':
          messagebox.showerror('Error','Employee ID Must be required',parent=self.root)
        else:
          cur.execute('select * from employee where eid=?',(self.var_emp_id.get(),))
          row=cur.fetchone()
          if row==None:
            messagebox.showerror('Error','Invalid Employee ID',parent=self.root)

          else:
            where_con=self.var_emp_id.get()
            cur.execute("update employee set name=?,email=?,gender=?,contact=?,dob=?,doj=?,password=?,utype=?,salary=? where eid=?",(
                      
                      
                      self.var_name.get(),
                      self.var_email.get(),
                      self.var_gender.get(),
                      self.var_contact.get(),
                      self.var_dob.get(),
                      self.var_doj.get(),
                      self.var_password.get(),
                      self.var_utype.get(),
                      self.var_salaray.get(),
                      self.var_emp_id.get(),
            ))
            con.commit()
            messagebox.showinfo('Success','Employee Updated Successfully',parent=self.root)
            self.show()
      except Exception as msg:
        messagebox.showerror('ERROR',f'Error due to : {str(msg)}',parent=self.root)


    #delete
    def delete(self):
      con=sqlite3.connect(database=r'sms.db')
      cur=con.cursor()
      try:
        if self.var_emp_id.get()=='':
          messagebox.showerror('Error','Employee ID Must be required',parent=self.root)
        else:
          cur.execute('select * from employee where eid=?',(self.var_emp_id.get(),))
          row=cur.fetchone()
          if row==None:
            messagebox.showerror('Error','Invalid Employee ID',parent=self.root)

          else:
            op=messagebox.askyesno('Confirm','Do you really want to delete?',parent=self.root)
            if op==True:
              cur.execute('delete from employee where eid=?',(self.var_emp_id.get(),))
              con.commit()
              messagebox.showinfo('Delete','Employee Deleted Successfully',parent=self.root)
              self.clear()
      except Exception as msg:
        messagebox.showerror('ERROR',f'Error due to : {str(msg)}',parent=self.root)
        

    #clear
    def clear(self):
        self.var_emp_id.set('')
        self.var_name.set('')
        self.var_email.set('')
        self.var_gender.set('Select')
        self.var_contact.set('')
        self.var_dob.set('')
        self.var_doj.set('')
        self.var_password.set('')
        self.var_utype.set('Admin')
        self.var_salaray.set('')
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
          cur.execute('select * from employee where '+self.var_searchby.get()+" like '%"+self.var_searchtxt.get()+"%'")
          rows=cur.fetchall()
          if len(rows)!=0:
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
              self.EmployeeTable.insert('',END,values=row)
          else:
            messagebox.showerror('Error','No Record Found',parent=self.root)
      except Exception as msg:
        messagebox.showerror('ERROR',f'Error due to : {str(msg)}',parent=self.root)





if __name__=='__main__':
  root=Tk()
  obj=employeeclass(root)
  root.mainloop()