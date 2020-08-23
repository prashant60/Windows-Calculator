from tkinter import *

from main import *
root = Tk()
root.title("Calculator")
root.resizable(0,0)

variable1 = StringVar()

text1 = Entry(root, textvariable=variable1, width=55, bd=10)
text1.pack()
text1.place(height=60)

off = Button(root, text="   OFF  ", command=offf, bd=5)
off.pack()
off.place(x=254, y=170)

onn = Button(root, text="   ON   ", command=start, bd=5)
onn.pack()
onn.place(x=254, y=200)

one = Button(root, text="     1    ", command=onee, bd=5)
one.pack()
one.place(x=50, y=230)

two = Button(root, text="     2    ", command=twoo, bd=5)
two.pack()
two.place(x=100, y=230)

three = Button(root, text="     3    ", command=threee, bd=5)
three.pack()
three.place(x=150, y=230)

four = Button(root, text="     4    ", command=fourr, bd=5)
four.pack()
four.place(x=50, y=200)

five = Button(root, text="     5    ", command=fivee, bd=5)
five.pack()
five.place(x=100, y=200)

six = Button(root, text="     6    ", command=sixx, bd=5)
six.pack()
six.place(x=150, y=200)

seven = Button(root, text="     7    ", command=sevenn, bd=5)
seven.pack()
seven.place(x=50, y=170)

eight = Button(root, text="     8    ", command=eightt, bd=5)
eight.pack()
eight.place(x=100, y=170)

nine = Button(root, text="     9    ", command=ninee, bd=5)
nine.pack()
nine.place(x=150, y=170)

zero = Button(root, text="     0    ", command=zeroo, bd=5)
zero.pack()
zero.place(x=50, y=260)

zero1 = Button(root, text="    00   ", command=zeroo1, bd=5)
zero1.pack()
zero1.place(x=100, y=260)

dot = Button(root, text="     .     ", command=dott, bd=5)
dot.pack()
dot.place(x=150, y=260)

plus = Button(root, text="     +     ", command=pluss, bd=5)
plus.pack()
plus.place(x=200, y=260)

minus = Button(root, text="      -     ", command=minuss, bd=5)
minus.pack()
minus.place(x=200, y=230)

mul = Button(root, text="      x     ", command=mull, bd=5)
mul.pack()
mul.place(x=200, y=200)

div = Button(root, text="      /     ", command=divv, bd=5)
div.pack()
div.place(x=200, y=170)

equal = Button(root, text="     =    ", command=calc, bd=5, height=3)
equal.pack()
equal.place(x=255, y=230)

root.geometry("350x300+100+100")
root.mainloop()

