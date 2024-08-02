from tkinter import*
from PIL import Image,ImageTk    #pip install pillow
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox

class comtype:
    def __init__(self,root):
        self.root=root
        self.root.title("Water Management System")
        self.root.geometry("1330x680+194+150")

        #Title
        lbl_title=Label(self.root,text="Complaint Type",font=("times new roman",18,"bold"),bg="black",fg="light blue",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1330,height=50)


        #Logo
        img2=Image.open(r"C:\Users\Sanket sawant\Documents\Mini - Project\wms-images\water2.png")
        img2=img2.resize((100,50),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=100,height=50)

        #Label Frame
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Complaint Type Details",font=("times new roman",12,"bold"),padx=2,)
        labelframeleft.place(x=5,y=50,width=540,height=350)

        #comdetails
        lbl_comdetails=Label(labelframeleft,text="Complaint Details:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_comdetails.grid(row=0,column=0,sticky=W)

        self.var_comdetails=StringVar()
        entry_comdetails=ttk.Entry(labelframeleft, textvariable=self.var_comdetails, font=("arial",13,"bold"),width=20)
        entry_comdetails.grid(row=0,column=1,sticky=W)

        #comnumber
        lbl_comnumber=Label(labelframeleft,text="Complaint Number:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_comnumber.grid(row=1,column=0,sticky=W)

        self.var_comnumber=StringVar()
        entry_comnumber=ttk.Entry(labelframeleft, textvariable=self.var_comnumber, font=("arial",13,"bold"),width=20)
        entry_comnumber.grid(row=1,column=1,sticky=W)

        #aoe
        lbl_aoe=Label(labelframeleft,text="AOE:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_aoe.grid(row=2,column=0,sticky=W)

        self.var_aoe=StringVar()
        entry_aoe=ttk.Entry(labelframeleft, textvariable=self.var_aoe, font=("arial",13,"bold"),width=20)
        entry_aoe.grid(row=2,column=1,sticky=W)

        #buttons
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add", command=self.add_data, font=("arial",12,"bold"),bg="black",fg="light blue",width=9)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update", command=self.update, font=("arial",12,"bold"),bg="black",fg="light blue",width=9)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete", command=self.dat_Delete, font=("arial",12,"bold"),bg="black",fg="light blue",width=9)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset", command=self.data_reset, font=("arial",12,"bold"),bg="black",fg="light blue",width=9)
        btnReset.grid(row=0,column=3,padx=1)

        #table_frame_search_system
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Complaint Type",font=("times new roman",12,"bold"),padx=2,)
        Table_Frame.place(x=600,y=55,width=600,height=350)

        scroll_x=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_Frame,orient=VERTICAL)

        self.Complaint_Type_Details_Table=ttk.Treeview(Table_Frame,column=("comdetails","comnumber","aoe"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
 
        scroll_x.config(command=self.Complaint_Type_Details_Table.xview)
        scroll_y.config(command=self.Complaint_Type_Details_Table.yview)

        self.Complaint_Type_Details_Table.heading("comdetails",text="comdetails")
        self.Complaint_Type_Details_Table.heading("comnumber",text="comnumber")
        self.Complaint_Type_Details_Table.heading("aoe",text="aoe")

        self.Complaint_Type_Details_Table["show"]="headings"

        self.Complaint_Type_Details_Table.column("comdetails",width=100)
        self.Complaint_Type_Details_Table.column("comnumber",width=100)
        self.Complaint_Type_Details_Table.column("aoe",width=100)


        self.Complaint_Type_Details_Table.pack(fill=BOTH,expand=1)
        self.Complaint_Type_Details_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_comdetails.get()=="" or self.var_aoe.get()=="":
            messagebox.showerror("Error!","All fields are necessary!",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="767686",database="wms")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into comtype values(%s,%s,%s)",(self.var_comdetails.get(),self.var_comnumber.get(),self.var_aoe.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Complaint Type has been added!",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="767686",database="wms")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from comtype")
        rows = my_cursor.fetchall()
        if len(rows)!= 0:
            self.Complaint_Type_Details_Table.delete(*self.Complaint_Type_Details_Table.get_children())
            for i in rows:
                self.Complaint_Type_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row = self.Complaint_Type_Details_Table.focus()
        content = self.Complaint_Type_Details_Table.item(cursor_row)
        row = content["values"]

        self.var_comdetails.set(row[0])
        self.var_comnumber.set(row[1])
        self.var_aoe.set(row[2])

    def update(self):
        if self.var_comdetails.get()=="":
            messagebox.showerror("Error","Please enter valid complaint type details.",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost",username="root",password="767686", database="wms")
            my_cursor = conn.cursor()
            my_cursor.execute("update comtype set comdetails=%s, aoe=%s where comnumber=%s",(self.var_comdetails.get(),self.var_aoe.get(),self.var_comnumber.get()))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Complaint Type details has been updated sucessfully!", parent=self.root)

    def dat_Delete(self):
        dat_Delete = messagebox.askyesno("Water Management System,","Do you want to delete this complaint type?",parent=self.root)
        if dat_Delete>0:
            conn = mysql.connector.connect(host="localhost",username="root",password="767686",database="wms")
            my_cursor = conn.cursor()
            query = "delete from comtype where comnumber=%s"
            value = (self.var_comnumber.get(),)
            my_cursor.execute(query,value)
        else:
            if not dat_Delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
 
    def data_reset(self):
        self.var_comdetails.set("")
        self.var_comnumber.set("")
        self.var_aoe.set("")


if __name__ == "__main__":
    root=Tk()
    obj=comtype(root)
    root.mainloop()