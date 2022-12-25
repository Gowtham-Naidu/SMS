from tkinter import*
from tkinter import messagebox
import sqlite3
import os
import email_pass
import smtplib
import time

class Login_System:
    def __init__(self,root):
        self.root=root
        self.root.title('Login System | Developed By Rock')
        self.root.geometry("1920x1080+0+0")
        self.root.config(bg="#e9e9e9")
        
        
        self.otp=''
        
        #images
        self.phone_image=PhotoImage(file="images/iPhone.png")
        self.lbl_phone_image=Label(self.root,image=self.phone_image,bg="#e9e9e9",bd=0).place(x=200,y=50)
        
        
        #####login_frame#########
        #variables
        self.employee_id=StringVar()
        self.password=StringVar()
        
        
        login_frame=Frame(self.root,bd=5,relief=RIDGE,bg="white")
        login_frame.place(x=850,y=110,width=450,height=560)
        
        title=Label(login_frame,text="SMS",font=("Imprint MT Shadow",45,"bold"),bg="white").place(x=0,y=30,relwidth=1)
   
        lbl_user=Label(login_frame,text="Employee ID",font=("MS Serif",25),bg="white",fg="#152190").place(x=50,y=100)
        
       
        txt_employee_id=Entry(login_frame,textvariable=self.employee_id,font=("times new roman",15),bg="#ECECEC").place(x=50,y=140,width=350)

        lbl_pass=Label(login_frame,text="Password",font=("MS Serif",25),bg="white",fg="#152190").place(x=50,y=200)
        txt_pass=Entry(login_frame,textvariable=self.password,show="*",font=("times new roman",15),bg="#ECECEC").place(x=50,y=240,width=350)

        #button
        self.logotlogo = PhotoImage(file='images/login1.png')
        Button_logout=Button(login_frame,command=self.login,text="Logout",image=self.logotlogo,border=0,cursor="hand2",bg='white',activebackground='white').place(x=50,y=300,width=350,height=55)

        hr=Label(login_frame,bg="lightgray").place(x=50,y=380,width=350,height=2)
        or_=Label(login_frame,text="OR",fg="lightgray",font=("times new roman",15,"bold"),bg="white").place(x=200,y=365)
        
        self.forget_logo = PhotoImage(file='images/forget.png')
        Button_forget=Button(login_frame,command=self.forget_window,image=self.forget_logo,border=0,cursor="hand2",bg='white',activebackground='white').place(x=50,y=400,width=350,height=55)

        #frame2
        register_frame=Frame(self.root,bd=5,relief=RIDGE,bg="white")
        register_frame.place(x=850,y=680,width=450,height=60)
        
        lbl_reg=Label(register_frame,text="Management is doing things right!!!",font=("times new roman",13),bg="white").place(x=0,y=15,relwidth=1)
        
        #self.send_email("xyz")
