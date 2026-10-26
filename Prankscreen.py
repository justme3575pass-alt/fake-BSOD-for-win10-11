import tkinter as tk
import random as rn
import socket
import datetime
import sys
import os
import ctypes
import time
import math
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
sth=AudioUtilities.GetSpeakers().EndpointVolume.GetMasterVolumeLevelScalar()
def toggle_mute(vol):
    device = AudioUtilities.GetSpeakers()
    volume = device.EndpointVolume
    volume.SetMasterVolumeLevelScalar(vol, None)
toggle_mute(vol=0.0)
origin=tk.Tk()
origin.withdraw()
origin.grab_set()
def keyblock(event):
    return "break"
origin.bind_all("<Key>",lambda e: keyblock(e))
def glitchingeffect():
    root=tk.Toplevel(origin)
    root.title("Window_Error(s)_Operation_Failed")
    root.geometry("1300x700")
    root.config(bg="blue")
    root.attributes("-fullscreen",True)
    root.attributes("-topmost", True)
    root.overrideredirect(True)
    root.grab_set()
    for i in range(1,25):
            window=tk.Toplevel(root)
            window.attributes("-topmost", True)
            window.title(f"Error{rn.randint(100,999)}")
            window.geometry("900x500")
            window.config(bg="black")
            window.grab_set()
            root.after(100+i*2,lambda window=window: window.destroy())
    for i in range(1,25):
            window=tk.Toplevel(root)
            window.attributes("-topmost", True)
            window.title(f"Error{rn.randint(100,999)}")
            window.geometry("300x200")
            window.config(bg="#2e2e2e")
            window.grab_set()
            root.after(100+i*2,lambda window=window: window.destroy())
    for i in range(1,25):
            window=tk.Toplevel(root)
            window.attributes("-topmost", True)
            window.title(f"Error{rn.randint(100,999)}")
            window.geometry("500x300")
            window.config(bg="#2e2e2e")
            window.grab_set()
            root.after(100+i*2,lambda window=window: window.destroy())
    for i in range(1,25):
            window=tk.Toplevel(root)
            window.attributes("-topmost", True)
            window.title(f"Error{rn.randint(100,999)}")
            window.geometry("1000x500")
            window.config(bg="#2e2e2e")
            window.grab_set()
            root.after(100+i*2,lambda window=window: window.destroy())
    root.after(2000,lambda: root.destroy())
    origin.after(2000,lambda: openfaketerminal())
def openfaketerminal():
    faketerminal=tk.Toplevel(origin)
    faketerminal.title("Terminal")
    faketerminal.attributes("-topmost", True)
    faketerminal.config(bg="black")
    faketerminal.geometry("1300x700")
    width=faketerminal.winfo_screenwidth()
    faketerminal.grab_set()
    fakebar=tk.Canvas(faketerminal,width=width-3,height=30,background="grey2")
    fakebar.place(x=0,y=0,anchor="nw")
    fakebar.create_text(4,2,text=">_",font=("Segoe UI Boot",-24),fill="white",justify="left",anchor="nw")
    fakebar.create_text(45,7,text="Terminal",font=("Segoe UI Boot",-24),fill="#aeadad",justify="left",anchor="nw")
    faketerminal.attributes("-fullscreen",True)
    cs=rn.randint(10,50)
    ct=datetime.datetime.now().strftime('%a_%d/%m/%Y - %H:%M:')
    filename = os.path.basename(sys.executable if getattr(sys, 'frozen', False) else __file__)
    txt=f"SystemClock: {ct+str(cs)}\nTraceback (most recent call last):\n{ct+str(cs)}: External intervention from '{filename}' detected\n{ct+str(cs+1)}: Third-party Software '{filename}' has taken Administrator role in: C:/Windows/System32\n{ct+str(cs+1)}: Third-party Software '{filename}' has made significant changes on your\nsystem configuration, at C:/Windows/System32\n{ct+str(cs+2)}: {socket.gethostname()} has encountered a fatal error\n{ct+str(cs+3)}: Device: {socket.gethostname()} unable to access driver: 'C:'\nErrorCode: 5(ACCESS_DENIED)\n{ct+str(cs+3)}: Device: {socket.gethostname()}is asking for Permission Level: 'Full Control' from Control Panel: User Account\n{ct+str(cs+5)}: Permission is given to: Device {socket.gethostname()}\n{ct+str(cs+5)}: Device: {socket.gethostname()} has successfully accessed driver: 'C:'\n{ct+str(cs+5)}: Device:{socket.gethostname()} has successfully accessed folder: 'System32'\n{ct+str(cs+6)}: Device {socket.gethostname()} missing all dll files(Originally Registered: {len([f for f in os.listdir(r'C:\Windows\System32') if f.lower().endswith('.dll')])})\n{ct+str(cs+6)}: It seems like your folder: 'System32' is currently empty\n{ct+str(cs+6)}: An Unexpected Error has occurred:\n{ct+str(cs+7)}: Operating efforts failed(OPERATION_FAILURE)\n{ct+str(cs+7)}: System core activation failed(STARTING_FAILURE)\n{ct+str(cs+8)}: System reactivation failed(REBOOT_FAILURE)\n{ct+str(cs+8)}: System deactivation failed(CLOSING_FAILURE)\nThis device must be restarted in case of information loss\nFor further details, visit our website at https://support.microsoft.com/vi-vn/\n_"
    text=tk.Label(faketerminal,text=txt,font=("Cascadia Mono",12),fg="white",bg="black",justify="left")
    def flickering():
         text.config(text=txt[:-1])
         faketerminal.after(750,lambda: text.config(text=txt))
         faketerminal.after(1500,lambda: flickering())
    flickering()
    text.place(x=10,y=40,anchor="nw")
    faketerminal.after(4100,lambda: faketerminal.destroy())
    origin.after(4000,lambda:bsod())
