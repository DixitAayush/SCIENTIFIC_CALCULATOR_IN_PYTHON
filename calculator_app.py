import tkinter as tk
import math

window=tk.Tk()
window.configure(bg="black")

first_number = None
operation = None
window.title("my scitific calculator")
display = tk.Entry(
    window,
    width=20,
    font=("Arial", 20),
    justify="right",
    bg="white",
    fg="black"
)

display.grid(row=0,column=0,columnspan=5)
def button1o():
    display.insert("end", "1")
button1 =tk.Button(window,text="1", command=button1o,width=5,height=2,padx=5,pady=5,bg="yellow",fg="black")
button1.grid(row=1,column=0)
def button2o():
    display.insert("end" , "2")
button2 = tk.Button(window,text ="2", command=button2o,width=5,height=2,padx=5,pady=5,bg="yellow",fg="black")
button2.grid(row=1,column=1)
def buttonclearo():
    display.delete(0,"end")
buttonclear =tk.Button(window,text="c",command=buttonclearo,width=5,height=2,padx=5,pady=5,bg="yellow",fg="black")
buttonclear.grid(row=1,column=3)
def button3o():
    display.insert("end", "3")
button3 =tk.Button(window,text="3", command=button3o,width=5,height=2,padx=5,pady=5,bg="yellow",fg="black")
button3.grid(row=1,column=2)
def button4o():
    display.insert("end", "4")
button4 =tk.Button(window,text="4", command=button4o,width=5,height=2,padx=5,pady=5,bg="yellow",fg="black")
button4.grid(row=2,column=0)
def button5o():
    display.insert("end", "5")
button5 =tk.Button(window,text="5", command=button5o,width=5,height=2,padx=5,pady=5,bg="yellow",fg="black")
button5.grid(row=2,column=1)
def button6o():
    display.insert("end", "6")
button6 =tk.Button(window,text="6", command=button6o,width=5,height=2,padx=5,pady=5,bg="yellow",fg="black")
button6.grid(row=2,column=2)
def button7o():
    display.insert("end", "7")
button7 =tk.Button(window,text="7", command=button7o,width=5,height=2,padx=5,pady=5,bg="yellow",fg="black")
button7.grid(row=3,column=0)
def button8o():
    display.insert("end", "8")
button8 =tk.Button(window,text="8", command=button8o,width=5,height=2,padx=5,pady=5,bg="yellow",fg="black")
button8.grid(row=3,column=1)
def button9o():
    display.insert("end", "9")
button9 =tk.Button(window,text="9", command=button9o,width=5,height=2,padx=5,pady=5,bg="yellow",fg="black")
button9.grid(row=3,column=2)
def button0o():
    display.insert("end", "0")
button0 =tk.Button(window,text="0", command=button0o,width=5,height=2,padx=5,pady=5,bg="yellow",fg="black")
button0.grid(row=4,column=1)
def buttondoto():
    display.insert("end", '.')
buttondot =tk.Button(window,text=".", command=buttondoto,width=5,height=2,padx=5,pady=5,bg="yellow",fg="black")
buttondot.grid(row=4,column=0)
def buttonaddo():
    display.insert("end", '+')
buttonadd =tk.Button(window,text="+", command=buttonaddo,width=5,height=2,padx=5,pady=5,bg="yellow",fg="black")
buttonadd.grid(row=1,column=4)
def buttonsubo():
    display.insert("end", '-')
buttonsub =tk.Button(window,text="-", command=buttonsubo,width=5,height=2,padx=5,pady=5,bg="yellow",fg="black")
buttonsub.grid(row=2,column=3)
def buttonmulo():
    display.insert("end", '*')
buttonmul =tk.Button(window,text="*", command=buttonmulo,width=5,height=2,padx=5,pady=5,bg="yellow",fg="black")
buttonmul.grid(row=2,column=4)
def buttondivo():
    display.insert("end", '/')
buttondiv =tk.Button(window,text="/", command=buttondivo,width=5,height=2,padx=5,pady=5,bg="yellow",fg="black")
buttondiv.grid(row=3,column=3)
def buttonlogo():
    number2 = float(display.get())
    if number2 >0:
        answer2 = math.log(number2)
        display.delete(0,"end")
        display.insert("end",answer2)
    elif number2<=0:
        display.delete(0,"end")
        display.insert("end","invalid")


buttonlog =tk.Button(window,text="log", command=buttonlogo,width=5,height=2,padx=5,pady=5,bg="yellow",fg="black")
buttonlog.grid(row=3,column=4)
def buttonpowo():
    display.insert("end", '**')
buttonpow =tk.Button(window,text="^", command=buttonpowo,width=5,height=2,padx=5,pady=5,bg="yellow",fg="black")
buttonpow.grid(row=4,column=3)
def buttonrooto():
    
    number = float(display.get())
    if number >=0:
        answer1 = math.sqrt(number)
        display.delete(0,"end")
        display.insert("end",answer1)
    else :
        display.delete(0,"end")
        display.insert("end", "invalid")
            


buttonroot =tk.Button(window,text='underroot', command=buttonrooto,width=5,height=2,padx=5,pady=5,bg="yellow",fg="black")
buttonroot.grid(row=4,column=4)
def buttonEQo():
    Expression = display.get()
    answer = eval(Expression)
    display.delete(0,"end")
    display.insert("end",answer)
buttonEQ =tk.Button(window,text='=', command=buttonEQo,width=5,height=2,padx=5,pady=5,bg="yellow",fg="black")
buttonEQ.grid(row=4,column=2)


window.mainloop()




