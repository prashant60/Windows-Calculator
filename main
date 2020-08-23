import gui
import operator

def offf():
    gui.text1.delete(0, 'end')
    globals()['abc'] = None
    globals()['abcd'] = None
    globals()['num1']=None
    globals()['op'] = None

def start():
    gui.variable1.set("00")
    globals()['abc'] = "0"
    globals()['abcd'] = "0"
    globals()['num1']=None
    globals()['op'] = None

def onee():
    if globals()['abc'] == "0" or globals()['abcd'] == "0":
        gui.variable1.set("1")
        globals()['abc'] = "1"
        globals()['abcd'] = "1"

    elif globals()['abc'] == "1" and globals()['abcd'] == "1":
        textt = gui.text1.get()
        gui.variable1.set(textt + "1")

def twoo():
    if globals()['abc'] == "0" or globals()['abcd'] == "0":
        gui.variable1.set("2")
        globals()['abc'] = "1"
        globals()['abcd'] = "1"

    elif globals()['abc'] == "1" and globals()['abcd'] == "1":
        textt = gui.text1.get()
        gui.variable1.set(textt + "2")

def threee():
    if globals()['abc'] == "0" or globals()['abcd'] == "0":
        gui.variable1.set("3")
        globals()['abc'] = "1"
        globals()['abcd'] = "1"

    elif globals()['abc'] == "1" and globals()['abcd'] == "1":
        textt = gui.text1.get()
        gui.variable1.set(textt + "3")

def fourr():
    if globals()['abc'] == "0" or globals()['abcd'] == "0":
        gui.variable1.set("4")
        globals()['abc'] = "1"
        globals()['abcd'] = "1"

    elif globals()['abc'] == "1" and globals()['abcd'] == "1":
        textt = gui.text1.get()
        gui.variable1.set(textt + "4")

def fivee():
    if globals()['abc'] == "0" or globals()['abcd'] == "0":
        gui.variable1.set("5")
        globals()['abc'] = "1"
        globals()['abcd'] = "1"

    elif globals()['abc'] == "1" and globals()['abcd'] == "1":
        textt = gui.text1.get()
        gui.variable1.set(textt + "5")

def sixx():
    if globals()['abc'] == "0" or globals()['abcd'] == "0":
        gui.variable1.set("6")
        globals()['abc'] = "1"
        globals()['abcd'] = "1"

    elif globals()['abc'] == "1" and globals()['abcd'] == "1":
        textt = gui.text1.get()
        gui.variable1.set(textt + "6")

def sevenn():
    if globals()['abc'] == "0" or globals()['abcd'] == "0":
        gui.variable1.set("7")
        globals()['abc'] = "1"
        globals()['abcd'] = "1"

    elif globals()['abc'] == "1" and globals()['abcd'] == "1":
        textt = gui.text1.get()
        gui.variable1.set(textt + "7")

def eightt():
    if globals()['abc'] == "0" or globals()['abcd'] == "0":
        gui.variable1.set("8")
        globals()['abc'] = "1"
        globals()['abcd'] = "1"

    elif globals()['abc'] == "1" and globals()['abcd'] == "1":
        textt = gui.text1.get()
        gui.variable1.set(textt + "8")

def ninee():
    if globals()['abc'] == "0" or globals()['abcd'] == "0":
        gui.variable1.set("9")
        globals()['abc'] = "1"
        globals()['abcd'] = "1"

    elif globals()['abc'] == "1" and globals()['abcd'] == "1":
        textt = gui.text1.get()
        gui.variable1.set(textt + "9")
def zeroo():
    if globals()['abc'] == "0" or globals()['abcd'] == "0":
        gui.variable1.set("0")
        globals()['abc'] = "1"
        globals()['abcd'] = "1"

    elif globals()['abc'] == "1" and globals()['abcd'] == "1":
        textt = gui.text1.get()
        gui.variable1.set(textt + "0")

def zeroo1():
    if globals()['abc'] == "0" or globals()['abcd'] == "0":
        gui.variable1.set("00")
        globals()['abc'] = "1"
        globals()['abcd'] = "1"

    elif globals()['abc'] == "1" and globals()['abcd'] == "1":
        textt = gui.text1.get()
        gui.variable1.set(textt + "00")

def dott():
    if globals()['abc'] == "0" or globals()['abcd'] == "0":
        gui.variable1.set("0.")
        globals()['abc'] = "1"
        globals()['abcd'] = "1"

    elif globals()['abc'] == "1" and globals()['abcd'] == "1":
        textt = gui.text1.get()
        gui.variable1.set(textt + ".")

def pluss():
    if globals()['abc'] == "1":

        if globals()['op'] == None:
            globals()['num1'] = float(gui.text1.get())

        else:
            if not gui.text1.get():
                pass
            else:
                globals()['num1'] = globals()['op'](globals()['num1'], float(gui.text1.get()))

        globals()['op'] = operator.add
        gui.text1.delete(0, 'end')

def minuss():
    if globals()['abc'] == "1":

        if globals()['op'] == None:
            globals()['num1'] = float(gui.text1.get())

        else:
            if not gui.text1.get():
                pass
            else:
                globals()['num1'] = globals()['op'](globals()['num1'], float(gui.text1.get()))

        globals()['op'] = operator.sub
        gui.text1.delete(0, 'end')

def mull():
    if globals()['abc'] == "1":

        if globals()['op'] == None:
            globals()['num1'] = float(gui.text1.get())

        else:
            if not gui.text1.get():
                pass
            else:
                globals()['num1'] = globals()['op'](globals()['num1'], float(gui.text1.get()))

        globals()['op'] = operator.mul
        gui.text1.delete(0, 'end')

def divv():
    if globals()['abc'] == "1":

        if globals()['op'] == None:
            globals()['num1'] = float(gui.text1.get())

        else:
            if not gui.text1.get():
                pass
            else:
                globals()['num1'] = globals()['op'](globals()['num1'], float(gui.text1.get()))

        globals()['op'] = operator.truediv
        gui.text1.delete(0, 'end')

def calc():
    if globals()['abc'] == "1":
        if globals()['op'] == None:
            globals()['num1'] = float(gui.text1.get())

        else:
            if not gui.text1.get():
                pass
            else:
                globals()['num1'] = globals()['op'](globals()['num1'], float(gui.text1.get()))

        final = globals()['num1']
        gui.variable1.set(final)
        globals()['abcd'] = "0"
        globals()['op'] = None
