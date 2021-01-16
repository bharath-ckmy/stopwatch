from tkinter import *
from datetime import *
running=False
counter=66600
def clock_start1(label):
    def count():
        if running==True:
            global counter
            if counter==6600:
                display="Starting..."
            else: 
                tt = datetime.fromtimestamp(counter) 
                string = tt.strftime("%H:%M:%S") 
                display=string  
            label['text']=display
            label['font']='Verdana 15 bold'
            label.after(1000,count)
            counter=counter+1
            print(counter)
        else:
            print("stop")
    count()
def clock_start(label):
    global running
    running=True
    clock_start1(label)
def clock_stop():
    global running
    running=False
def clock_reset(label):
     global counter  
     counter=66600
      
     if running==False:        
         label['text']='Welcome!'
      
     else:                 
         label['text']='Starting...'
root=Tk()
root.minsize(width=250, height=70)
root.title("Clock")
label=Label(text="Welcome")
label.pack()
f=Frame(root)
f.pack(anchor = 'center',pady=5)
button_1=Button(f,text="start",command=lambda:clock_start(label))
button_1.pack(side="left")
button_2=Button(f,text="stop",command=clock_stop)
button_2.pack(side="left")
button_3=Button(f,text="reset",command=lambda:clock_reset(label))
button_3.pack(side="left")

root.mainloop()
