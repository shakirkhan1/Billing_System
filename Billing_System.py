from Tkinter import *
from tkMessageBox import *

root=Tk()
root.title("Billing System")
root.geometry("480x400+0+0")
#root.resizable('0,0')
root.configure(background='DarkGoldenrod')
Label(root,text='  Select Your Breakfast  ',font='times 23 bold ',bg='DarkGoldenrod',borderwidth=8,width=16).grid(row=0,column=1,columnspan=2)
Label(root,text='(Breakfast Calculator)',font='times 19 bold ',bg='DarkGoldenrod',borderwidth=6,width=17).grid(row=1,column=1,columnspan=2)

#--------------------------------------------------------------------------
v1=IntVar()
v2=IntVar()
v3=IntVar()
v4=IntVar()
v5=IntVar()
v6=IntVar()
v7=IntVar()
v8=IntVar()
v8=IntVar()
v9=IntVar()
v10=IntVar()
v11=IntVar()
v12=IntVar()
v13=IntVar()
v14=IntVar()
v15=IntVar()
v16=IntVar()
#----------------------------------------------------------------------------------

Checkbutton(root,text='macroni(105)     ',variable=v1,onvalue=1,anchor=W,width=15,bg='DarkGoldenrod4').grid(row=2,column=0)
Checkbutton(root,text='sandwich(80)     ',variable=v2,onvalue=2,anchor=W,width=15,bg='DarkGoldenrod4').grid(row=3,column=0)
Checkbutton(root,text='Aloo paratha(200)',variable=v3,onvalue=3,anchor=W,width=15,bg='DarkGoldenrod4').grid(row=4,column=0)
Checkbutton(root,text='poha(50)         ',variable=v4,onvalue=4,anchor=W,width=15,bg='DarkGoldenrod4').grid(row=5,column=0)
Checkbutton(root,text='noodles(120)     ',variable=v5,onvalue=5,anchor=W,width=15,bg='DarkGoldenrod4').grid(row=6,column=0)
Checkbutton(root,text='egg(20)          ',variable=v6,onvalue=6,anchor=W,width=15,bg='DarkGoldenrod4').grid(row=7,column=0)
Checkbutton(root,text='idli(60)         ',variable=v7,onvalue=7,anchor=W,width=15,bg='DarkGoldenrod4').grid(row=8,column=0)
Checkbutton(root,text='upma(70)         ',variable=v8,onvalue=8,anchor=W,width=15,bg='DarkGoldenrod4').grid(row=9,column=0)

Checkbutton(root,text='pav bhaji(110)   ',variable=v9,onvalue=9,anchor=W,width=15,bg='DarkGoldenrod4').grid(row=2,column=2)
Checkbutton(root,text='pastha(80)       ',variable=v10,onvalue=10,anchor=W,width=15,bg='DarkGoldenrod4').grid(row=3,column=2)
Checkbutton(root,text='omlete(30)       ',variable=v11,onvalue=11,anchor=W,width=15,bg='DarkGoldenrod4').grid(row=4,column=2)
Checkbutton(root,text='fruits(40)       ',variable=v12,onvalue=12,anchor=W,width=15,bg='DarkGoldenrod4').grid(row=5,column=2)
Checkbutton(root,text='bread butter(20) ',variable=v13,onvalue=13,anchor=W,width=15,bg='DarkGoldenrod4').grid(row=6,column=2)
Checkbutton(root,text='sprouts          ',variable=v14,onvalue=14,anchor=W,width=15,bg='DarkGoldenrod4').grid(row=7,column=2)
Checkbutton(root,text='porage(55)       ',variable=v15,onvalue=15,anchor=W,width=15,bg='DarkGoldenrod4').grid(row=8,column=2)
Checkbutton(root,text='milk corn flakes ',variable=v16,onvalue=16,anchor=W,width=15,bg='DarkGoldenrod4').grid(row=9,column=2)
#----------------------------------------------------------------------------------------
def add(x):
    a=0
    for i in x:
        a=a+i
    Label(root,text="total amount is: ").grid(row=12,column=1,columnspan=1)
    Label(root,text=a).grid(row=12,column=2,columnspan=2)
    Label(root,text="INR").grid(row=12,column=3)
    if a!=0:
        showinfo("ENJOYED","Have a good day")
    else:
        showinfo("NOT ENJOYED","no items ordered")
    #clear()



def sett():
    x=[]
    if(v1.get()==1):
        x.append(105)
    if(v2.get()==2):
        x.append(80)
    if(v3.get()==3):
        x.append(200)
    if(v4.get()==4):
        x.append(50)
    if(v5.get()==5):
        x.append(120)
    if(v6.get()==6):
        x.append(20)
    if(v7.get()==7):
        x.append(60)
    if(v8.get()==8):
        x.append(70)
    if(v9.get()==9):
        x.append(110)
    if(v10.get()==10):
        x.append(80)
    if(v11.get()==11):
        x.append(30)
    if(v12.get()==12):
        x.append(40)
    if(v13.get()==13):
        x.append(20)
    if(v14.get()==14):
        x.append(65)
    if(v15.get()==15):
        x.append(55)
    if(v16.get()==16):
        x.append(25)
    add(x)    
#----------------------------------------------------------------------------------------


def q():
    s=askyesno("quit system","Are you sure")
    if s>0:
        root.destroy()
        return


Button(root,text='CheckRs',command=sett,bg='dark grey').grid(row=11,column=0,columnspan=2)
Button(root,text='Exit',command=q,bg='dark grey').grid(row=11,column=1)


root.mainloop()
