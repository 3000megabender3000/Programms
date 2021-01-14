from tkinter import *

def output1(event):
    label['text']=1
def output2(event):
    label['text']=2    
def output3(event):
    label['text']=3       
root=Tk()
root.title('Easy calculator')

label = Label(root,text='',bg='white',height=2,width=12,fill=X)

but1=Button(root,text='1',height=2,width=3)
but2=Button(root,text='2',height=2,width=3)
but3=Button(root,text='3',height=2,width=3)

but1.grid(row=1,column=0)
but2.grid(row=1,column=1)
but3.grid(row=1,column=2)

but1.bind("<Button-1>",output1)
but2.bind("<Button-1>",output2)
but3.bind("<Button-1>",output3)

label.grid(row=0,columnspan=3)

root.mainloop()