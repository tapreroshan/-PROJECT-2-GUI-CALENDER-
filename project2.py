from tkinter import *
from tkcalendar import *
r=Tk()
def chose_date():
    present_date=disply_cal.get_date()
    user_date = Label(text=present_date)
    user_date.pack(padx=2,pady=2)
disply_cal= Calendar(r,setmode="Day",date_pattern='d/m/yy')
disply_cal.pack(padx=15,pady=15)
open_cal=Button(r,text="select date",bg="red",activebackground="white",command=chose_date)
open_cal.pack(padx=15,pady=15)
#geometry gives dimension
r.geometry('500x500')
#title is used to give the title to calander
r.title("My GUI CALENDER")
# for the background colour
r.configure(bg="skyblue")
r.mainloop()