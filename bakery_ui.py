import tkinter
from tkinter import *


class BakeryView:
    def __init__(self, window):
        self.__init_window(window)

    def __init_window(self, window):
        window.title("빵집")
        window.geometry('400x200')
        label = Label(window, text='주문내역')
        label.pack()
        self.orderText = Text(window)
        self.orderText.pack()

    def add_order(self, orders):
        self.orderText.insert(0.0, orders + "\n")


class CustomerView:
    def __init__(self, name, window, bakery_view):
        self.name = name
        self.__init_window(window)
        self.bakeryView = bakery_view

    def __init_window(self, window):
        window.title("고객: " + self.name)
        window.geometry('350x200')
        Label(window, text="샌드위치 (5000원)").grid(column=0, row=0)
        Label(window, text="케이스 (20000원)").grid(column=0, row=1)
        self.order1 = Entry(window, width=10)
        self.order2 = Entry(window, width=10)
        self.order1.grid(column=1, row=0)
        self.order2.grid(column=1, row=1)
        btn_order = Button(window, text="주문하기", command=self.send_order)
        btn_order.grid(column=0, row=3)


    def send_order(self):
        num1 = self.order1.get()
        num2 = self.order2.get()
        if num1.isdigit() and int(num1) > 0 and num2.isdigit() and int(num2) > 0:
            order_text = "%s: 샌드위치 (5000원) %s개, 케이크 (20000원) %s개"%(self.name, self.order1.get(), self.order2.get())
            self.bakeryView.add_order(order_text)
        elif (not num2.isdigit() or int(num2) <= 0) and num1.isdigit() and int(num1) > 0:
            order_text = "%s: 샌드위치 (5000원) %s개"%(self.name, self.order1.get())
            self.bakeryView.add_order(order_text)
        elif (not num1.isdigit() or int(num1) <= 0) and num2.isdigit() and int(num2) > 0:
            order_text = "%s: 케이크 (20000원) %s개"%(self.name, self.order2.get())
            self.bakeryView.add_order(order_text)

if __name__ == '__main__':
    app = Tk()
    bakery = BakeryView(app)
    CustomerView('고객A', Toplevel(app), bakery)
    CustomerView('고객B', Toplevel(app), bakery)
    app.mainloop()