###########################functions##########################################################

    def login(self):
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
            if self.employee_id.get()=="" or self.password.get()=='':
                messagebox.showerror('Error','All Fields Are Required',parent=self.root)
            else:
                cur.execute('select utype from employee where eid=? and password=?',(self.employee_id.get(),self.password.get()))
                user=cur.fetchone()
                if user==None:
                     messagebox.showerror('Error','Invalid USERNAME/PASSWORD',parent=self.root)
                else:
                    #print(user)
                    if user[0]=="Admin":
                        self.root.destroy()
                        os.system("python dashboard.py")
                    else:
                        self.root.destroy()
                        os.system("python billing.py")                    
        except Exception as msg:
            messagebox.showerror('ERROR',f'Error due to : {str(msg)}',parent=self.root)

    #forget password
    def forget_window(self):
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
            if self.employee_id.get()=='':
                messagebox.showerror('ERROR','Employee Id Must Be Required',parent=self.root)
            else:
                cur.execute('select email from employee where eid=?',(self.employee_id.get(),))
                email=cur.fetchone()
                if email==None:
                     messagebox.showerror('Error','Invalid Employee ID,Try Again',parent=self.root)
                else:
                    #forget window
                    #variables
                    self.var_otp=StringVar()
                    self.var_new_pass=StringVar()
                    self.var_conf_pass=StringVar()
                    #call send email fun
                    #print(email)
                    chk=self.send_email(email[0]) #('gmail.com',)
                    if chk=='f':
                        messagebox.showerror('Error','Connection Error,Try Again',parent=self.root)
                    else:                      
                        self.forget_win=Toplevel(self.root)
                        self.forget_win.title('RESET PASSWORD')
                        self.forget_win.geometry("400x350+500+100")
                        self.forget_win.focus_force()
                        
                        title=Label(self.forget_win,text="Reset Password",font=("goudy old style",15,"bold"),bg="#3f51b5",fg="white").pack(side=TOP,fill=X)
                        lbl_reset=Label(self.forget_win,text="Enter OTP sent On Registered Email",font=("times new roman",15)).place(x=20,y=60)
                        
                        txt_reset=Entry(self.forget_win,textvariable=self.var_otp,font=("times new roman",15),bg="yellow").place(x=20,y=100,width=250,height=30)
            
            
                        lbl_new_pass=Label(self.forget_win,text="New Password",font=("times new roman",15)).place(x=20,y=160)
                        
                        txt_new_pass=Entry(self.forget_win,textvariable=self.var_new_pass,font=("times new roman",15),bg="yellow").place(x=20,y=190,width=250,height=30)
            
                        
                        lbl_conf_pass=Label(self.forget_win,text="Confirm Password",font=("times new roman",15)).place(x=20,y=225)
                        
                        txt_conf_pass=Entry(self.forget_win,textvariable=self.var_conf_pass,font=("times new roman",15),bg="yellow").place(x=20,y=255,width=250,height=30)
            
                        #button
                        self.button_reset=Button(self.forget_win,command=self.validate_otp,text="SUBMIT",font=("times new roman",15),bg='lightblue')
                        self.button_reset.place(x=280,y=100,width=100,height=30)
                        
                        self.button_update=Button(self.forget_win,text="Update",command=self.update_password,state=DISABLED,font=("times new roman",15),bg='lightblue')
                        self.button_update.place(x=150,y=300,width=100,height=30)
                        
                    
        except Exception as msg:
            messagebox.showerror('ERROR',f'Error due to : {str(msg)}',parent=self.root)

    
    def update_password(self):
        if self.var_new_pass.get()=='' or self.var_conf_pass.get()=='':
            messagebox.showerror('Error','Password Is Required',parent=self.forget_win)
        elif self.var_new_pass.get()!=self.var_conf_pass.get():
            messagebox.showerror('Error','Password & Confirm Password Should Be Same',parent=self.forget_win)
        else:
            con=sqlite3.connect(database=r'sms.db')
            cur=con.cursor()
            messagebox.showinfo('Success','Password Updated Sucessfully',parent=self.forget_win)
            self.forget_win.destroy()
            try:
                cur.execute("Update employee  set password=? where eid=?",(self.var_new_pass.get(),self.employee_id.get()))
                con.commit()
            except Exception as msg:
                messagebox.showerror('ERROR',f'Error due to : {str(msg)}',parent=self.root)

    
    #submit fun
    def validate_otp(self):
        if int(self.otp)==int(self.var_otp.get()):
            self.button_update.config(state=NORMAL)
            self.button_reset.config(state=DISABLED)
        else:
            messagebox.showerror('Error','Invalid OTP,Try Again',parent=self.forget_win)
     
        
    def send_email(self,to_):
        s=smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        email_=email_pass.email_
        pass_=email_pass.pass_
            
            
        s.login(email_,pass_)
            
        self.otp=int(time.strftime("%H%S%M"))+int(time.strftime("%S"))
        #print(self.otp)
        
        #sending email
        subj="SMS-Reset Password OTP"
        msg=f"Dear Sir/Madam! \n\nYour Rest OTP Is:{str(self.otp)}\n\nWith Regards,\nSMS Team"
        msg='Subject:{}\n\n{}'.format(subj,msg)
        s.sendmail(email_,to_,msg)
        chk=s.ehlo()
        
        if chk[0]==250:
            return 's'
        else:
            return 'f'
        
        
        
            
root=Tk()
obj=Login_System(root)
root.mainloop()