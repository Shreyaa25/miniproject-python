from tkinter import *
from tkinter import ttk
import webbrowser

class InfoPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Water Management System Info")
        self.root.geometry("1330x680+194+150")

        # Title
        lbl_title = Label(self.root, text="Water Management System", font=("times new roman", 18, "bold"), bg="black", fg="light blue", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1330, height=50)

        #image
        self.water_system_image = PhotoImage(file="wms-images/water3.png")
        lbl_image = Label(self.root, image=self.water_system_image)
        lbl_image.place(x=430, y=51)
        self.root.resizable(False, False)

        # Group Members Frame
        frame_members = LabelFrame(self.root, bd=2, relief=RIDGE, text="Group Members", font=("times new roman", 12, "bold"), padx=2)
        frame_members.place(x=5, y=60, width=425, height=150)

        members = [
            "Manas Gajare",
            "Nishita Patel",
            "Shreya Patil",
            "Sanket Sawant"
        ]

        lbl_members = Label(frame_members, text="\n".join(members), font=("arial", 12), padx=2, pady=6)
        lbl_members.pack(expand=True)

        # Helpline Numbers Frame
        frame_helpline = LabelFrame(self.root, bd=2, relief=RIDGE, text="Water Related Helpline Numbers in India", font=("times new roman", 12, "bold"), padx=2)
        frame_helpline.place(x=5, y=220, width=425, height=150)

        helplines = [
            "Central Helpline: 112",
            "State Helpline: 101",
            "Flood Control: 102",
            "Water Board: 103"
        ]

        lbl_helplines = Label(frame_helpline, text="\n".join(helplines), font=("arial", 12), padx=2, pady=6)
        lbl_helplines.pack(expand=True)

        # Disaster Helpline Numbers Frame
        frame_disaster = LabelFrame(self.root, bd=2, relief=RIDGE, text="Disaster Related Helpline Numbers", font=("times new roman", 12, "bold"), padx=2)
        frame_disaster.place(x=5, y=380, width=425, height=150)

        disaster_helplines = [
            "National Emergency Number: 112",
            "NDMA (Disaster Management): 1078",
            "NDRF Helpline: 9711077372"
        ]

        lbl_disaster_helplines = Label(frame_disaster, text="\n".join(disaster_helplines), font=("arial", 12), padx=2, pady=6)
        lbl_disaster_helplines.pack(expand=True)

        # Further Reading Frame
        frame_reading = LabelFrame(self.root, bd=2, relief=RIDGE, text="Further Reading on Water Related Issues", font=("times new roman", 12, "bold"), padx=2)
        frame_reading.place(x=5, y=540, width=425, height=120)

        # Function to open URLs
        def open_url(url):
            webbrowser.open_new_tab(url)

        # Websites for further reading
        websites = {
            "World Water Council": "http://www.worldwatercouncil.org",
            "Water.org": "https://water.org",
            "UN Water": "https://www.unwater.org"
        }

        # Create buttons for each website
        for i, (text, url) in enumerate(websites.items()):
            btn = Button(frame_reading, text=text, command=lambda url=url: open_url(url), font=("arial", 10), padx=2, pady=2)
            btn.pack(pady=2)

        # Make the window not resizable
        self.root.resizable(False, False)

if __name__ == "__main__":
    root = Tk()
    obj = InfoPage(root)
    root.mainloop()