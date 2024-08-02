from tkinter import*
from PIL import Image,ImageTk #pip install pillow
from user import userwin
from complaint import complaint
from comtype import comtype 
from aboutus import InfoPage

class wms:
    def __init__(self,root):
        self.root=root
        self.root.title("Water Management System")
        self.root.geometry("1535x800+0+0")
        self.root.attributes('-fullscreen',True)
        
        #First Image
        img1=Image.open(r"C:\Users\Sanket sawant\Documents\Mini - Project\wms-images\water1.png") #used r to convert backward slash to forward slash
        img1=img1.resize((1535,100), Image.LANCZOS) 
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1535,height=100)

        #top image
        img3=Image.open(r"C:\Users\Sanket sawant\Documents\Mini - Project\wms-images\water3.jpg") #used r to convert backward slash to forward slash
        img3=img3.resize((1550,140), Image.LANCZOS) 
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg=Label(self.root,image=self.photoimg3,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)

        #Logo
        img2=Image.open(r"C:\Users\Sanket sawant\Documents\Mini - Project\wms-images\water2.png") #used r to convert backward slash to forward slash
        img2=img2.resize((150,100), Image.LANCZOS) 
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,relief=RIDGE)
        lblimg.place(x=0,y=0,width=150,height=100)

        #Title
        lbl_title=Label(self.root,text="WATER MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="black",fg="light blue",relief=RIDGE)
        lbl_title.place(x=0,y=100,width=1537,height=50)

        #Main Frame
        main_frame=Frame(self.root,relief=RIDGE,bg="sky blue")
        main_frame.place(x=0,y=150,width=1535,height=713)

        #bg image
        img4=Image.open(r"C:\Users\Sanket sawant\Documents\Mini - Project\wms-images\water4.png") #used r to convert backward slash to forward slash
        img4=img4.resize((1335,715), Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg4=Label(self.root,image=self.photoimg4,relief=RIDGE)
        lblimg4.place(x=200,y=150,width=1335,height=715)

        #Menu
        lbl_menu=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="gold",relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=200)

        #Button Frame
        btn_frame=Frame(main_frame,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=200,height=207)

        user_btn=Button(btn_frame,text="USER",command=self.user_details,width=18,font=("times new roman",14,"bold"),bg="black",fg="light blue",relief=RIDGE,cursor="hand2")
        user_btn.grid(row=0,column=0,pady=1)

        cmpt_btn=Button(btn_frame,text="COMPLAINT",command=self.complaint_details, width=18,font=("times new roman",14,"bold"),bg="black",fg="light blue",relief=RIDGE,cursor="hand2")
        cmpt_btn.grid(row=1,column=0,pady=1)

        ct_btn=Button(btn_frame,text="COMPLAINT TYPE",command=self.comtype, width=18,font=("times new roman",14,"bold"),bg="black",fg="light blue",relief=RIDGE,cursor="hand2")
        ct_btn.grid(row=2,column=0,pady=1)

        report_btn=Button(btn_frame,text="ABOUT US & INFO",command=self.aboutus, width=18,font=("times new roman",14,"bold"),bg="black",fg="light blue",relief=RIDGE,cursor="hand2")
        report_btn.grid(row=3,column=0,pady=1)

        logout_btn=Button(btn_frame,text="LOGOUT",command=self.logout, width=18,font=("times new roman",14,"bold"),bg="black",fg="light blue",relief=RIDGE,cursor="hand2")
        logout_btn.grid(row=4,column=0,pady=1)

        r'''
        Right Side Image

        img3=Image.open(r"C:\Users\Sanket sawant\Documents\Mini - Project\wms-images\right-side-image.png")
        img3=img3.resize((1310,610),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg1=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg1.place(x=225,y=0,width=1310,height=610)

        #Down Images

        img4=Image.open(r"C:\Users\Sanket sawant\Documents\Mini - Project\wms-images\water2.png")
        img4=img4.resize((230,210),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg1=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg1.place(x=0,y=225,width=230,height=210)


        img5=Image.open(r"C:\Users\Sanket sawant\Documents\Mini - Project\wms-images\water1.png")
        img5=img5.resize((230,190),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lblimg1=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lblimg1.place(x=0,y=420,width=230,height=190)
        '''
 
    def user_details(self):
        self.new_window=Toplevel(self.root)
        self.app=userwin(self.new_window)

    def complaint_details(self):
        self.new_window=Toplevel(self.root)
        self.app=complaint(self.new_window)

    def comtype(self):
        self.new_window=Toplevel(self.root)
        self.app=comtype(self.new_window)

    def aboutus(self):
        self.new_window=Toplevel(self.root)
        self.app=InfoPage(self.new_window)

    def logout(self):
        self.root.destroy()

if __name__=="__main__":
    root=Tk()
    obj=wms(root)
    root.mainloop()