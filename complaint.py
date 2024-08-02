from tkinter import*
from PIL import Image,ImageTk    #pip install pillow
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox

class complaint:
    def __init__(self,root):
        self.root=root
        self.root.title("Water Management System")
        self.root.geometry("1330x680+194+150")

        #variables
        self.var_user_contact=StringVar()
        self.var_date_of_complaint=StringVar()
        self.var_date_of_complaint_resolved=StringVar()
        self.var_aoe=StringVar()
        self.var_comnumber=StringVar()
        self.var_info=StringVar()

        #Title
        lbl_title=Label(self.root,text="Complaint",font=("times new roman",18,"bold"),bg="black",fg="light blue",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1330,height=50)


        #Logo
        img2=Image.open(r"C:\Users\Sanket sawant\Documents\Mini - Project\wms-images\water2.png")
        img2=img2.resize((100,50),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=100,height=50)

        #Label Frame
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Complaint Details",font=("times new roman",12,"bold"),padx=2,)
        labelframeleft.place(x=5,y=50,width=425,height=490)

        #Labels and Entries

        #mobile number
        lbl_user_contact=Label(labelframeleft,text="Mobile Number:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_user_contact.grid(row=0,column=0,sticky=W)

        entry_contact=ttk.Entry(labelframeleft,textvariable=self.var_user_contact, font=("arial",13,"bold"),width=20)
        entry_contact.grid(row=0,column=1,sticky=W)

        #fetch data button
        btnfetchdata=Button(labelframeleft,command=self.Fetch_Contact, text="Fetch Data", font=("arial",8,"bold"),bg="black",fg="light blue",width=8)
        btnfetchdata.place(x=347, y=4)

        #date of complaint
        date_of_complaint=Label(labelframeleft,text="Date of complaint:",font=("arial",12,"bold"),padx=2,pady=6)
        date_of_complaint.grid(row=1,column=0,sticky=W)
        
        txtdate_of_complaint=ttk.Entry(labelframeleft,textvariable=self.var_date_of_complaint, font=("arial",13,"bold"),width=29)
        txtdate_of_complaint.grid(row=1,column=1)

        #date of complaint resolved
        lbl_date_of_complaint_resolved=Label(labelframeleft,text="Resolved:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_date_of_complaint_resolved.grid(row=2,column=0,sticky=W)
        
        txt_date_of_complaint_resolved=ttk.Entry(labelframeleft,textvariable=self.var_date_of_complaint_resolved, font=("arial",13,"bold"),width=29)
        txt_date_of_complaint_resolved.grid(row=2,column=1)

        #aoe (scale)
        lbl_aoe=Label(labelframeleft,text="Area of effect:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_aoe.grid(row=3,column=0,sticky=W)

        conn = mysql.connector.connect(host="localhost",username="root",password="767686",database="wms")
        my_cursor = conn.cursor()
        my_cursor.execute("select aoe from comtype")
        rows = my_cursor.fetchall()
        
        combo_aoe=ttk.Combobox(labelframeleft,textvariable=self.var_aoe, font=("arial",12,"bold"),width=27,state="readonly")
        combo_aoe["value"]=rows
        combo_aoe.current(0)
        combo_aoe.grid(row=3,column=1)

        #complaint number
        lblcomnumber=Label(labelframeleft,text="Complaint No.:", font=("arial",12,"bold"),padx=2,pady=6)
        lblcomnumber.grid(row=4,column=0,sticky=W)
        
        #txtlblcomnumber=ttk.Entry(labelframeleft,textvariable=self.var_comnumber, font=("arial",13,"bold"),width=29)
        #txtlblcomnumber.grid(row=4,column=1)

        conn = mysql.connector.connect(host="localhost",username="root",password="767686",database="wms")
        my_cursor = conn.cursor()
        my_cursor.execute("select comnumber from comtype")
        rows = my_cursor.fetchall()

        combo_comnum=ttk.Combobox(labelframeleft,textvariable=self.var_comnumber, font=("arial",12,"bold"),width=27,state="readonly")
        combo_comnum["value"]=rows
        combo_comnum.current(0)
        combo_comnum.grid(row=4,column=1)

        #additional information
        lblinfo=Label(labelframeleft,text="Information:", font=("arial",12,"bold"),padx=2,pady=6)
        lblinfo.grid(row=5,column=0,sticky=W)
        
        txtinfo=ttk.Entry(labelframeleft,textvariable=self.var_info, font=("arial",13,"bold"),width=29)
        txtinfo.grid(row=5,column=1)

        #buttons
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data, font=("arial",12,"bold"),bg="black",fg="light blue",width=9)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.update, font=("arial",12,"bold"),bg="black",fg="light blue",width=9)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.dat_Delete, font=("arial",12,"bold"),bg="black",fg="light blue",width=9)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.data_reset, font=("arial",12,"bold"),bg="black",fg="light blue",width=9)
        btnReset.grid(row=0,column=3,padx=1)

        #table_frame_search_system
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search Database",font=("times new roman",12,"bold"),padx=2,)
        Table_Frame.place(x=435,y=280,width=890,height=260)

        lblSearchBy=Label(Table_Frame,font=("arial",12,"bold"),text="Search By:",bg="black",fg="light blue") 
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()
        combo_search=ttk.Combobox(Table_Frame,textvariable=self.search_var, font=("arial",12,"bold"),width=24,state="readonly")
        combo_search["value"]=("user_contact","comnumber")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Table_Frame,textvariable=self.txt_search, font=("arial",13,"bold"),width=24) 
        txtSearch.grid(row=0,column=2,padx=2)

        btnSearch=Button(Table_Frame,text="Search",command=self.search_data, font=("arial",12,"bold"),bg="black",fg="light blue",width=9)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShow=Button(Table_Frame,text="Show All",command=self.fetch_data, font=("arial",12,"bold"),bg="black",fg="light blue",width=9)
        btnShow.grid(row=0,column=4,padx=1)

        #Show data table
        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=180)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Complaint_Details_Table=ttk.Treeview(details_table,column=("user_contact","date_of_complaint","date_of_complaint_resolved","aoe","comnumber","info"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
 
        scroll_x.config(command=self.Complaint_Details_Table.xview)
        scroll_y.config(command=self.Complaint_Details_Table.yview)

        self.Complaint_Details_Table.heading("user_contact",text="user_contact")
        self.Complaint_Details_Table.heading("date_of_complaint",text="date_of_complaint")
        self.Complaint_Details_Table.heading("date_of_complaint_resolved",text="date_of_complaint_resolved")
        self.Complaint_Details_Table.heading("aoe",text="aoe")
        self.Complaint_Details_Table.heading("comnumber",text="comnumber")
        self.Complaint_Details_Table.heading("info",text="info")

        self.Complaint_Details_Table["show"]="headings"

        self.Complaint_Details_Table.column("user_contact",width=100)
        self.Complaint_Details_Table.column("date_of_complaint",width=100)
        self.Complaint_Details_Table.column("date_of_complaint_resolved",width=100)
        self.Complaint_Details_Table.column("aoe",width=100)
        self.Complaint_Details_Table.column("comnumber",width=100)
        self.Complaint_Details_Table.column("info",width=100)

        self.Complaint_Details_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.Complaint_Details_Table.pack(fill=BOTH,expand=1)
        self.fetch_data()
    
    def add_data(self):
        if self.var_user_contact.get()=="" or self.var_date_of_complaint.get()=="":
            messagebox.showerror("Error!","All fields are necessary!",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="767686",database="wms")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into complaint values(%s,%s,%s,%s,%s,%s)",(self.var_user_contact.get(),self.var_date_of_complaint.get(),self.var_date_of_complaint_resolved.get(),self.var_aoe.get(),self.var_comnumber.get(),self.var_info.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Complaint has been added!",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="767686",database="wms")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from complaint")
        rows = my_cursor.fetchall()
        if len(rows)!= 0:
            self.Complaint_Details_Table.delete(*self.Complaint_Details_Table.get_children())
            for i in rows:
                self.Complaint_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row = self.Complaint_Details_Table.focus()
        content = self.Complaint_Details_Table.item(cursor_row)
        row = content["values"]

        self.var_user_contact.set(row[0])
        self.var_date_of_complaint.set(row[1])
        self.var_date_of_complaint_resolved.set(row[2])
        self.var_aoe.set(row[3])
        self.var_comnumber.set(row[4])
        self.var_info.set(row[5])

    def update(self):
        if self.var_user_contact.get()=="":
            messagebox.showerror("Error","Please enter valid mobile number.",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost",username="root",password="767686", database="wms")
            my_cursor = conn.cursor()
            my_cursor.execute("update complaint set date_of_complaint=%s, date_of_complaint_resolved=%s, aoe=%s, comnumber=%s, info=%s where user_contact=%s",(self.var_date_of_complaint.get(),self.var_date_of_complaint_resolved.get(),self.var_aoe.get(),self.var_comnumber.get(),self.var_info.get(),self.var_user_contact.get()))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Complaint details has been updated sucessfully!", parent=self.root)

    def dat_Delete(self):
        dat_Delete = messagebox.askyesno("Water Management System,","Do you want to delete this complaint?",parent=self.root)
        if dat_Delete>0:
            conn = mysql.connector.connect(host="localhost",username="root",password="767686",database="wms")
            my_cursor = conn.cursor()
            query = "delete from complaint where user_contact=%s"
            value = (self.var_user_contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not dat_Delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
 
    def data_reset(self):
        self.var_user_contact.set("")
        self.var_date_of_complaint.set("")
        self.var_date_of_complaint_resolved.set("")
        self.var_aoe.set("")
        self.var_comnumber.set("")
        self.var_info.set("")

    def Fetch_Contact(self):
        if self.var_user_contact.get()=="":
            messagebox.showerror("Error!","Please enter a valid contact number!",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="767686",database="wms")
            my_cursor=conn.cursor()
            query=("select first_name from users where mobilenumber=%s")
            value=(self.var_user_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error!","We couldn't find an entry with that mobile number.",parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataframe.place(x=435,y=55,width=890,height=220)

                lblName=Label(showDataframe,text="First Name:",font=("arial",12,"bold"))
                lblName.place(x=0,y=0)

                lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=0)

                #1
                conn=mysql.connector.connect(host="localhost",username="root",password="767686",database="wms")
                my_cursor=conn.cursor()
                query=("select user_ref from users where mobilenumber=%s")
                value=(self.var_user_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblGender=Label(showDataframe,text="user_ref:",font=("arial",12,"bold"))
                lblGender.place(x=0,y=30)

                lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=30)

                #2
                conn=mysql.connector.connect(host="localhost",username="root",password="767686",database="wms")
                my_cursor=conn.cursor()
                query=("select gender from users where mobilenumber=%s")
                value=(self.var_user_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblGender=Label(showDataframe,text="Gender:",font=("arial",12,"bold"))
                lblGender.place(x=0,y=60)

                lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=60)

                #3
                conn=mysql.connector.connect(host="localhost",username="root",password="767686",database="wms")
                my_cursor=conn.cursor()
                query=("select email from users where mobilenumber=%s")
                value=(self.var_user_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblGender=Label(showDataframe,text="Email:",font=("arial",12,"bold"))
                lblGender.place(x=0,y=90)

                lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=90)

                #4
                conn=mysql.connector.connect(host="localhost",username="root",password="767686",database="wms")
                my_cursor=conn.cursor()
                query=("select address from users where mobilenumber=%s")
                value=(self.var_user_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblGender=Label(showDataframe,text="Address:",font=("arial",12,"bold"))
                lblGender.place(x=0,y=120)

                lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=120)
    
    #search_system
    def search_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="767686",database="wms")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM complaint WHERE " + str(self.search_var.get()) + " LIKE '%" + str(self.txt_search.get()) + "%'")
        rows_fetch = my_cursor.fetchall()
        if len(rows_fetch)!=0:
            self.Complaint_Details_Table.delete(*self.Complaint_Details_Table.get_children())
            for i in rows_fetch:
                self.Complaint_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()





if __name__ == "__main__":
    root=Tk()
    obj=complaint(root)
    root.mainloop()