def  bsod():
    errorscreen=tk.Toplevel(origin)
    errorscreen.geometry("1300x700")
    errorscreen.attributes("-topmost", True)
    errorscreen.attributes("-fullscreen",True)
    errorscreen.config(cursor="none")
    w=errorscreen.winfo_screenwidth()
    h=errorscreen.winfo_screenheight()
    errorscreen.grab_set()
    canvas=tk.Canvas(errorscreen,width=w,height=h,bg="#0177D7")
    canvas.place(relx=0.5,rely=0.5,anchor="center")
    percent=-1
    percentage=tk.Label(canvas,text=f"{percent}% complete",font=("Segoe UI Light",-33),fg="white",bg="#0177D7")
    percentage.place(x=0.1*w,y=0.525*h)
    def risingpercent():
        nonlocal percent,percentage
        ctypes.windll.user32.mouse_event(0x0001, 1, 0, 0, 0)  # Move +1 X
        ctypes.windll.user32.mouse_event(0x0001, -1, 0, 0, 0)
        if percent<100:
            percent+=1
            errorscreen.after(2000+rn.randint(-1000,2000),risingpercent)
            percentage.config(text=f"{percent}% complete")
        elif percent>=100:
             fakerestart=tk.Toplevel(origin)
             fakerestart.attributes("-fullscreen",True)
             fakerestart.attributes("-topmost",True)
             fakerestart.config(bg="#2047A7")
             loading=tk.Canvas(fakerestart,width=1300,height=700,background="#2047A6",highlightthickness=0,bd=0,relief="flat")
             loading.place(relx=0.5,rely=0.44,anchor="center")
             text=tk.Label(fakerestart,text="   Restarting...",font=("Segoe UI Boot",19),bg="#2047A7",fg="white",justify="center")
             text.place(relx=0.5,rely=0.54,anchor="center")
             rotatingpoints=[]
             for i in range(6):
                  dot=loading.create_oval(0,0,5,5,fill="white",outline="")
                  rotatingpoints.append(dot)
             angle=0
             def rotating():
                nonlocal angle
                for i,dot in enumerate(rotatingpoints):
                    angleforad=angle+i*(360/18)
                    radian=math.radians(angleforad)
                    x=650+25*math.cos(radian)
                    y=350+25*math.sin(radian)
                    loading.moveto(dot,x-3,y-3)
                if  angle<180:
                    angle+=3
                elif 360>angle>=180:
                    angle+=5
                elif angle>=360:
                    angle=0
                fakerestart.after(15,lambda: rotating())
             rotating()
             fakerestart.after(15000,lambda:fakerestart.config(bg="black"))
             fakerestart.after(15000,lambda:text.place_forget())
             fakerestart.after(15000,lambda:loading.place_forget())
             fakerestart.after(15000,lambda:fakerestart.config(cursor="none"))
             errorscreen.after(17000,lambda:origin.destroy())
             fakerestart.protocol("WM_DELETE_WINDOW",lambda: toggle_mute(vol=sth))
             finalmessage=tk.Tk()
             finalmessage.geometry("250x100")
             credit=tk.Label(finalmessage,text="You've been trolled lol:))",font=("Arial",50))
             credit.place(relx=0.5,rely=0.5,anchor="center")
             finalmessage.attributes("-fullscreen",True)
             finalmessage.after(19000,lambda: finalmessage.destroy())
             finalmessage.mainloop()
    risingpercent()
    canvas.create_text(0.1*w,0.2*h,text=":(",font=("Segoe UI Light",-120),fill="white",anchor="w")
    canvas.create_text(0.1*w,0.405*h,text="Your PC ran into a problem and needs to restart. We're \njust collecting some error info, and then we'll restart for \nyou.",font=("Segoe UI Light",-28),fill="white",anchor="w")
    canvas.create_text(0.1*w,0.655*h,text="For more information about this issue and possible fixes, visit our website.\n\n\nIf you call a support person, give them this info:\n\nStop code: 0x0000007B",font=("Segoe UI",-15),fill="white",anchor="nw")
    errorscreen.protocol("WM_DELETE_WINDOW",lambda: origin.destroy())
    errorscreen.after(400000,lambda: origin.unbind("<Key>"))
    errorscreen.after(400000,lambda: origin.grab_release())
    errorscreen.after(400000,lambda: errorscreen.unbind("<Key>"))
    errorscreen.after(400000,lambda: errorscreen.grab_release())
glitchingeffect()
def tem(event):
    toggle_mute(vol=sth)
origin.bind("<Destroy>",tem)
origin.mainloop()
