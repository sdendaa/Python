from tkinter import *


def i_calc(source, side):
    store_obj = Frame(source, borderwidth=1, bd=6, bg='powder blue')
    store_obj.pack(side=side, expand=YES, fill=BOTH)
    return store_obj


def button(source, side, text, command=None):
    store_obj = Button(source, text=text, command=command)
    store_obj.pack(side=side, expand=YES, fill=BOTH)
    return store_obj


class MyApp(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font', 'arial 20 bold')
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Calculator')

        display = StringVar()
        Entry(self, relief=RIDGE, textvariable=display,
              justify='right', bd=30, bg='powder blue').pack(side=TOP,
                                                             expand=YES, fill=BOTH)
        for clearBut in (["CE"], ["C"]):
            erase = i_calc(self, TOP)
            for iEquals in clearBut:
                button(erase, LEFT, iEquals,
                       lambda store_obj=display, q=iEquals: store_obj.set(''))

        for numBut in ("789/", "456*", "123-", "0.+"):
            function_num = i_calc(self, TOP)
            for iEquals in numBut:
                button(function_num, LEFT, iEquals,
                       lambda store_obj=display, q=iEquals: store_obj.set(store_obj.get()+q))

        equal_button = i_calc(self, TOP)
        for iEquals in "=":
            if iEquals == '=':
                equals = button(equal_button, LEFT, iEquals)
                equals.bind('<ButtonRelease-1>',
                            lambda e, s=self, store_obj=display: s.calc(store_obj), '+')
            else:
                button(equal_button, LEFT, iEquals,
                       lambda store_obj=display, s='%s' % iEquals: store_obj.set(store_obj.get()+s))

    def calc(self, display):
        try:
            display.set(eval(display.get()))
        except:
            display.set("ERROR")

if __name__ == '__main__':
    MyApp().mainloop()
