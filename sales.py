from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
import os
class salesclass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("STORE MANAGEMENT SYSTEM | Develpoed by Gowtham")
        self.root.config(bg='white')
        self.root.focus_force()
        ###############variables
        self.var_invoice=StringVar()
        self.bill_list=[]

        #title
        lbl_title=Label(self.root,text='View Customer Bills',font=('goudy old style',30),bg='#184a45',fg='white',bd=5,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=5)

        #lbl_invoice
        lbl_invoice=Label(self.root,text='Invoice No.',font=('times new roman',15),bg='white').place(x=50,y=100)

        txt_invoice=Entry(self.root,textvariable=self.var_invoice,font=('times new roman',15),bg='yellow').place(x=160,y=100,width=180,height=28)

        #button
        Button_search = Button(self.root,text='Search',command=self.search,font=("goudy old style",15,"bold"),cursor='hand2',bg='#2196f3',fg='white').place(x=360,y=100,width=120,height=28)

        Button_clear = Button(self.root,text='Clear',command=self.clear,font=("goudy old style",15,"bold"),cursor='hand2',bg='lightgray').place(x=490,y=100,width=120,height=28)

        #sales_frame
        sales_frame=Frame(self.root,bd=3,relief=RIDGE)
        sales_frame.place(x=50,y=140,width=200,height=330)

        #list_view
        scrolly=Scrollbar(sales_frame,orient=VERTICAL)
        self.sales_list=Listbox(sales_frame,font=('goudy old style',15),bg="white",yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.sales_list.yview)
        self.sales_list.pack(fill=BOTH,expand=1)


        #bill frame
        bill_frame=Frame(self.root,bd=3,relief=RIDGE)
        bill_frame.place(x=280,y=140,width=410,height=330)
        #bill_area_title
        lbl_title=Label(bill_frame,text='Customer Bill Area',font=('goudy old style',20),bg='orange').pack(side=TOP,fill=X)
        #bill_list_view
        scrolly2=Scrollbar(bill_frame,orient=VERTICAL)
        self.bill_area=Text(bill_frame,bg="yellow",yscrollcommand=scrolly2.set,cursor='hand2')
        scrolly2.pack(side=RIGHT,fill=Y)
        scrolly2.config(command=self.bill_area.yview)
        self.bill_area.pack(fill=BOTH,expand=1)
        self.sales_list.bind('<ButtonRelease-1>',self.get_data)

        #image_for_bill_area
        self.bill_img=Image.open('images/sales.jpg')
        self.bill_img=self.bill_img.resize((400,400))
        self.bill_img=ImageTk.PhotoImage(self.bill_img)
        
        self.lbl_im1=Label(self.root,image=self.bill_img,bd=0)
        self.lbl_im1.place(x=700,y=100)
        self.show()

##########################################################################
    
    #bill_reading
    def show(self):
        del self.bill_list[:]
        self.sales_list.delete(0,END)
        #print(os.listdir('bill'))
        for i in os.listdir('bill'):
            #print(i.split('.'),i.split('.')[-1])
            if i.split('.')[-1]=='txt':
                self.sales_list.insert(END,i)
                self.bill_list.append(i.split('.')[0])

    def get_data(self,ev):
        index_=self.sales_list.curselection()
        file_name=self.sales_list.get(index_)
        #print(file_name)
        self.bill_area.delete('1.0',END)
        fp=open(f'bill/{file_name}','r')
        for i in fp:
            self.bill_area.insert(END,i)
        fp.close()
    
    #search
    def search(self):
        if self.var_invoice.get()=="":
            messagebox.showerror('Error','Invoice NO. Should Be Required',parent=self.root)
        else:
            if self.var_invoice.get() in self.bill_list:
                fp=open(f'bill/{self.var_invoice.get()}.txt','r')
                self.bill_area.delete('1.0',END)
                for i in fp:
                    self.bill_area.insert(END,i)
                fp.close()
            else:
                messagebox.showerror('Error','Invalid Invoice No.',parent=self.root)


    #clear
    def clear(self):
        self.show()
        self.bill_area.delete('1.0',END)





if __name__=='__main__':
  root=Tk()
  obj=salesclass(root)
  root.mainloop()