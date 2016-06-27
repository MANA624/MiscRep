from tkinter import *
from tkinter import messagebox
from threading import Thread
import csv

# This is a comment!

line = []


class Gui:
    active_boxes = 6
    root = Tk()
    root.title("The World's Best Grade Averager Eva!!!")

    class_info = ""
    save_state = "disabled"
    categories = 0
    line = []
    class_index = -1

    def __init__(self):
        Thread(target=self.read_classes).start()

        self.root.bind("<Control-s>", self.save_scores)
        self.root.bind("<Control-a>", self.add_class)

        Label(self.root, text="Welcome to the Grade Averager").grid(row=0, columnspan=6, padx=10, pady=20)

        Label(self.root, text="Category").grid(row=1, column=0)
        Label(self.root, text="Score(s)").grid(row=1, column=1)
        Label(self.root, text="Weight (%)").grid(row=1, column=2)
        Label(self.root, text="Drop lowest grade?").grid(row=1, column=3)
        Label(self.root, text="Extra credit?").grid(row=1, column=4)

        self.scores = [self.create_entries(row+2, 1) for row in range(self.active_boxes)]
        self.weights = [self.create_entries(row+2, 2) for row in range(self.active_boxes)]
        self.drop_low = [self.create_check_boxes(row + 2, 3) for row in range(self.active_boxes)]
        self.extra_credit = [self.create_check_boxes(row+2, 4) for row in range(self.active_boxes)]

        self.fill_text()

        self.bottom_frame = Frame(self.root)
        self.bottom_frame.grid(row=self.active_boxes+2, columnspan=10)

        self.reset = Button(self.bottom_frame, text="Reset", command=self.restart)
        self.reset.grid(row=0, column=0, padx=10, pady=10)

        self.submit = Button(self.bottom_frame, text="Submit", command=lambda: Thread(target=self.submit_form).start())
        self.submit.grid(row=0, column=1, padx=10, pady=10)

        self.status = Label(self.bottom_frame)
        self.status.grid(padx=10, pady=10, row=1, columnspan=5)

        self.test = Button(self.bottom_frame, text="Test it", command=self.test)
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
            self.naming.add_command(label=item[0], command=lambda: messagebox.showerror("rename that song"))
            self.open_syl_menu.add_command(label=item[0], command=lambda: messagebox.showinfo("Yo", "Hey"))
            self.scores_load_menu.add_command(label=item[0], command=lambda label=item[0]: self.load_class(label))
            self.save_syl_menu.add_command(label=item[0], command=lambda: messagebox.showinfo("FDSJKF", "fdsfa"))
            self.delete_menu.add_command(label=item[0], command=lambda row=item: self.delete_class(item))

        self.help_menu = Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label='Help', menu=self.help_menu)
        self.help_menu.add_command(label='Help', command=lambda: messagebox.showerror("You need help"))
        self.help_menu.add_command(label='About', command=lambda: messagebox.showerror("About that..."))

        self.root.mainloop()

    def test(self):
        print("Tested")

    def read_classes(self):
        try:
            reading = open("Classes.csv")
            reader = csv.reader(reading)
            self.class_info = list(reader)
            reading.close()
        except FileNotFoundError:
            messagebox.showinfo("Congrats!", "Hello! And thank you for using the\nworld's best averager")

    def fill_text(self):
        if self.class_index == -1:
            for row in range(self.active_boxes):
                label = Label(self.root, text="Participation: ")
                label.grid(row=row+2, column=0, sticky=E, padx=10)
        else:
            for row in range(self.active_boxes):
                label = Label(self.root, text=self.class_info[self.class_index][row*5+1])
                label.grid(row=row + 2, column=0, sticky=E, padx=10)

    def create_entries(self, row, col):
        entry = Entry(self.root)
        entry.insert(END, '0')
        entry.grid(pady=10, column=col, row=row)
        entry.bind("<Return>", lambda _: Thread(target=self.submit_form).start())
        return entry

    def create_check_boxes(self, row, col):
        var = IntVar()
        check_box = Checkbutton(self.root, variable=var)
        check_box.grid(padx=10, pady=10, column=col, row=row)
        return var

    def load_class(self, class_name):
        self.active_boxes = 6
        for i in range(len(self.class_info)):
            if self.class_info[i][0] == class_name:
                self.status.config(text=class_name+" loaded!")
                self.class_index = i
                print(self.class_index)
                break
        try:
            self.active_boxes = int((len(self.class_info[self.class_index])-1)/5)
        except NameError:
            self.status.config(text="Class not found\nDid you corrupt the data file?")

        self.save_state = "normal"
        self.restart()

    def submit_form(self):

        bad = 0
        grades = []
        weights = []
        weighted_grades = []
        weight_sum = 0

        for box in range(self.active_boxes):
            grades.append(self.parse_grades(self.scores[box].get(), self.drop_low[box].get()))
            weights.append(self.parse_grades(self.weights[box].get(), False))
            weighted_grades.append(grades[box] * weights[box])
            if not self.extra_credit[box].get():
                weight_sum += weights[box]
            self.scores[box].config(bg='white')
            self.weights[box].config(bg='white')
            if isinstance(grades[box], bool):
                self.scores[box].config(bg='red')
                bad += 1
            if isinstance(weights[box], bool):
                self.weights[box].config(bg='red')
                bad += 1

        if bad:
            self.status.config(text="You had " + str(bad) + " invalid input(s)")
            return

        if not weight_sum:
            self.status.config(text="Error! All your weights were 0!")
            return

        final_grade = sum(weighted_grades) / weight_sum

        self.status.config(text="Your final grade is " + str(final_grade))

    def restart(self, *message):
        for child in self.root.winfo_children():
            child.destroy()

        self.__init__()

    def save_scores(self, *args):
        if self.save_state == "disabled":
            return
        grades = [self.parse_grades(self.scores[box].get()) for box in range(self.active_boxes)]
        weights = [self.parse_grades(self.weights[box].get()) for box in range(self.active_boxes)]
        print(grades)
        print(weights)

    def delete_class(self, row):
        if not messagebox.askokcancel("Careful!", "You are trying to delete " + row[0] +
                                      "\nAre you sure you want to continue?"):
            return

        if self.class_index != -1 and self.class_info[self.class_index] == row:
            self.active_boxes = 6
            self.class_index = -1
            self.save_state = "disabled"
        self.class_info.remove(row)
        writing = open("Classes.csv", 'w', newline='')
        writer = csv.writer(writing)
        for row in self.class_info:
            writer.writerow(row)
        writing.close()

        self.restart()

    def add_class(self, *args):

        if len(self.class_info) >= 20:
            self.status.config(text="Do you really need that many classes?")
            return

        self.categories = 0
        self.line = []

        def submit_info(*args):
            cat = entry.get().title()
            entry.delete(0, END)
            if self.categories == 0:
                title.config(text="What do you want to call your first catergory?")
            elif self.categories == 1:
                title.config(text="What do you want to call your next category?")
            if cat == "Quit":
                if self.categories <= 1:
                    title.config(text="Oops! You need at least one category!")
                    return
                writing = open("Classes.csv", 'a', newline='')
                writer = csv.writer(writing)
                writer.writerow(self.line)
                writing.close()
                root.destroy()
                self.read_classes()
                self.restart()
                return
            if not cat:
                title.config(text="You can't name it nothing!")
                return
            if len(cat) > 12:
                cat = cat[:12] + "..."
            if self.categories == 0:
                for item in self.class_info:
                    if cat == item[0]:
                        title.config(text="You already have a class with that name!")
                        return
                self.line.append(cat)
            else:
                self.line.extend((cat, 0, 0, 0, 0))
            self.categories += 1

            if self.categories >= 15:
                entry.insert(END, "Quit")
                submit_info()

        root = Tk()

        title = Label(root, text="What is the name of your class to be called?")
        title.pack(padx=10, pady=10)

        Label(root, text='Type "Quit" when done').pack(padx=10, pady=5)

        entry = Entry(root)
        entry.bind("<Return>", submit_info)
        entry.pack(padx=10, pady=10)

        button = Button(root, text="Submit", command=submit_info)
        button.pack()

        root.mainloop()

    def parse_grades(self, grades, drop):
        scores = grades.split(',')

        try:
            for num in range(len(scores)):
                scores[num] = float(scores[num])

        except ValueError:
            self.status.config(text="Invalid input!")
            return False

        if drop and len(scores) > 1:
            scores.sort()
            scores = scores[1:]

        avg = sum(scores) / len(scores)

        return avg


def main():
    Gui()


if __name__ in "__main__:":
    main()
