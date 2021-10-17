import tkinter
from tkinter import font
from tkinter.font import Font

root = tkinter.Tk()
root.title("Discount Caculator")
root.minsize(height=120, width=300)

# font and UI style
font1 = Font(
    family="Helveetica",
    size=20,
    weight="bold"
)

font2 = Font(
    family="Helveetica",
    size=15,
)


# Create GUI
def tab1():
    def cleartab1():
        label_intro.destroy()
        button1.destroy()
        button2.destroy()

    def tab2():
        def back():
            label_offerPrice.destroy()
            entry_offerPrice.destroy()
            label_discountPercent.destroy()
            entry_discountPercent.destroy()
            button3.destroy()
            tab1()
        cleartab1()
        label_offerPrice = tkinter.Label(
            root, text="WHAT'S THE PRICE ? :  ", font=font1)
        label_offerPrice.grid(column=0, row=0)
        entry_offerPrice = tkinter.Entry(root)
        entry_offerPrice.grid(column=1, row=0)
        label_discountPercent = tkinter.Label(
            root, text="HOW MUCH PERCENT DISCOUNT  :  ", font=font1)
        label_discountPercent.grid(column=0, row=1)
        entry_discountPercent = tkinter.Entry(root)
        entry_discountPercent.grid(column=1, row=1)
        button3 = tkinter.Button(root, text=" BACK ", command=back, font=font2)
        button3.grid(column=1, row=2, sticky=tkinter.E)

    def tab3():
        def back():
            label_finalPrice.destroy()
            entry_finalPrice.destroy()
            label_discountPercent.destroy()
            entry_discountPercent.destroy()
            button3.destroy()
            tab1()

        cleartab1()
        label_finalPrice = tkinter.Label(
            root, text="HOW MUCH DID YOU PAY ? :  ", font=font1)
        label_finalPrice.grid(column=0, row=0)
        entry_finalPrice = tkinter.Entry(root)
        entry_finalPrice.grid(column=1, row=0)
        label_discountPercent = tkinter.Label(
            root, text="WHAT'S THE DISCOUNT OFFER ? :  ", font=font1)
        label_discountPercent.grid(column=0, row=1)
        entry_discountPercent = tkinter.Entry(root)
        entry_discountPercent.grid(column=1, row=1)
        button3 = tkinter.Button(root, text=" BACK ", command=back, font=font2)
        button3.grid(column=1, row=2, sticky=tkinter.E)

    label_intro = tkinter.Label(
        root, text=" WHAT DO YOU WANT TO FIND ?", font=font1)
    label_intro.pack()
    button1 = tkinter.Button(root, text=" OFFER PRICE ",
                             command=tab2, font=font2)
    button1.pack()
    button2 = tkinter.Button(
        root, text=" ORGINAL PRICE", command=tab3, font=font2)
    button2.pack()


tab1()
root.mainloop()
