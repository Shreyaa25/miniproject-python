from tkinter import*
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox




class userwin:
    def __init__(self,root):
        self.root=root
        self.root.title("Water Management System")
        self.root.geometry("1330x680+194+150")

        #variables
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_first_name=StringVar()
        self.var_last_name=StringVar()
        self.var_gender=StringVar()
        self.var_postcode=StringVar()
        self.var_mobilenumber=StringVar()
        self.var_email=StringVar()
        self.var_state=StringVar()
        self.var_idproof=StringVar()
        self.var_idnumber=StringVar()
        self.var_address=StringVar()


        #Title
        lbl_title=Label(self.root,text="ADD USER DETAILS",font=("times new roman",18,"bold"),bg="black",fg="light blue",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1330,height=50)


        #Logo
        img2=Image.open(r"C:\Users\Sanket sawant\Documents\Mini - Project\wms-images\water2.png")
        img2=img2.resize((100,50),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=100,height=50)

        #Label Frame
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="User Details",font=("times new roman",12,"bold"),padx=2,)
        labelframeleft.place(x=5,y=50,width=425,height=490)

        #Labels and Entries

        #user_ref
        lbl_user_ref=Label(labelframeleft,text="User Reference",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_user_ref.grid(row=0,column=0,sticky=W)

        entry_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref, font=("arial",13,"bold"),width=29,state="readonly")
        entry_ref.grid(row=0,column=1)

        #first_name 
        cname=Label(labelframeleft,font=("arial",12,"bold"),text="First Name:",padx=2,pady=6) 
        cname.grid(row=1,column=0,sticky=W) 
        txtcname=ttk.Entry(labelframeleft,textvariable=self.var_first_name, font=("arial",13,"bold"),width=29)
        txtcname.grid(row=1,column=1) 
        
        #last_name 
        lbllname=Label(labelframeleft,font=("arial",12,"bold"),text="Last Name:",padx=2,pady=6)
        lbllname.grid(row=2,column=0,sticky=W) 
        txtlname=ttk.Entry(labelframeleft,textvariable=self.var_last_name, font=("arial",13,"bold"),width=29) 
        txtlname.grid(row=2,column=1) 
        
        #gender
        label_gender=Label(labelframeleft,font=("arial",12,"bold"),text="Gender:",padx=2,pady=6) 
        label_gender.grid(row=3,column=0,sticky=W)

        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender, font=("arial",12,"bold"),width=27,state="readonly")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(1)
        combo_gender.grid(row=3,column=1)

        #postcode
        lblpostcode=Label(labelframeleft,font=("arial",12,"bold"),text="Postcode:",padx=2,pady=6) 
        lblpostcode.grid(row=4,column=0,sticky=W) 
        txtpostcode=ttk.Entry(labelframeleft,textvariable=self.var_postcode, font=("arial",13,"bold"),width=29)
        txtpostcode.grid(row=4,column=1) 
        
        #mobilenumber 
        lblMobile=Label(labelframeleft,font=("arial",12,"bold"),text="Mobile Number:",padx=2,pady=6)
        lblMobile.grid(row=5,column=0,sticky=W) 
        txtmbno=ttk.Entry(labelframeleft,textvariable=self.var_mobilenumber, font=("arial",13,"bold"),width=29) 
        txtmbno.grid(row=5,column=1)

        #email
        lblemail=Label(labelframeleft,font=("arial",12,"bold"),text="Email",padx=2,pady=6) 
        lblemail.grid(row=6,column=0,sticky=W) 
        txtemail=ttk.Entry(labelframeleft,textvariable=self.var_email, font=("arial",13,"bold"),width=29)
        txtemail.grid(row=6,column=1) 
        
        #state
        lblnat=Label(labelframeleft,font=("arial",12,"bold"),text="State or Union Territory:",padx=2,pady=6)
        lblnat.grid(row=7,column=0,sticky=W)

        combo_nat=ttk.Combobox(labelframeleft,textvariable=self.var_state, font=("arial",12,"bold"),width=27,state="readonly")
        combo_nat["value"]=("Andaman and Nicobar Islands","Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chandigarh","Chhattisgarh","Dadra and Nagar Haveli and Daman and Diu","Delhi","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Ladakh","Lakshadweep","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Puducherry","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal")
        combo_nat.current(20)
        combo_nat.grid(row=7,column=1)
        
        #idproof
        lblid=Label(labelframeleft,font=("arial",12,"bold"),text="ID Proof:",padx=2,pady=6) 
        lblid.grid(row=8,column=0,sticky=W)

        combo_idproof=ttk.Combobox(labelframeleft,textvariable=self.var_idproof, font=("arial",12,"bold"),width=27,state="readonly")
        combo_idproof["value"]=("Aadhaar Card","Voter ID Card","Passport")
        combo_idproof.current(0)
        combo_idproof.grid(row=8,column=1)

        #idnumber
        lblidno=Label(labelframeleft,font=("arial",12,"bold"),text="ID Number:",padx=2,pady=6)
        lblidno.grid(row=9,column=0,sticky=W) 
        txtidno=ttk.Entry(labelframeleft,textvariable=self.var_idnumber, font=("arial",13,"bold"),width=29) 
        txtidno.grid(row=9,column=1)

        #address 
        lbladd=Label(labelframeleft,font=("arial",12,"bold"),text="Address:",padx=2,pady=6) 
        lbladd.grid(row=10,column=0,sticky=W) 
        txtadd=ttk.Entry(labelframeleft,textvariable=self.var_address, font=("arial",13,"bold"),width=29)
        txtadd.grid(row=10,column=1)

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

        #table_frame_search
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search Database",font=("times new roman",12,"bold"),padx=2,)
        Table_Frame.place(x=435,y=50,width=860,height=490)

        lblSearchBy=Label(Table_Frame,font=("arial",12,"bold"),text="Search By:",bg="black",fg="light blue") 
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()
        combo_search=ttk.Combobox(Table_Frame,textvariable=self.search_var, font=("arial",12,"bold"),width=24,state="readonly")
        combo_search["value"]=("mobilenumber","user_ref")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Table_Frame,textvariable=self.txt_search, font=("arial",13,"bold"),width=24) 
        txtSearch.grid(row=0,column=2,padx=2)

        btnSearch=Button(Table_Frame,text="Search",command=self.search_data,font=("arial",12,"bold"),bg="black",fg="light blue",width=9)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShow=Button(Table_Frame,text="Show All",command=self.fetch_data,font=("arial",12,"bold"),bg="black",fg="light blue",width=9)
        btnShow.grid(row=0,column=4,padx=1)

        #Show data table
        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=350)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.User_Details_Table=ttk.Treeview(details_table,column=("user_ref","first_name","last_name","gender","postcode","mobilenumber","email","state","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
 
        scroll_x.config(command=self.User_Details_Table.xview)
        scroll_y.config(command=self.User_Details_Table.yview)

        self.User_Details_Table.heading("user_ref",text="User Reference")
        self.User_Details_Table.heading("first_name",text="First Name")
        self.User_Details_Table.heading("last_name",text="Last Name")
        self.User_Details_Table.heading("gender",text="Gender")
        self.User_Details_Table.heading("postcode",text="Postcode")
        self.User_Details_Table.heading("mobilenumber",text="Mobile Number")
        self.User_Details_Table.heading("email",text="Email")
        self.User_Details_Table.heading("state",text="State or Union Territory")
        self.User_Details_Table.heading("idproof",text="ID Proof")
        self.User_Details_Table.heading("idnumber",text="ID Number")
        self.User_Details_Table.heading("address",text="Address")

        self.User_Details_Table["show"]="headings"

        self.User_Details_Table.column("user_ref",width=100)
        self.User_Details_Table.column("first_name",width=100)
        self.User_Details_Table.column("last_name",width=100)
        self.User_Details_Table.column("gender",width=100)
        self.User_Details_Table.column("postcode",width=100)
        self.User_Details_Table.column("mobilenumber",width=100)
        self.User_Details_Table.column("email",width=100)
        self.User_Details_Table.column("state",width=100)
        self.User_Details_Table.column("idproof",width=100)
        self.User_Details_Table.column("idnumber",width=100)
        self.User_Details_Table.column("address",width=100)

        self.User_Details_Table.pack(fill=BOTH,expand=1)
        self.User_Details_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()


    def add_data(self):
        if self.var_mobilenumber.get()=="" or self.var_last_name.get()=="":
            messagebox.showerror("Error","All fields are necessary!",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="767686",database="wms")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into users values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_ref.get(),self.var_first_name.get(),self.var_last_name.get(),self.var_gender.get(),self.var_postcode.get(),self.var_mobilenumber.get(),self.var_email.get(),self.var_state.get(),self.var_idproof.get(),self.var_idnumber.get(),self.var_address.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","User has been added!",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong:{str(es)}",parent=self.root)


    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="767686",database="wms")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from users")
        rows = my_cursor.fetchall()
        if len(rows)!= 0:
            self.User_Details_Table.delete(*self.User_Details_Table.get_children())
            for i in rows:
                self.User_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row = self.User_Details_Table.focus()
        content = self.User_Details_Table.item(cursor_row)
        row = content["values"]

        self.var_ref.set(row[0]),
        self.var_first_name.set(row[1]),
        self.var_last_name.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_postcode.set(row[4]),
        self.var_mobilenumber.set(row[5]),
        self.var_email.set(row[6]),
        self.var_state.set(row[7]),
        self.var_idproof.set(row[8]),
        self.var_idnumber.set(row[9]),
        self.var_address.set(row[10])


    def update(self):
        if self.var_mobilenumber.get()=="":
            messagebox.showerror("Error","Please enter valid mobile number.",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost",username="root",password="767686", database="wms")
            my_cursor = conn.cursor()
            my_cursor.execute("update users set first_name=%s, last_name=%s, gender=%s, postcode=%s, mobilenumber=%s, email=%s, state=%s, idproof=%s, idnumber=%s, address=%s where user_ref=%s",(self.var_first_name.get(),self.var_last_name.get(),self.var_gender.get(),self.var_postcode.get(),self.var_mobilenumber.get(),self.var_email.get(),self.var_state.get(),self.var_idproof.get(),self.var_idnumber.get(),self.var_address.get(),self.var_ref.get()))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","User details has been updated sucessfully!", parent=self.root)

    def dat_Delete(self):
        dat_Delete = messagebox.askyesno("Water Management System,","Do you want to delete this user?",parent=self.root)
        if dat_Delete>0:
            conn = mysql.connector.connect(host="localhost",username="root",password="767686",database="wms")
            my_cursor = conn.cursor()
            query = "delete from users where user_ref=%s"
            value = (self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not dat_Delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def data_reset(self):
        #self.var_ref.set(""),
        self.var_first_name.set(""),
        self.var_last_name.set(""),
        #self.var_gender.set(""),
        self.var_postcode.set(""),
        self.var_mobilenumber.set(""),
        self.var_email.set(""),
        #self.var_state.set(""),
        #self.var_idproof.set(""),
        self.var_idnumber.set(""),
        self.var_address.set("")

        x = random.randint(1000,9999)
        self.var_ref.set(str(x))


    def search_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="767686",database="wms")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM users WHERE " + str(self.search_var.get()) + " LIKE '%" + str(self.txt_search.get()) + "%'")
        rows_fetch = my_cursor.fetchall()
        if len(rows_fetch)!=0:
            self.User_Details_Table.delete(*self.User_Details_Table.get_children())
            for i in rows_fetch:
                self.User_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()


if __name__ == "__main__":
    root=Tk()
    obj=userwin(root)
    root.mainloop()