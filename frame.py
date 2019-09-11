import tkinter as tk
from tkinter import*

master=tk.Tk()
def button_input(num):
    global operator
    operator=operator+str(num)
    input_text.set(operator)
def clear_button():
    global operator
    operator=''
    input_text.set(operator)
def equal_button():
    global operator
    sumup=str(eval(operator))
    input_text.set(sumup)
    operator=operator
master.title('Calculator')
input_text=StringVar()
operator=''
entry=Entry(master,width=40,justify='right',textvariable=input_text).grid(row=0,column=1,columnspan=4)
button11=Button(master,text='1',padx=16,command=lambda:button_input(1))
button11.grid(row=1,column=1)

button12=Button(master,text='2',padx=16,command=lambda : button_input(2))
button12.grid(row=1,column=2)
button13=Button(master,text='3',padx=16,command=lambda:button_input(3))
button13.grid(row=1,column=3)
button14=Button(master,text='/',padx=16,command=lambda:button_input('/'))
button14.grid(row=1,column=4)
button21=Button(master,text='4',padx=16,command=lambda:button_input(4))
button21.grid(row=2,column=1)
button22=Button(master,text='5',padx=16,command=lambda:button_input(5))
button22.grid(row=2,column=2)
button23=Button(master,text='6',padx=16,command=lambda:button_input(6))
button23.grid(row=2,column=3)
button24=Button(master,text='*',padx=16,command=lambda:button_input('*'))
button24.grid(row=2,column=4)
button31=Button(master,text='7',padx=16,command=lambda:button_input(7))
button31.grid(row=3,column=1)
button32=Button(master,text='8',padx=16,command=lambda:button_input(8))
button32.grid(row=3,column=2)
button33=Button(master,text='9',padx=16,command=lambda:button_input(9))
button33.grid(row=3,column=3)
button34=Button(master,text='+',padx=15,command=lambda:button_input('+'))
button34.grid(row=3,column=4)
button41=Button(master,text='C',padx=16,command=lambda:clear_button())
button41.grid(row=4,column=1)
button42=Button(master,text='0',padx=16,command=lambda:button_input(0))
button42.grid(row=4,column=2)
button43=Button(master,text='=',padx=16,command=lambda:equal_button())
button43.grid(row=4,column=3)
button44=Button(master,text='-',padx=16,command=lambda:button_input('-'))
button44.grid(row=4,column=4)

master.mainloop()

