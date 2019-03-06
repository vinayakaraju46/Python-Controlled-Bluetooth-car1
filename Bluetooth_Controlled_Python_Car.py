from Tkinter import *

import bluetooth

print "Searching for devices....."
print ""

nearby_devices = bluetooth.discover_devices()

num = 0
print "Select your device by entering its corresponding number....."
for i in nearby_devices:
    num+=1
    print num , ": ", bluetooth.lookup_name(i)

selection = input("> ") - 1
print "You have selected", bluetooth.lookup_name(nearby_devices[selection])
bd_addr = nearby_devices[selection]
port = 1




class MyBtn(Button):
    # set function to call when pressed
    def set_down(self,fn):
        self.bind('<Button-1>',fn)
     
    # set function to be called when released
    def set_up(self,fn):
        self.bind('<ButtonRelease-1>',fn)






class Window(Frame):
    sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
    def __init__(self, master=None):
        self.sock.connect((bd_addr, port))
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Hold")
        self.pack(fill=BOTH, expand=5)
        
        btn = MyBtn(self,text = 'FORWARD')
        btn.place(x=150, y=60, height=50, width=80)
        btn.set_up(self.on_up)
        btn.set_down(self.on_down)

        
        btn1 = MyBtn(self,text = 'BACKWARD ')
        btn1.place(x=150, y=200, height=50, width=80)
        btn1.set_up(self.on_up1)
        btn1.set_down(self.on_down1)


        btn2 = MyBtn(self,text = 'RIGHT ')
        btn2.place(x=250, y=60, height=50, width=80)
        btn2.set_up(self.on_up2)
        btn2.set_down(self.on_down2)

        btn3 = MyBtn(self,text = 'LEFT ')
        btn3.place(x=50, y=60, height=50, width=80)
        btn3.set_up(self.on_up3)
        btn3.set_down(self.on_down3)

        btn4 = MyBtn(self,text = 'HARD LEFT ')
        btn4.place(x=50, y=130, height=50, width=80)
        btn4.set_up(self.on_up4)
        btn4.set_down(self.on_down4)

        btn5 = MyBtn(self,text = 'HARD RIGHT ')
        btn5.place(x=250, y=130, height=50, width=80)
        btn5.set_up(self.on_up5)
        btn5.set_down(self.on_down5)

        btn6 = MyBtn(self,text = 'REVERSE \n RIGHT ')
        btn6.place(x=250, y=200, height=50, width=80)
        btn6.set_up(self.on_up6)
        btn6.set_down(self.on_down6)

        btn7 = MyBtn(self,text = 'REVERSE \n LEFT')
        btn7.place(x=50, y=200, height=50, width=80)
        btn7.set_up(self.on_up7)
        btn7.set_down(self.on_down7)



        

        # function called when pressed
    def on_down(self,x):
        print("FRONT")
        self.sock.send(b'1')
    def on_up(self,x):
        print("STOP")
        self.sock.send(b'9')
        
    def on_down1(self,x):
        print("BACK")
        self.sock.send(b'0')     
    def on_up1(self,x):
        print("STOP")
        self.sock.send(b'9')
        
    def on_down2(self,x):
        print("FORWARD RIGHT")
        self.sock.send(b'2')
    def on_up2(self,x):
        print("STOP")
        self.sock.send(b'9')


    def on_down3(self,x):
        print("FORWARD LEFT")
        self.sock.send(b'3')  
    def on_up3(self,x):
        print("STOP")
        self.sock.send(b'9')
        
    def on_down4(self,x):
        print("HARD RIGHT")
        self.sock.send(b'5')
    def on_up4(self,x):
        print("STOP")
        self.sock.send(b'9')
        
    def on_down5(self,x):
        print("HARD LEFT")
        self.sock.send(b'4')
    def on_up5(self,x):
        print("STOP")
        self.sock.send(b'9')

        
    def on_down6(self,x):
        print("BACKWARD RIGHT")
        self.sock.send(b'6')
    def on_up6(self,x):
        print("STOP")
        self.sock.send(b'9')

    def on_down7(self,x):
        print("BACKWARD LEFT")
        self.sock.send(b'7')
    
    def on_up7(self,x):
        print("STOP")
        self.sock.send(b'9')

    
if __name__ == "__main__":

        root = Tk()
        root.geometry("400x400")
        app = Window(master=root)

        app.mainloop()
        root.destroy()        
