from tkinter import *
from tkinter import messagebox
from threading import Thread
import csv
import sys
# This is a comment!

line = []


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

        self.fill_text()

        self.reset = Button(self.root, text="Change todo", command=self.redo)
        self.reset.grid(row=self.active_boxes + 2, column=0, padx=10, pady=10)

        self.submit = Button(self.root, text="Press me!", command=lambda: Thread(target=self.submit_form).start())
        self.submit.grid(row=self.active_boxes + 2, column=1, padx=10, pady=10)

        self.status = Label(self.root, text="")
        self.status.grid(padx=10, pady=10, row=self.active_boxes + 3, columnspan=5)

        self.test = Button(self.root, text="Test it", command=self.add_class)
        self.test.grid()

        menu = Menu(self.root)
        self.root.config(menu=menu)

        sub_menu = Menu(menu, tearoff=False)
        menu.add_cascade(label='File', menu=sub_menu)
        subsub_menu = Menu(sub_menu, tearoff=False)
        sub_menu.add_cascade(label='Open Syllabus', menu=subsub_menu)
        sub_save_menu = Menu(sub_menu, tearoff=False)
        sub_menu.add_cascade(label='Save Syllabus', menu=sub_save_menu)
        scores_load_menu = Menu(sub_menu, tearoff=False)
        sub_menu.add_separator()
        sub_menu.add_cascade(label='Load Scores', menu=scores_load_menu)
        scores_save_menu = Menu(sub_menu, tearoff=False)
        sub_menu.add_cascade(label='Save Scores', menu=scores_save_menu)
        sub_menu.add_separator()

        sub_save_menu.add_command(label="Math er something", command=lambda: messagebox.showerror("salvado"))

        subsub_menu.add_command(label="Some command", command=lambda: messagebox.showerror("this command"))

        scores_load_menu.add_command(label="Dat class", command=lambda: messagebox.showerror("idk"))

        scores_save_menu.add_command(label="Math or something", comman=lambda: messagebox.showerror("saved by the blood of christ."))

        sub_menu.add_command(label='Quit', command=self.root.destroy)

        customize_menu = Menu(menu, tearoff=False)
        menu.add_cascade(label='Customize', menu=customize_menu)
        naming = Menu(customize_menu, tearoff=False)
        customize_menu.add_cascade(label='Rename Classes', menu=naming)
        naming.add_command(label='Rename Class 1', command=lambda: messagebox.showerror("rename that song"))

        help_menu = Menu(menu, tearoff=False)
        menu.add_cascade(label='Help', menu=help_menu)
        help_menu.add_command(label='Help', command=lambda: messagebox.showerror("You need help"))
        help_menu.add_command(label='About', command=lambda: messagebox.showerror("About that..."))

        self.root.mainloop()

    def fill_text(self):
        for row in range(self.active_boxes):
            label = Label(self.root, text="Catergory: ")
            label.grid(row=row+2, column=0, sticky=E)

    def create_entries(self, row, col):
        entry = Entry(self.root)
        entry.insert(END, '0')
        entry.grid(padx=4, pady=10, column=col, row=row)
        entry.bind("<Return>", lambda _: Thread(target=self.submit_form).start())
        return entry

    def create_check_boxes(self, row, col):
        var = IntVar()
        check_box = Checkbutton(self.root, variable=var)
        check_box.grid(padx=10, pady=10, column=col, row=row)
        return var

    def create_cascades(self):
        print("Yo")

    def submit_form(self):
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

    def add_class(self):

        def submit_info(*args):
            global line
            title.config(text="What do you want to call your next category?")
            if entry.get().title() == "None":
                writing = open("Classes.csv", 'a', newline='')
                writer = csv.writer(writing)
                writer.writerow(line)
                writing.close()
                root.destroy()
                self.status.config(text="Class created!")
                return

            line.extend((entry.get().title(), 0, 0, 0, 0))
            entry.delete(0, END)

        root = Tk()

        title = Label(root, text="What is the name of your class to be called?")
        title.pack(padx=10, pady=10)

        entry = Entry(root)
        entry.bind("<Return>", submit_info)
        entry.pack(padx=10, pady=10)

        button = Button(root, text="Submit", command=submit_info)
        button.pack()

        root.mainloop()


def main():
    Gui()


if __name__ in "__main__:":
    main()