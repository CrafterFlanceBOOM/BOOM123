import time,os
worldname = 'Default World'
print ("Loading Maintic Blocks.... ",worldname)
time.sleep(2)
print ("Loading.")
time.sleep(2)
os.system('cls')
time.sleep(0.2)
print ("Loading...")
time.sleep(2)
os.system('cls')
time.sleep(0.2)
print ("Loaded!")


from tkinter import *


print ("Maintic Blocks Beta (Control Pack)")

w = 0
num_x = 0
tmp = [0]
  
def rd_move(event):

    print ('move',w.get())
    #print (w, type(w))
    
    num_x = w.get()
    tmp.append(num_x)
    
    previous = tmp[-2]
    
    if previous < num_x:
        print ('forward', 'prev',previous, 'current',num_x)
        canvas.move(test, num_x, 0)
    else:
        print ('backward','prev',previous, 'current',num_x)
        canvas.move(test, -num_x, 0)
    
def destroy():
    print ('Character was kicked out of game')
    canvas.destroy()

def clear_text():
    os.system('cls')
def char_inf():
    print ("Name: Character")
    print ("Nickname: Shadesic")
    print ("I'm a generated character in manticblocks!")
    print ("char_inf by BP")
    
def make_img():
    global canvas
    global test
    canvas = Canvas(master, width = 900, height = 300)      
    canvas.pack()      
    
    
    print ("[FILEMENU] Character respawned")
    test = canvas.create_image(20,20, anchor=NW, image=img)
def open_credits(event):
    os.system('C:\\Users\\brand\\Desktop\\f.manticblocks\\credits.txt')
    
master = Tk()  
w = Scale(master, from_=0, to=40, orient=HORIZONTAL, command=rd_move) 
w.pack()
img = PhotoImage(file="C:\\Users\\brand\\Desktop\\f.manticblocks\\person.png") #The person picture.   
make_img()
'''
canvas = Canvas(master, width = 900, height = 300)      
canvas.pack()      
img = PhotoImage(file="person.png") #The person picture.     
test = canvas.create_image(20,20, anchor=NW, image=img)
'''
menu = Menu(master) 
master.config(menu=menu) 
filemenu = Menu(menu) 
menu.add_cascade(label='Character', menu=filemenu) 
filemenu.add_command(label='Ban Character', command=destroy)
filemenu.add_command(label='Respawn Character', command=make_img)    
filemenu.add_separator() 
filemenu.add_command(label='Exit', command=master.quit) 
helpmenu = Menu(menu) 
menu.add_cascade(label='PyWindow', menu=helpmenu) 
helpmenu.add_command(label='Clear Text on PyWindow', command=clear_text)
helpmenu.add_command(label='Character Info...', command=char_inf)
l = Label(master, text='Hello. You are using MainticBlocks 1.0, so this is early released!') 
l.pack()
mainloop()
