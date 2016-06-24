from tkinter import *
from threading import Thread


class Gui:
    active_boxes = 6
    root = Tk()
    root.title("The World's Best Grade Averager Eva!!!")

    def __init__(self):
        Label(self.root, text="Welcome to the Grade Averager").grid(row=0, columnspan=6, padx=10, pady=20)

        self.scores = [self.create_entries(row+2, 1) for row in range(self.active_boxes)]
        self.weights = [self.create_entries(row+2, 2) for row in range(self.active_boxes)]
        self.extra_credit = [self.create_check_boxes(row+2, 3) for row in range(self.active_boxes)]
        self.drop_low = [self.create_check_boxes(row+2, 4) for row in range(self.active_boxes)]

        self.reset = Button(self.root, text="Change todo", command=self.redo)
        self.reset.grid(row=self.active_boxes + 2, column=0, padx=10, pady=10)

        self.submit = Button(self.root, text="Press me!", command=Thread(target=self.submit_form).start)
        self.submit.grid(row=self.active_boxes + 2, column=1, padx=10, pady=10)

        self.status = Label(self.root, text="")
        self.status.grid(padx=10, pady=10, row=self.active_boxes + 3, columnspan=5)

        self.root.mainloop()

    def create_labels(self):
        for row in range(self.active_boxes):
            label = Label(self.root)
            label.grid(row=row, column=0)

    def create_entries(self, row, col):
        entry = Entry(self.root)
        entry.insert(END, '0')
        entry.grid(padx=10, pady=10, column=col, row=row)
        entry.bind("<Return>", Thread(target=self.submit_form).start)
        return entry

    def create_check_boxes(self, row, col):
        var = IntVar()
        check_box = Checkbutton(self.root, variable=var)
        check_box.grid(padx=10, pady=10, column=col, row=row)
        return var

    def submit_form(self, *args):
        sum = 0
        for entry in self.scores:
            sum += int(entry.get())

        update = "The total is " + str(sum)

        self.status.config(text=update)

        return

    def redo(self):
        # num = input("How many now, punk?: ")

        try:
            self.active_boxes = int(self.scores[0].get()) + 1
        except ValueError:
            self.active_boxes = 1

        for child in self.root.winfo_children():
            child.destroy()

        self.__init__()


def main():
    Gui()


if __name__ in "__main__:":
    main()