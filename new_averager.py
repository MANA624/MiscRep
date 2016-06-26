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

    class_info = ""
    save_state = "disabled"

    def __init__(self):
        Thread(target=self.read_classes).start()

        self.root.bind("<Control-s>", self.save_scores)
        self.root.bind("<Control-a>", self.add_class)

        Label(self.root, text="Welcome to the Grade Averager").grid(row=0, columnspan=6, padx=10, pady=20)

        self.scores = [self.create_entries(row+2, 1) for row in range(self.active_boxes)]
        self.weights = [self.create_entries(row+2, 2) for row in range(self.active_boxes)]
        self.extra_credit = [self.create_check_boxes(row+2, 3) for row in range(self.active_boxes)]
        self.drop_low = [self.create_check_boxes(row+2, 4) for row in range(self.active_boxes)]

        self.fill_text()

        self.bottom_frame = Frame(self.root)
        self.bottom_frame.grid(row=self.active_boxes+2, columnspan=10)

        self.reset = Button(self.bottom_frame, text="Change todo", command=self.restart)
        self.reset.grid(row=0, column=0, padx=10, pady=10)

        self.submit = Button(self.bottom_frame, text="Press me!", command=lambda: Thread(target=self.submit_form).start())
        self.submit.grid(row=0, column=1, padx=10, pady=10)

        self.status = Label(self.bottom_frame, text="")
        self.status.grid(padx=10, pady=10, row=1, columnspan=5)

        self.test = Button(self.bottom_frame, text="Test it", command=self.add_class)
        self.test.grid(row=2, columnspan=10, padx=10, pady=10)

        self.menu = Menu(self.root)
        self.root.config(menu=self.menu)

        self.file_menu = Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label='File', menu=self.file_menu)
        self.open_syl_menu = Menu(self.file_menu, tearoff=False)
        self.file_menu.add_cascade(label='Open Syllabus', menu=self.open_syl_menu)
        self.save_syl_menu = Menu(self.file_menu, tearoff=False)
        self.file_menu.add_cascade(label='Save Syllabus', menu=self.save_syl_menu)
        self.scores_load_menu = Menu(self.file_menu, tearoff=False)
        self.file_menu.add_separator()
        self.file_menu.add_cascade(label='Load Class', menu=self.scores_load_menu)

        self.save_command = self.file_menu.add_command(label='Save Scores', accelerator="Ctr+S", state=self.save_state)
        self.file_menu.add_separator()

        self.file_menu.add_command(label='Quit', command=self.root.destroy)

        self.customize_menu = Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label='Customize', menu=self.customize_menu)
        self.naming = Menu(self.customize_menu, tearoff=False)
        self.customize_menu.add_cascade(label='Rename Class', menu=self.naming)

        self.customize_menu.add_command(label="Add Class", accelerator="Ctrl+A", command=self.add_class)
        self.delete_menu = Menu(self.customize_menu, tearoff=False)
        self.customize_menu.add_cascade(label="Delete Class", menu=self.delete_menu)

        for item in self.class_info:
            label = item[0]
            self.naming.add_command(label=item[0], command=lambda: messagebox.showerror("rename that song"))
            self.open_syl_menu.add_command(label=item[0], command=lambda: messagebox.showinfo("Yo", "Hey"))
            self.scores_load_menu.add_command(label=item[0], command=lambda label=label: self.load_class(label))
            self.save_syl_menu.add_command(label=item[0], command=lambda: messagebox.showinfo("FDSJKF", "fdsfa"))
            self.delete_menu.add_command(label=item[0], command=lambda item=item: self.delete_class(item))

        self.help_menu = Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label='Help', menu=self.help_menu)
        self.help_menu.add_command(label='Help', command=lambda: messagebox.showerror("You need help"))
        self.help_menu.add_command(label='About', command=lambda: messagebox.showerror("About that..."))

        self.root.mainloop()

    def read_classes(self):
        try:
            reading = open("Classes.csv")
            reader = csv.reader(reading)
            self.class_info = list(reader)
            reading.close()
        except FileNotFoundError:
            messagebox.showinfo("Congrats!", "Hello! And thank you for using the\nworld's best averager")

    def fill_text(self):
        for row in range(self.active_boxes):
            label = Label(self.root, text="Catergory: ")
            label.grid(row=row+2, column=0, sticky=E)

    def create_entries(self, row, col):
        entry = Entry(self.root)
        entry.insert(END, '0')
        entry.grid(padx=14, pady=10, column=col, row=row)
        entry.bind("<Return>", lambda _: Thread(target=self.submit_form).start())
        return entry

    def create_check_boxes(self, row, col):
        var = IntVar()
        check_box = Checkbutton(self.root, variable=var)
        check_box.grid(padx=10, pady=10, column=col, row=row)
        return var

    def load_class(self, class_name):
        for i in range(len(self.class_info)):
            if self.class_info[i][0] == class_name:
                self.status.config(text=class_name+" loaded!")
                index = i
                break
        try:
            self.active_boxes = int((len(self.class_info[index])-1)/5)
        except NameError:
            self.status.config(text="Class not found\nDid you corrupt the data file?")

        self.save_state = "normal"
        self.restart()

    def submit_form(self):
        sum = 0
        for entry in self.scores:
            sum += int(entry.get())

        update = "The total is " + str(sum)

        self.status.config(text=update)

        return

    def restart(self):
        self.active_boxes = 6

        for child in self.root.winfo_children():
            child.destroy()

        self.__init__()

    def save_scores(self, *args):
        if self.save_state == "disabled":
            return
        print("Saved!")

    def delete_class(self, row):
        if not messagebox.askokcancel("Careful!", "You are trying to delete " + row[0]
                                      + "\nAre you sure you want to continue?"):
            return
        self.class_info.remove(row)
        writing = open("Classes.csv", 'w', newline='')
        writer = csv.writer(writing)
        for row in self.class_info:
            writer.writerow(row)
        writing.close()
        self.active_boxes = 6
        self.save_state = "disabled"
        self.restart()

    def add_class(self, *args):

        if len(self.class_info) >= 10:
            self.status.config(text="Too many classes. Sorry!")
            return

        self.categories = 0
        self.line = []

        def submit_info(*args):
            if self.categories == 0:
                title.config(text="What do you want to call your first catergory?")
            elif self.categories == 1:
                title.config(text="What do you want to call your next category?")
            if entry.get().title() == "Quit":
                if self.categories == 1:
                    title.config(text="Oops! You need at least one class!")
                writing = open("Classes.csv", 'a', newline='')
                writer = csv.writer(writing)
                writer.writerow(self.line)
                writing.close()
                root.destroy()
                self.status.config(text="Class created!")
                self.read_classes()
                self.restart()
                return
            if self.categories == 0:
                self.line.append(entry.get().title())
            else:
                self.line.extend((entry.get().title(), 0, 0, 0, 0))
            self.categories += 1
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
