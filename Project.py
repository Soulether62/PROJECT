#importing modules
from tkinter import *
from tkinter.filedialog import *
from tkinter.font import *
from PIL import ImageTk
from stegano import exifHeader as stg
from tkinter import messagebox


# decoding the file


def Decode():
    Screen.destroy()
    DecScreen = Tk()
    DecScreen.state("zoomed") 
    photo=ImageTk.PhotoImage(file=r'E:\Projects\image-steganography-project\268148.jpg')
    Label(DecScreen,image=photo).pack()
    label2 = Label(DecScreen,text="Select The Encoded Image And Click On Decode Button",bg="black",fg="white",font=("times new roman",30,"italic bold"),height=1,width=48)
    label2.place(relx=0.2,rely=0.05)   
    DecScreen.title("Decoder- Soulether62")
    DecScreen.geometry("600x400+1000+100")

   
   
    def OpenFile():
        global FileOpen
        FileOpen=StringVar()
        FileOpen = askopenfilename(initialdir ="/Desktop",title="Select the File",filetypes=(("only jpeg files","*jpg"),("all type of files","*.*")))
        
   
   
    def Decoder():
        Message=stg.reveal(FileOpen)
        label3 = Label(DecScreen,text=Message,fg="green",height=1,font=("times new roman",40,"bold"))
        label3.place(relx=0.43,rely=0.2)     
    SelectButton = Button(DecScreen,bd=20,text="PICK A FILE",height=1,width=12,bg="white",font=("times new roman",30,"italic bold"),command=OpenFile)
    SelectButton.place(relx=0.25,rely=0.4)
    EncodeButton=Button(DecScreen,bd=20,text="DECODE",height=1,width=10,bg="green",font=("times new roman",30,"italic bold"),command=Decoder)
    EncodeButton.place(relx=0.6,rely=0.4)
    ExitButton1=Button(DecScreen,bd=20,text="EXIT",height=1,width=10,bg="white",font=("times new roman",30,"italic bold"),command=DecScreen.destroy)
    ExitButton1.place(relx=0.8,rely=0.8)
    ImButton=Button(h=5)


#encoding the file


def Encode():
    Screen.destroy()
    EncScreen = Tk()
    EncScreen.state("zoomed")  
    photo=ImageTk.PhotoImage(file=r'E:\Projects\image-steganography-project\268148.jpg')
    Label(EncScreen,image=photo).pack()
    photo1=ImageTk.PhotoImage(file=r'E:\Projects\image-steganography-project\encoder.png')
    EncScreen.title("Encoder- Soulether62")
    EncScreen.geometry("600x400+1000+100")



    label = Label(EncScreen,fg="white",text="Enter Confidential Message",font=("times new roman",32,"italic bold"),height=1,width=24,bg="blue")
    label.place(relx=0.1,rely=0.4)
    entry=Entry(EncScreen,width=40,bd=10,font=("times new roman",32,"italic bold"))
    entry.place(relx=0.5,rely=0.4)
    label1 = Label(EncScreen,fg="white",text="Name of the File",height=1,width=24,font=("times new roman",32,"italic bold"),bg="blue")
    label1.place(relx=0.1,rely=0.2)
    SaveEntry = Entry(EncScreen,bd=10,font=("times new roman",32,"italic bold"))
    SaveEntry.place(relx=0.5,rely=0.2)
    label2 = Label(EncScreen,text="Select The Image File And Click on ENCODE Button",bg="black",fg="white",font=("times new roman",30,"italic bold"),height=1,width=48)
    label2.place(relx=0.2,rely=0.05)

        

    def OpenFile():
        global FileOpen
        FileOpen=StringVar()
        FileOpen = askopenfilename(initialdir ="/Desktop",title="SelectFile",filetypes=(("only jpeg files","*jpg"),("all type of files","*.*")))

        label2 = Label(text=FileOpen,height=1,bd=15,font=("times new roman",32,"italic bold"))
        label2.place(relx=0.4,rely=0.6)


    def Encoder():
        Response= messagebox.askyesno("PopUp","Do you want to encode the image?")
        if Response == 1:
            stg.hide(FileOpen,SaveEntry.get()+".jpg",entry.get())
            messagebox.showinfo("Pop Up","Your message is Successfully Encoded")
        else:
            messagebox.showwarning("Pop Up","Unsuccessful, please try again")



    SelectButton = Button(EncScreen,text="Select the file",height=1,width=12,bg="blue",bd=15,font=("times new roman",20,"italic bold"),command=OpenFile)
    SelectButton.place(relx=0.2,rely=0.6)
    EncodeButton=Button(EncScreen,text="ENCODE",height=100,width=500,bg="red",image=photo1,bd=20,compound=LEFT,font=("times new roman",40,"italic bold"),command=Encoder)
    EncodeButton.place(relx=0.37,rely=0.7)
    ExitButton2=Button(EncScreen,text="EXIT",font=("times new roman",30,"italic bold"),bd=20,height=1,width=10,bg="white",command=EncScreen.destroy)
    ExitButton2.place(relx=0.8,rely=0.8)
    EncodeButton=Button(EncScreen,h=5)



#Initializing the screen


Screen = Tk()
Screen.title("Steganography By Soulether62 ")
Screen.state("zoomed")
Screen.geometry("600x400+1000+100")
photo=ImageTk.PhotoImage(file=r'E:\Projects\image-steganography-project\4643038.jpg')
Label(Screen,image=photo).pack()
cross=PhotoImage(file=r'E:\Projects\image-steganography-project\cross.png')
cross0=cross.subsample(12,12)
photo5=PhotoImage(file=r'E:\Projects\image-steganography-project\encoding.png')
photo6=photo5.subsample(5,5)
photo7=PhotoImage(file=r'E:\Projects\image-steganography-project\encoder.png')
photo8=photo7.subsample(3,3)
label2 = Label(Screen,text="IMAGE   STEGANOGRAPHY",bg="black",fg="white",font=("times new roman",50,"italic bold"),height=1,width=48)
label2.place(relx=0.02,rely=0.05)


def Exit():
    Screen.destroy()


    #creating buttons


EncodeButton = Button(text="ENCODE ",bd=20,font=("times new roman",30,"italic bold"),image=photo8,compound=LEFT,bg="red",width=300,height=100,command=Encode)
EncodeButton.place(relx=0.25,rely=0.4)

DecodeButton = Button(text="DECODE",bd=10,font=("times new roman",30,"italic bold"),image=photo6,compound=LEFT,bg="blue",width=300,height=100,command=Decode)
DecodeButton.place(relx=0.6,rely=0.4)

ExitButton = Button(text="CLOSE",bd=3,image=cross0,font=("times new roman",30,"italic bold"),height=35,width=160,compound=LEFT,bg="white",command=Exit)
ExitButton.place(relx=0.8,rely=0.8)


mainloop()