# Import TKinter
from tkinter import *
import tkinter.messagebox
from tkinter.filedialog import askopenfilename
import os
import shutil

# These are some variables used to determine if a window has been opened yet
root = Tk()

# I'm gonna write some code that involves checking for a text file, and reading a text file and saving the result
# as a global variable. The purpose of this is so that the user can rename their classes. Here goes
def check_names():
    global class1, class2, class3, class4, class5, class6, class7
    try:
        math_text = open('math.txt', 'r')
        class1 = math_text.read()
        math_text.close()
    except:
        class1 = 'Math'

    try:
        comp_text = open('comp.txt', 'r')
        class2 = comp_text.read()
        comp_text.close()
    except:
        class2 = 'Comp. Sci.'

    try:
        phys_text = open('phys.txt', 'r')
        class3 = phys_text.read()
        phys_text.close()
    except:
        class3 = 'Physics'

    try:
        span_text = open('span.txt', 'r')
        class4 = span_text.read()
        span_text.close()
    except:
        class4 = 'Spanish'

    try:
        engl_text = open('engl.txt', 'r')
        class5 = engl_text.read()
        engl_text.close()
    except:
        class5 = 'English'

    try:
        hist_text = open('hist.txt', 'r')
        class6 = hist_text.read()
        hist_text.close()
    except:
        class6 = 'History'

    try:
        chem_text = open('chem.txt', 'r')
        class7 = chem_text.read()
        chem_text.close()
    except:
        class7 = 'Chemistry'


check_names()


# This is the function to open the scores for a class. active.txt gets changed to all 0's every time the window
# closes, but the user can choose to open a class, which sets active.txt to the value of the scores saved in the
# class chosen
def load_scores():
    global scores1
    try:
        score_reader = open('active.txt', 'r')
        scores1 = score_reader.read()
        score_reader.close()

        scores1 = scores1.split('\n')
    except:
        scores1 = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]

load_scores()


# This function saves the scores of the first class by retrieving all the values of the boxes and saving them in
# a scores1.txt text file
def save_scores1():
    scores1 = str(test.prompt_Box_1_1.get()) + '\n' \
              + str(test.prompt_Box_1_2.get()) + '\n' + \
              str(test.prompt_Box_2_1.get()) + '\n' + \
              str(test.prompt_Box_2_2.get()) + '\n' + \
              str(test.prompt_Box_3_1.get()) + '\n' + \
              str(test.prompt_Box_3_2.get()) + '\n' + \
              str(test.prompt_Box_4_1.get()) + '\n' + \
              str(test.prompt_Box_4_2.get()) + '\n' + \
              str(test.prompt_Box_5_1.get()) + '\n' + \
              str(test.prompt_Box_5_2.get()) + '\n' + \
              str(test.prompt_Box_6_1.get()) + '\n' + \
              str(test.prompt_Box_6_2.get()) + '\n' + \
              str(test.prompt_Box_7_1.get()) + '\n' + \
              str(test.prompt_Box_7_2.get()) + '\n' + \
              str(test.prompt_Box_8_1.get()) + '\n' + \
              str(test.prompt_Box_8_2.get()) + '\n'
    score_writer = open('scores1.txt', 'w')
    score_writer.write(scores1)
    score_writer.close()


def open_scores1():
    global test, root
    try:
        temp_reader = open('scores1.txt', 'r')
        temp = temp_reader.read()
        temp_reader.close()

        active_writer = open('active.txt', 'w')
        active_writer.write(temp)
        active_writer.close()

        load_scores()

        dims = [root.winfo_x(), root.winfo_y(), root.winfo_height(), root.winfo_width()]
        test.master.destroy()
        root = Tk()
        root.geometry('%dx%d+%d+%d' % (dims[3], dims[2], dims[0], dims[1]))
        test = AverageClass(root)
        root.iconbitmap('favicon.ico')
    except:
        tkinter.messagebox.showinfo('Problem Loading Scores', "Scores for this class could not be found. Try saving some first")


# This function saves the scores of the first class by retrieving all the values of the boxes and saving them in
# a scores2.txt text file
def save_scores2():
    scores1 = str(test.prompt_Box_1_1.get()) + '\n' \
              + str(test.prompt_Box_1_2.get()) + '\n' + \
              str(test.prompt_Box_2_1.get()) + '\n' + \
              str(test.prompt_Box_2_2.get()) + '\n' + \
              str(test.prompt_Box_3_1.get()) + '\n' + \
              str(test.prompt_Box_3_2.get()) + '\n' + \
              str(test.prompt_Box_4_1.get()) + '\n' + \
              str(test.prompt_Box_4_2.get()) + '\n' + \
              str(test.prompt_Box_5_1.get()) + '\n' + \
              str(test.prompt_Box_5_2.get()) + '\n' + \
              str(test.prompt_Box_6_1.get()) + '\n' + \
              str(test.prompt_Box_6_2.get()) + '\n' + \
              str(test.prompt_Box_7_1.get()) + '\n' + \
              str(test.prompt_Box_7_2.get()) + '\n' + \
              str(test.prompt_Box_8_1.get()) + '\n' + \
              str(test.prompt_Box_8_2.get()) + '\n'
    score_writer = open('scores2.txt', 'w')
    score_writer.write(scores1)
    score_writer.close()


def open_scores2():
    try:
        global test, root
        temp_reader = open('scores2.txt', 'r')
        temp = temp_reader.read()
        temp_reader.close()

        active_writer = open('active.txt', 'w')
        active_writer.write(temp)
        active_writer.close()

        load_scores()

        dims = [root.winfo_x(), root.winfo_y(), root.winfo_height(), root.winfo_width()]
        test.master.destroy()
        root = Tk()
        root.geometry('%dx%d+%d+%d' % (dims[3], dims[2], dims[0], dims[1]))
        test = AverageClass(root)
        root.iconbitmap('favicon.ico')

    except:
        tkinter.messagebox.showinfo('Problem Loading Scores', "Scores for this class could not be found. Try saving some first")


# This function saves the scores of the first class by retrieving all the values of the boxes and saving them in
# a scores3.txt text file
def save_scores3():
    scores1 = str(test.prompt_Box_1_1.get()) + '\n' \
              + str(test.prompt_Box_1_2.get()) + '\n' + \
              str(test.prompt_Box_2_1.get()) + '\n' + \
              str(test.prompt_Box_2_2.get()) + '\n' + \
              str(test.prompt_Box_3_1.get()) + '\n' + \
              str(test.prompt_Box_3_2.get()) + '\n' + \
              str(test.prompt_Box_4_1.get()) + '\n' + \
              str(test.prompt_Box_4_2.get()) + '\n' + \
              str(test.prompt_Box_5_1.get()) + '\n' + \
              str(test.prompt_Box_5_2.get()) + '\n' + \
              str(test.prompt_Box_6_1.get()) + '\n' + \
              str(test.prompt_Box_6_2.get()) + '\n' + \
              str(test.prompt_Box_7_1.get()) + '\n' + \
              str(test.prompt_Box_7_2.get()) + '\n' + \
              str(test.prompt_Box_8_1.get()) + '\n' + \
              str(test.prompt_Box_8_2.get()) + '\n'
    score_writer = open('scores3.txt', 'w')
    score_writer.write(scores1)
    score_writer.close()


def open_scores3():
    try:
        global test, root
        temp_reader = open('scores3.txt', 'r')
        temp = temp_reader.read()
        temp_reader.close()

        active_writer = open('active.txt', 'w')
        active_writer.write(temp)
        active_writer.close()

        load_scores()

        dims = [root.winfo_x(), root.winfo_y(), root.winfo_height(), root.winfo_width()]
        test.master.destroy()
        root = Tk()
        root.geometry('%dx%d+%d+%d' % (dims[3], dims[2], dims[0], dims[1]))
        test = AverageClass(root)
        root.iconbitmap('favicon.ico')

    except:
        tkinter.messagebox.showinfo('Problem Loading Scores', "Scores for this class could not be found. Try saving some first")


# This function saves the scores of the fourth class by retrieving all the values of the boxes and saving them in
# a scores4.txt text file
def save_scores4():
    scores1 = str(test.prompt_Box_1_1.get()) + '\n' \
              + str(test.prompt_Box_1_2.get()) + '\n' + \
              str(test.prompt_Box_2_1.get()) + '\n' + \
              str(test.prompt_Box_2_2.get()) + '\n' + \
              str(test.prompt_Box_3_1.get()) + '\n' + \
              str(test.prompt_Box_3_2.get()) + '\n' + \
              str(test.prompt_Box_4_1.get()) + '\n' + \
              str(test.prompt_Box_4_2.get()) + '\n' + \
              str(test.prompt_Box_5_1.get()) + '\n' + \
              str(test.prompt_Box_5_2.get()) + '\n' + \
              str(test.prompt_Box_6_1.get()) + '\n' + \
              str(test.prompt_Box_6_2.get()) + '\n' + \
              str(test.prompt_Box_7_1.get()) + '\n' + \
              str(test.prompt_Box_7_2.get()) + '\n' + \
              str(test.prompt_Box_8_1.get()) + '\n' + \
              str(test.prompt_Box_8_2.get()) + '\n'
    score_writer = open('scores4.txt', 'w')
    score_writer.write(scores1)
    score_writer.close()


def open_scores4():
    try:
        global test, root
        temp_reader = open('scores4.txt', 'r')
        temp = temp_reader.read()
        temp_reader.close()

        active_writer = open('active.txt', 'w')
        active_writer.write(temp)
        active_writer.close()

        load_scores()

        dims = [root.winfo_x(), root.winfo_y(), root.winfo_height(), root.winfo_width()]
        test.master.destroy()
        root = Tk()
        root.geometry('%dx%d+%d+%d' % (dims[3], dims[2], dims[0], dims[1]))
        test = AverageClass(root)
        root.iconbitmap('favicon.ico')

    except:
        tkinter.messagebox.showinfo('Problem Loading Scores', "Scores for this class could not be found. Try saving some first")

def save_scores5():
    scores1 = str(test.prompt_Box_1_1.get()) + '\n' \
              + str(test.prompt_Box_1_2.get()) + '\n' + \
              str(test.prompt_Box_2_1.get()) + '\n' + \
              str(test.prompt_Box_2_2.get()) + '\n' + \
              str(test.prompt_Box_3_1.get()) + '\n' + \
              str(test.prompt_Box_3_2.get()) + '\n' + \
              str(test.prompt_Box_4_1.get()) + '\n' + \
              str(test.prompt_Box_4_2.get()) + '\n' + \
              str(test.prompt_Box_5_1.get()) + '\n' + \
              str(test.prompt_Box_5_2.get()) + '\n' + \
              str(test.prompt_Box_6_1.get()) + '\n' + \
              str(test.prompt_Box_6_2.get()) + '\n' + \
              str(test.prompt_Box_7_1.get()) + '\n' + \
              str(test.prompt_Box_7_2.get()) + '\n' + \
              str(test.prompt_Box_8_1.get()) + '\n' + \
              str(test.prompt_Box_8_2.get()) + '\n'
    score_writer = open('scores5.txt', 'w')
    score_writer.write(scores1)
    score_writer.close()


def open_scores5():
    try:
        global test, root
        temp_reader = open('scores5.txt', 'r')
        temp = temp_reader.read()
        temp_reader.close()

        active_writer = open('active.txt', 'w')
        active_writer.write(temp)
        active_writer.close()

        load_scores()

        dims = [root.winfo_x(), root.winfo_y(), root.winfo_height(), root.winfo_width()]
        test.master.destroy()
        root = Tk()
        root.geometry('%dx%d+%d+%d' % (dims[3], dims[2], dims[0], dims[1]))
        test = AverageClass(root)
        root.iconbitmap('favicon.ico')

    except:
        tkinter.messagebox.showinfo('Problem Loading Scores', "Scores for this class could not be found. Try saving some first")

def save_scores6():
    scores1 = str(test.prompt_Box_1_1.get()) + '\n' \
              + str(test.prompt_Box_1_2.get()) + '\n' + \
              str(test.prompt_Box_2_1.get()) + '\n' + \
              str(test.prompt_Box_2_2.get()) + '\n' + \
              str(test.prompt_Box_3_1.get()) + '\n' + \
              str(test.prompt_Box_3_2.get()) + '\n' + \
              str(test.prompt_Box_4_1.get()) + '\n' + \
              str(test.prompt_Box_4_2.get()) + '\n' + \
              str(test.prompt_Box_5_1.get()) + '\n' + \
              str(test.prompt_Box_5_2.get()) + '\n' + \
              str(test.prompt_Box_6_1.get()) + '\n' + \
              str(test.prompt_Box_6_2.get()) + '\n' + \
              str(test.prompt_Box_7_1.get()) + '\n' + \
              str(test.prompt_Box_7_2.get()) + '\n' + \
              str(test.prompt_Box_8_1.get()) + '\n' + \
              str(test.prompt_Box_8_2.get()) + '\n'
    score_writer = open('scores6.txt', 'w')
    score_writer.write(scores1)
    score_writer.close()


def open_scores6():
    try:
        global test, root
        temp_reader = open('scores6.txt', 'r')
        temp = temp_reader.read()
        temp_reader.close()

        active_writer = open('active.txt', 'w')
        active_writer.write(temp)
        active_writer.close()

        load_scores()

        dims = [root.winfo_x(), root.winfo_y(), root.winfo_height(), root.winfo_width()]
        test.master.destroy()
        root = Tk()
        root.geometry('%dx%d+%d+%d' % (dims[3], dims[2], dims[0], dims[1]))
        test = AverageClass(root)
        root.iconbitmap('favicon.ico')

    except:
        tkinter.messagebox.showinfo('Problem Loading Scores', "Scores for this class could not be found. Try saving some first")

def save_scores7():
    scores1 = str(test.prompt_Box_1_1.get()) + '\n' \
              + str(test.prompt_Box_1_2.get()) + '\n' + \
              str(test.prompt_Box_2_1.get()) + '\n' + \
              str(test.prompt_Box_2_2.get()) + '\n' + \
              str(test.prompt_Box_3_1.get()) + '\n' + \
              str(test.prompt_Box_3_2.get()) + '\n' + \
              str(test.prompt_Box_4_1.get()) + '\n' + \
              str(test.prompt_Box_4_2.get()) + '\n' + \
              str(test.prompt_Box_5_1.get()) + '\n' + \
              str(test.prompt_Box_5_2.get()) + '\n' + \
              str(test.prompt_Box_6_1.get()) + '\n' + \
              str(test.prompt_Box_6_2.get()) + '\n' + \
              str(test.prompt_Box_7_1.get()) + '\n' + \
              str(test.prompt_Box_7_2.get()) + '\n' + \
              str(test.prompt_Box_8_1.get()) + '\n' + \
              str(test.prompt_Box_8_2.get()) + '\n'
    score_writer = open('scores7.txt', 'w')
    score_writer.write(scores1)
    score_writer.close()


def open_scores7():
    try:
        global test, root
        temp_reader = open('scores7.txt', 'r')
        temp = temp_reader.read()
        temp_reader.close()

        active_writer = open('active.txt', 'w')
        active_writer.write(temp)
        active_writer.close()

        load_scores()

        dims = [root.winfo_x(), root.winfo_y(), root.winfo_height(), root.winfo_width()]
        test.master.destroy()
        root = Tk()
        root.geometry('%dx%d+%d+%d' % (dims[3], dims[2], dims[0], dims[1]))
        test = AverageClass(root)
        root.iconbitmap('favicon.ico')

    except:
        tkinter.messagebox.showinfo('Problem Loading Scores', "Scores for this class could not be found. Try saving some first")


def reset_scores():
    global test, root
    score_writer = open('active.txt', 'w')
    score_writer.write('0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0')
    score_writer.close()

    load_scores()

    dims = [root.winfo_x(), root.winfo_y(), root.winfo_height(), root.winfo_width()]
    test.master.destroy()
    root = Tk()
    root.geometry('%dx%d+%d+%d' % (dims[3], dims[2], dims[0], dims[1]))
    test = AverageClass(root)
    root.iconbitmap('favicon.ico')


# These are the functions that open the syllabi for your courses feel free to rename them, but hopefully
# I'll make it so that's not necessary!
def open_math():
    try:
        os.startfile('math_syl.pdf')
    except:
        tkinter.messagebox.showinfo('Error opening file', 'No such file was found. Try saving your syllabus first')


def open_comp():
    try:
        os.startfile('comp_syl.pdf')
    except:
        tkinter.messagebox.showinfo('Error opening file', 'No such file was found. Try saving your syllabus first')


def open_phys():
    try:
        os.startfile('phys_syl.pdf')
    except:
        tkinter.messagebox.showinfo('Error opening file', 'No such file was found. Try saving your syllabus first')


def open_span():
    try:
        os.startfile('span_syl.pdf')
    except:
        tkinter.messagebox.showinfo('Error opening file', 'No such file was found. Try saving your syllabus first')


def open_engl():
    try:
        os.startfile('engl_syl.pdf')
    except:
        tkinter.messagebox.showinfo('Error opening file', 'No such file was found. Try saving your syllabus first')

def open_hist():
    try:
        os.startfile('hist_syl.pdf')
    except:
        tkinter.messagebox.showinfo('Error opening file', 'No such file was found. Try saving your syllabus first')

def open_chem():
    try:
        os.startfile('chem_syl.pdf')
    except:
        tkinter.messagebox.showinfo('Error opening file', 'No such file was found. Try saving your syllabus first')


# This function is the class that runs all the main frame repeatedly
class AverageClass:
    def __init__(self, master):
        global scores1

        # I am giving the thing a title
        self.master = master
        self.master.title("Hand Caclulations Are So Last Century!")

        self.master.maxsize(width=604, height=474)

        self.frame = Frame(master)
        self.frame.pack(fill=BOTH)

        # Some things that were farther down, but I needed to be behind the background image
        imag_label = Label(self.frame, text="")
        imag_label.grid(row=11, column=0, columnspan=4, padx=275)

        top_space = Label(self.frame, text='\n')
        top_space.grid(row=0, column=0, columnspan=5)

        bottom_space = Label(self.frame, text='\n')
        bottom_space.grid(row=2, column=0)

        # This is the code for the background image
        self.photo = PhotoImage(file="bg_img.png")

        self.img_label = Label(self.frame, image=self.photo)
        self.img_label.grid(row=0, column=0, rowspan=13, columnspan=5)

        # This is the label at the top
        self.greet_label = Label(self.frame, text="  Welcome to the Average Grade Calculator!  ", bd=15, highlightcolor="black")
        self.greet_label.grid(row=1, column=0, columnspan=4)

        # T hese are the top row of words of how to place the numbers
        guide_label_1 = Label(self.frame, text="Catergory", bd=2)
        guide_label_1.grid(row=3, column=0, sticky=E)

        guide_label_2 = Label(self.frame, text="Percentage", bd=2)
        guide_label_2.grid(row=3, column=1)

        guide_label_2 = Label(self.frame, text="Weight (%)", bd=2)
        guide_label_2.grid(row=3, column=2)

        # This is the first row with entries
        # The label for the first row
        side_label_1 = Label(self.frame, text="Written Homework:")
        side_label_1.grid(row=4, column=0, sticky=E)

        # The input for the grades for the first row
        self.prompt_Box_1_1 = Entry(self.frame, bd=2)
        self.prompt_Box_1_1.grid(row=4, column=1)
        self.prompt_Box_1_1.insert(0, scores1[0])
        self.prompt_Box_1_1.bind("<Return>", self.retrieve_input)
        self.color = self.prompt_Box_1_1.cget('bg')

        # The input for the weight for the first row
        self.prompt_Box_1_2 = Entry(self.frame, bd=2)
        self.prompt_Box_1_2.grid(row=4, column=2)
        self.prompt_Box_1_2.insert(0, scores1[1])
        self.prompt_Box_1_2.bind("<Return>", self.retrieve_input)

        self.var1 = IntVar()
        c1 = Checkbutton(self.frame, text="Drop lowest grade:", variable=self.var1)
        c1.grid(row=4, column=3, sticky=W)

        # This is the second row with entries
        side_label_2 = Label(self.frame, text="Online Homework:")
        side_label_2.grid(row=5, column=0, sticky=E)

        self.prompt_Box_2_1 = Entry(self.frame, bd=2)
        self.prompt_Box_2_1.grid(row=5, column=1)
        self.prompt_Box_2_1.insert(0, scores1[2])
        self.prompt_Box_2_1.bind("<Return>", self.retrieve_input)

        self.prompt_Box_2_2 = Entry(self.frame, bd=2)
        self.prompt_Box_2_2.grid(row=5, column=2)
        self.prompt_Box_2_2.insert(0, scores1[3])
        self.prompt_Box_2_2.bind("<Return>", self.retrieve_input)

        self.var2 = IntVar()
        c1 = Checkbutton(self.frame, text="Drop lowest grade:", variable=self.var2)
        c1.grid(row=5, column=3, sticky=W)

        # The third row with entries
        side_label_3 = Label(self.frame, text="Quizzes:")
        side_label_3.grid(row=6, column=0, sticky=E)

        self.prompt_Box_3_1 = Entry(self.frame, bd=2)
        self.prompt_Box_3_1.grid(row=6, column=1)
        self.prompt_Box_3_1.insert(0, scores1[4])
        self.prompt_Box_3_1.bind("<Return>", self.retrieve_input)

        self.prompt_Box_3_2 = Entry(self.frame, bd=2)
        self.prompt_Box_3_2.grid(row=6, column=2)
        self.prompt_Box_3_2.insert(0, scores1[5])
        self.prompt_Box_3_2.bind("<Return>", self.retrieve_input)

        self.var3 = IntVar()
        c1 = Checkbutton(self.frame, text="Drop lowest grade:", variable=self.var3)
        c1.grid(row=6, column=3, sticky=W)

        # The fourth row with entries
        side_label_4 = Label(self.frame, text="Test 1:")
        side_label_4.grid(row=7, column=0, sticky=E)

        self.prompt_Box_4_1 = Entry(self.frame, bd=2)
        self.prompt_Box_4_1.grid(row=7, column=1)
        self.prompt_Box_4_1.insert(0, scores1[6])
        self.prompt_Box_4_1.bind("<Return>", self.retrieve_input)

        self.prompt_Box_4_2 = Entry(self.frame, bd=2)
        self.prompt_Box_4_2.grid(row=7, column=2)
        self.prompt_Box_4_2.insert(0, scores1[7])
        self.prompt_Box_4_2.bind("<Return>", self.retrieve_input)

        # The fifth row with entries
        side_label_5 = Label(self.frame, text="Test 2:")
        side_label_5.grid(row=8, column=0, sticky=E)

        self.prompt_Box_5_1 = Entry(self.frame, bd=2)
        self.prompt_Box_5_1.grid(row=8, column=1)
        self.prompt_Box_5_1.insert(0, scores1[8])
        self.prompt_Box_5_1.bind("<Return>", self.retrieve_input)

        self.prompt_Box_5_2 = Entry(self.frame, bd=2)
        self.prompt_Box_5_2.grid(row=8, column=2)
        self.prompt_Box_5_2.insert(0, scores1[9])
        self.prompt_Box_5_2.bind("<Return>", self.retrieve_input)

        # The sixth row with entries
        side_label_6 = Label(self.frame, text="Test 3:")
        side_label_6.grid(row=9, column=0, sticky=E)

        self.prompt_Box_6_1 = Entry(self.frame, bd=2)
        self.prompt_Box_6_1.grid(row=9, column=1)
        self.prompt_Box_6_1.insert(0, scores1[10])
        self.prompt_Box_6_1.bind("<Return>", self.retrieve_input)

        self.prompt_Box_6_2 = Entry(self.frame, bd=2)
        self.prompt_Box_6_2.grid(row=9, column=2)
        self.prompt_Box_6_2.insert(0, scores1[11])
        self.prompt_Box_6_2.bind("<Return>", self.retrieve_input)

        # The seventh row with entries ... how many more do I have?
        side_label_7 = Label(self.frame, text="THE FINAL...:")
        side_label_7.grid(row=10, column=0, sticky=E)

        self.prompt_Box_7_1 = Entry(self.frame, bd=2)
        self.prompt_Box_7_1.grid(row=10, column=1)
        self.prompt_Box_7_1.insert(0, scores1[12])
        self.prompt_Box_7_1.bind("<Return>", self.retrieve_input)

        self.prompt_Box_7_2 = Entry(self.frame, bd=2)
        self.prompt_Box_7_2.grid(row=10, column=2)
        self.prompt_Box_7_2.insert(0, scores1[13])
        self.prompt_Box_7_2.bind("<Return>", self.retrieve_input)

        # The eighth row with entries ... just some extra credit
        side_label_8 = Label(self.frame, text="Extra Credit:")
        side_label_8.grid(row=11, column=0, sticky=E)

        self.prompt_Box_8_1 = Entry(self.frame, bd=2)
        self.prompt_Box_8_1.grid(row=11, column=1, sticky=N)
        self.prompt_Box_8_1.insert(0, scores1[14])
        self.prompt_Box_8_1.bind("<Return>", self.retrieve_input)

        self.prompt_Box_8_2 = Entry(self.frame, bd=2)
        self.prompt_Box_8_2.grid(row=11, column=2, sticky=N)
        self.prompt_Box_8_2.insert(0, scores1[15])
        self.prompt_Box_8_2.bind("<Return>", self.retrieve_input)

        # This is some code to have the cells expand as the screen expands. First the columns
        Grid.columnconfigure(self.frame, 0, weight=2)
        Grid.columnconfigure(self.frame, 1, weight=1)
        Grid.columnconfigure(self.frame, 2, weight=1)
        Grid.columnconfigure(self.frame, 3, weight=3)

        # Then the rows. Not much is done here, but looking at the final product, I'm okay with that. It collapses well
        Grid.rowconfigure(self.frame, 0, weight=7)
        Grid.rowconfigure(self.frame, 1, weight=3)
        Grid.rowconfigure(self.frame, 2, weight=7)
        Grid.rowconfigure(self.frame, 3, weight=1)
        Grid.rowconfigure(self.frame, 4, weight=1)
        Grid.rowconfigure(self.frame, 5, weight=1)
        Grid.rowconfigure(self.frame, 6, weight=1)
        Grid.rowconfigure(self.frame, 7, weight=1)
        Grid.rowconfigure(self.frame, 8, weight=1)
        Grid.rowconfigure(self.frame, 9, weight=1)
        Grid.rowconfigure(self.frame, 10, weight=1)
        Grid.rowconfigure(self.frame, 11, weight=1)
        Grid.rowconfigure(self.frame, 12, weight=0)

        # This is the code for the buttons
        self.submit_Button = Button(self.frame, text="Submit", command=self.retrieve_input, bd=4)
        self.submit_Button.grid(row=12, column=2, columnspan=1, padx=0, pady=40)
        self.submit_Button.bind("<button-1>")

        self.reset_Button = Button(self.frame, text="Reset", command=reset_scores, bd=4)
        self.reset_Button.grid(row=12, column=1, columnspan=1, padx=0, pady=40)
        self.reset_Button.bind("<button-1>")

        # This is a developing but of code that can do a lot of cool things. But it kinda makes me wanna cry...
        menu = Menu(master)
        root.config(menu=menu)

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

        sub_save_menu.add_command(label=class1, command=set_math_path)
        sub_save_menu.add_command(label=class2, command=set_comp_path)
        sub_save_menu.add_command(label=class3, command=set_phys_path)
        sub_save_menu.add_command(label=class4, command=set_span_path)
        sub_save_menu.add_command(label=class5, command=set_engl_path)
        sub_save_menu.add_command(label=class6, command=set_hist_path)
        sub_save_menu.add_command(label=class7, command=set_chem_path)

        subsub_menu.add_command(label=class1, command=open_math)
        subsub_menu.add_command(label=class2, command=open_comp)
        subsub_menu.add_command(label=class3, command=open_phys)
        subsub_menu.add_command(label=class4, command=open_span)
        subsub_menu.add_command(label=class5, command=open_engl)
        subsub_menu.add_command(label=class6, command=open_hist)
        subsub_menu.add_command(label=class7, command=open_chem)

        scores_load_menu.add_command(label=class1, command=open_scores1)
        scores_load_menu.add_command(label=class2, command=open_scores2)
        scores_load_menu.add_command(label=class3, command=open_scores3)
        scores_load_menu.add_command(label=class4, command=open_scores4)
        scores_load_menu.add_command(label=class5, command=open_scores5)
        scores_load_menu.add_command(label=class6, command=open_scores6)
        scores_load_menu.add_command(label=class7, command=open_scores7)

        scores_save_menu.add_command(label=class1, comman=save_scores1)
        scores_save_menu.add_command(label=class2, comman=save_scores2)
        scores_save_menu.add_command(label=class3, comman=save_scores3)
        scores_save_menu.add_command(label=class4, comman=save_scores4)
        scores_save_menu.add_command(label=class5, comman=save_scores5)
        scores_save_menu.add_command(label=class6, comman=save_scores6)
        scores_save_menu.add_command(label=class7, comman=save_scores7)

        sub_menu.add_command(label='Quit', command=root.destroy)

        customize_menu = Menu(menu, tearoff=False)
        menu.add_cascade(label='Customize', menu=customize_menu)
        naming = Menu(customize_menu, tearoff=False)
        customize_menu.add_cascade(label='Rename Classes', menu=naming)
        naming.add_command(label='Rename Class 1', command=prompt_math)
        naming.add_command(label='Rename Class 2', command=prompt_comp)
        naming.add_command(label='Rename Class 3', command=prompt_phys)
        naming.add_command(label='Rename Class 4', command=prompt_span)
        naming.add_command(label='Rename Class 5', command=prompt_engl)
        naming.add_command(label='Rename Class 6', command=prompt_hist)
        naming.add_command(label='Rename Class 7', command=prompt_chem)

        help_menu = Menu(menu, tearoff=False)
        menu.add_cascade(label='Help', menu=help_menu)
        help_menu.add_command(label='Help', command=help_box)
        help_menu.add_command(label='About', command=about_box)

    # This function takes the inputs
    def retrieve_input(self, *args):


        if self.var1.get() == 0:
            written = average(self.prompt_Box_1_1.get())
        else:
            written = drop_low_average(self.prompt_Box_1_1.get())
        if written == 9480203402:
            self.prompt_Box_1_1.config(bg='red')
        else:
            self.prompt_Box_1_1.config(bg=self.color)
        written_w = average(self.prompt_Box_1_2.get())
        written_f = written * (written_w / 100)
        if written_w == 9480203402:
            self.prompt_Box_1_2.config(bg='red')
        else:
            self.prompt_Box_1_2.config(bg=self.color)

        if self.var2.get() == 0:
            online = average(self.prompt_Box_2_1.get())
        else:
            online = drop_low_average(self.prompt_Box_2_1.get())
        if online == 9480203402:
            self.prompt_Box_2_1.config(bg='red')
        else:
            self.prompt_Box_2_1.config(bg=self.color)
        online_w = average(self.prompt_Box_2_2.get())
        online_f = online * (online_w / 100)
        if online_w == 9480203402:
            self.prompt_Box_2_2.config(bg='red')
        else:
            self.prompt_Box_2_2.config(bg=self.color)

        if self.var2.get() == 0:
            quizzes = average(self.prompt_Box_3_1.get())
        else:
            quizzes = drop_low_average(self.prompt_Box_3_1.get())
        if quizzes == 9480203402:
            self.prompt_Box_3_1.config(bg='red')
        else:
            self.prompt_Box_3_1.config(bg=self.color)
        quizzes_w = average(self.prompt_Box_3_2.get())
        quizzes_f = quizzes * (quizzes_w / 100)
        if quizzes_w == 9480203402:
            self.prompt_Box_3_2.config(bg='red')
        else:
            self.prompt_Box_3_2.config(bg=self.color)

        test1 = average(self.prompt_Box_4_1.get())
        if test1 == 9480203402:
            self.prompt_Box_4_1.config(bg='red')
        else:
            self.prompt_Box_4_1.config(bg=self.color)
        test1_w = average(self.prompt_Box_4_2.get())
        test1_f = test1 * (test1_w / 100)
        if test1_w == 9480203402:
            self.prompt_Box_4_2.config(bg='red')
        else:
            self.prompt_Box_4_2.config(bg=self.color)

        test2 = average(self.prompt_Box_5_1.get())
        if test2 == 9480203402:
            self.prompt_Box_5_1.config(bg='red')
        else:
            self.prompt_Box_5_1.config(bg=self.color)
        test2_w = average(self.prompt_Box_5_2.get())
        test2_f = test2 * (test2_w / 100)
        if test2_w == 9480203402:
            self.prompt_Box_5_2.config(bg='red')
        else:
            self.prompt_Box_5_2.config(bg=self.color)

        test3 = average(self.prompt_Box_6_1.get())
        if test3 == 9480203402:
            self.prompt_Box_6_1.config(bg='red')
        else:
            self.prompt_Box_6_1.config(bg=self.color)
        test3_w = average(self.prompt_Box_6_2.get())
        test3_f = test3 * (test3_w / 100)
        if test3_w == 9480203402:
            self.prompt_Box_6_2.config(bg='red')
        else:
            self.prompt_Box_6_2.config(bg=self.color)

        final = average(self.prompt_Box_7_1.get())
        if final == 9480203402:
            self.prompt_Box_7_1.config(bg='red')
        else:
            self.prompt_Box_7_1.config(bg=self.color)
        final_w = average(self.prompt_Box_7_2.get())
        final_f = final * (final_w / 100)
        if final_w == 9480203402:
            self.prompt_Box_7_2.config(bg='red')
        else:
            self.prompt_Box_7_2.config(bg=self.color)

        extra_credit = average(self.prompt_Box_8_1.get())
        if extra_credit == 9480203402:
            self.prompt_Box_8_1.config(bg='red')
        else:
            self.prompt_Box_8_1.config(bg=self.color)
        extra_credit_w = average(self.prompt_Box_8_2.get())
        extra_credit_f = extra_credit * (extra_credit_w / 100)
        if extra_credit_w == 9480203402:
            self.prompt_Box_8_2.config(bg='red')
        else:
            self.prompt_Box_8_2.config(bg=self.color)

        # The sum of the weights
        final_weight = written_w + online_w + quizzes_w + test1_w + test2_w + test3_w + final_w

        top_disp = ""

        # This is a test vector. I want to make sure none of the inputs were bad
        test_arr = [written, online, quizzes, test1, test2, test3, final, extra_credit, written_w,
                    online_w, quizzes_w, test1_w, test2_w, test3_w, final_w, extra_credit_w]

        # A continuation of what I was doing. If a number were a string, it would get
        # turned into that long, awful number
        no_good = 0
        for x in range(len(test_arr)):
            if test_arr[x] == 9480203402:
                no_good = 1
                final_arr = 9480203402
                break

        # This is a test to make sure we're not dividing by 0
        if final_weight == 0:
            no_good = 1
            final_arr = 9480203402
            tkinter.messagebox.showinfo('You really screwed up this time', "Bro. Literally all your weights were 0")

        if no_good == 0:
            final_arr = written_f + online_f + quizzes_f + test1_f + test2_f + test3_f + final_f + extra_credit_f

        scorer(final_arr, final_weight)


# The purpose of this function is to both make the conversion
# from string to float and average any lists of grades entered
def average(scores):

    if scores[0] == '#':
        scores = '0'

    test1 = scores.split(',')

    while True:
        try:
            for x in range(len(test1)):
                test1[x] = float(test1[x])
            break
        except ValueError:
            tkinter.messagebox.showinfo('You really screwed up this time', ' \"' + scores + "\" is not a valid input  ")
            test1 = [9480203402]
            break

    scores = test1

    avg = sum(scores) / len(scores)

    return avg


# This is the same function as the last, only it stores the
# lowest score as an unused variable and aveages the rest of them
def drop_low_average(scores):

    if scores[0] == '#':
        scores = '0'

    test1 = scores.split(',')

    while True:
        try:
            for x in range(len(test1)):
                test1[x] = float(test1[x])
            break
        except ValueError:
            tkinter.messagebox.showinfo('You really screwed up this time', ' \"' + str(scores) + "\" is not a valid input  ")
            test1 = [9480203402]
            break

    scores = test1

    if len(scores) > 1:
        scores.sort()
        dummy, *scores = scores

    avg = sum(scores) / len(scores)

    return avg


# The purpose of this function is to take the final score and
# final weight and calculate our long-awaited average!
def scorer(final_arr, weight):

    if final_arr == 9480203402:
        weight = 100

    avg = final_arr / (weight / 100)

    grade(avg)


# This function just returns the grade for the class and calls the function to tell the user the result
def grade(avg):
    if avg > 100:
        mid_disp = "Dude, you're such a cheater. Or a liar. I'm not sure which"
    elif avg >= 92.5:
        mid_disp = "You got an A! :)"
    elif avg >= 89.5:
        mid_disp = "You got an A-!"
    elif avg >= 86.5:
        mid_disp = "You got a B+"
    elif avg >= 82.5:
        mid_disp = "You got a B"
    elif avg >= 79.5:
        mid_disp = "You got a B- :("
    elif avg >= 76.5:
        mid_disp = "You got a C+ :("
    elif avg >= 72.5:
        mid_disp = "You got a C :'("
    elif avg >= 69.5:
        mid_disp = "You got a C- :'("
    elif avg >= 66.5:
        mid_disp = "You got a D+ :'0"
    elif avg >= 62.5:
        mid_disp = "You got a D :'0"
    elif avg >= 59.5:
        mid_disp = "You got a D- :'0_"
    else:
        mid_disp = "You got an F\nJust go kill yourself"

    if int(round(avg)) != 9480203402:
        while TRUE:
            try:
                temp_root.destroy()
                break
            finally:
                break

        abre_ventana(avg, mid_disp)


# This actually opens the window in which the user sees the final grade result
def abre_ventana(middle, last):
    global temp_root

    temp_root = Tk()

    label2 = Label(temp_root, text="\nYour average is currently: " + "{0:.2f}".format(middle) + "\n")
    label2.pack(padx=19)

    label3 = Label(temp_root, text=last + '\n')
    label3.pack()

    temp_root.iconbitmap('favicon.ico')
    temp_root.title('Result')


# This opens the tkinter box with the help menu in it. It currently has four different options to explain the
# four different parts of the application. I had to make a bunch of global variables since you can't call
# a variable from inside a function, and it's hard to call a class from a menu button.
def help_box():
    global var, label, gen_text, rnme_text, syl_text, grd_text

    global help_root


    while True:
        try:
            help_root.destroy()
            break
        finally:
            break

    help_root = Tk()

    var = tkinter.StringVar(help_root)
    # initial value
    var.set('General')
    choices = ['General', 'Renaming Classes', 'Opening Your Syllabus', 'Opening Saved Grades']
    option = tkinter.OptionMenu(help_root, var, *choices)

    option.grid(pady=20, sticky=S)

    help_root.title('Socorro!')

    gen_text ="Welcome to the Grade Averager!\n\n" \
              "In the grade percentage, enter as many grades as you want in the\n" \
              "same box separated by commas and they will be averaged. Then put the\n" \
              "percentage of weight they have and enter it. Feel free to leave any boxes\n" \
              "empty. If you don't want the program to read a box, enter # before the\n" \
              "number(s). Even though you are probably a friend or family member if\nyou are reading this, please give suggestions and comments!"

    rnme_text = "So, this is pretty straightforward, but I'll hold your hand and tell you how\n" \
                "to do it anyways. Well, I won't hold your hand, but you get the idea.\n" \
                "Unless you're a freshman engineering student like me, you probably aren't\n" \
                "taking math, physics, computer science, blah, blah, blah. So just go to\n" \
                "Customize > Rename Classes pick the class you want to rename. From there\n" \
                "enter your class' name in the box and hit enter. Name it anything. I dare ya."

    syl_text = "Because I, too, am a lazy college student, I know that you don't want\n" \
               "to find your syllabus every time you need to calculate your grades!\n" \
               "As a result, there is a built-in function that makes it so you only have\n" \
               "to browse your computer once for that obsolete PDF. Just go to\n" \
               "File > Save Syllabus and pick the class you want to save your syllabus for.\n" \
               "Then next time you need that syllabus, just go to File > Open Syllabus and\n" \
               "that syllabus will open in your default .pdf reader. Feel free to move\n" \
               "or get rid of the syllabus. It is saved inside the program.\n" \
               "*Please note that your syllabus must be in .pdf form*"

    grd_text = "What's the use of a grade calculator that doesn't remember your grades, you ask?\n" \
               "The answer is none. And if you have a grade calculator that can't even remember\n" \
               "some stupid numbers, then you need to burn it with fire! Here, though, you just\n" \
               "have to enter your grades, and when you're done go to File > Save Grades and pick\n" \
               "the class that you just entered grades for. Then next time you want to update or\n" \
               "view them, just go to File > Open Grades and they will magically appear, just like\n" \
               "you left them!\n"

    label = Label(help_root, text=gen_text)
    label.grid(row=0, column=1, rowspan=2, padx=30, pady=30, sticky=N)

    button = Button(help_root, text="Go!", command=update_label)
    button.grid(row=1, padx=70, pady=20, sticky=N)

    help_root.iconbitmap('favicon.ico')

    help_root.mainloop()

def update_label():
    global var, label, gen_text, rnme_text, syl_text, grd_text

    if var.get() == 'General':
        label.config(text=gen_text)

    if var.get() == 'Renaming Classes':
        label.config(text=rnme_text)

    if var.get() == 'Opening Your Syllabus':
        label.config(text=syl_text)

    if var.get() == 'Opening Saved Grades':
        label.config(text=grd_text)

# This opens the about box. Just makin' sure people get straight who made this epic program
def about_box():
    global about

    while True:
        try:
            about.destroy()
            break
        finally:
            break
    about = Tk()
    about.title('We all cool here')

    label = Label(about, text="This is a privately developed Python GUI Application\n"
                              "developed soley by Matthew Niemiec. Feel free to use\n"
                              "it as needed, just don't do anything stupid like showing\n"
                              "it to your friends and saying it's yours. That's just\n"
                              "rude. Special thanks to Adam Smith for critiques and\n"
                              "general guidance. You're the coolest, Adam!")
    label.pack(side=TOP, padx=30, pady=30)

    about.iconbitmap('favicon.ico')

    about.mainloop()


# This essentially copies and pastes the user's choice of PDF file into the folder and renames
# renames it so that the program can consistently read it and open it.
def set_math_path():
    fname = askopenfilename(filetypes=(("PDF files", "*.pdf;*.PDF"),
                                       ("All files", "*.*")))

    try:
        shutil.copyfile(fname, 'math_syl.pdf')
    except:
        pass


# Same thing as the above function, only with the second class, which happens to be Physics by default
def set_phys_path():
    fname = askopenfilename(filetypes=(("PDF files", "*.pdf;*.PDF"),
                                       ("All files", "*.*")))

    try:
        shutil.copyfile(fname, 'phys_syl.pdf')
    except:
        pass


# Same thing as the above function, only with the third class, which happens to be Computer Science by default
def set_comp_path():
    fname = askopenfilename(filetypes=(("PDF files", "*.pdf;*.PDF"),
                                       ("All files", "*.*")))

    try:
        shutil.copyfile(fname, 'comp_syl.pdf')
    except:
        pass


# Same thing as the above function, only with the fourth class, which happens to be Spanish by default
def set_span_path():
    fname = askopenfilename(filetypes=(("PDF files", "*.pdf;*.PDF"),
                                       ("All files", "*.*")))

    while TRUE:
        try:
            shutil.copyfile(fname, 'span_syl.pdf')
            break
        finally:
            break


# Same thing as the above function, only with the fourth class, which happens to be Spanish by default
def set_engl_path():
    fname = askopenfilename(filetypes=(("PDF files", "*.pdf;*.PDF"),
                                       ("All files", "*.*")))

    while TRUE:
        try:
            shutil.copyfile(fname, 'engl_syl.pdf')
            break
        finally:
            break


# Same thing as the above function, only with the fourth class, which happens to be Spanish by default
def set_hist_path():
    fname = askopenfilename(filetypes=(("PDF files", "*.pdf;*.PDF"),
                                       ("All files", "*.*")))

    while TRUE:
        try:
            shutil.copyfile(fname, 'hist_syl.pdf')
            break
        finally:
            break


# Same thing as the above function, only with the fourth class, which happens to be Spanish by default
def set_chem_path():
    fname = askopenfilename(filetypes=(("PDF files", "*.pdf;*.PDF"),
                                       ("All files", "*.*")))

    while TRUE:
        try:
            shutil.copyfile(fname, 'chem_syl.pdf')
            break
        finally:
            break


# This function first asks the user what they want to rename their first class to
def prompt_math():
    global math_root

    # This just makes sure that there isn't already the same box open
    while TRUE:
        try:
            math_root.destroy()
            break
        finally:
            break

    # This code is for the actual box that the user inputs their name into
    math_root = Tk()
    math_root.title("Name Changer")
    math_root.iconbitmap('favicon.ico')

    label = Label(math_root, text='     What would you like to call your first class?')
    label.grid(row=0, column=0, sticky=E, pady=25)
    global entry
    entry = Entry(math_root)
    entry.grid(row=0, column=1, sticky=W, pady=25)
    entry.bind("<Return>", submit_math)
    space = Label(math_root, text='    ')
    space.grid(row=0, column=2)

    button = Button(math_root, text='Submit', command=submit_math)
    button.grid(row=1, columnspan=3)
    bottom_space = Label(math_root, text=' ')
    bottom_space.grid(row=2, pady=1)

    math_root.mainloop()


# Synonymous with the function above, it takes the string from the entry box, destroys the window, and restarts the
# program with the renamed classes
def submit_math(*args):
    global class1, entry, root, test

    class1 = entry.get()

    if len(class1) > 18:
        class1 = class1[0:16] + '...'

    math_write = open('math.txt', 'w')
    math_write.write(class1)
    math_write.close()

    math_root.destroy()

    dims = [root.winfo_x(), root.winfo_y(), root.winfo_height(), root.winfo_width()]
    test.master.destroy()
    root = Tk()
    root.geometry('%dx%d+%d+%d' % (dims[3], dims[2], dims[0], dims[1]))
    test = AverageClass(root)
    root.iconbitmap('favicon.ico')


# If you didn't notice, the next six functions are continuations of the last two, only with the remaining three classes
def prompt_comp():
    global comp_root

    while TRUE:
        try:
            comp_root.destroy()
            break
        finally:
            break

    comp_root = Tk()
    comp_root.title("Name Changer")
    comp_root.iconbitmap('favicon.ico')

    label = Label(comp_root, text='     What would you like to call your second class?')
    label.grid(row=0, column=0, sticky=E, pady=25)
    global entry1
    entry1 = Entry(comp_root)
    entry1.grid(row=0, column=1, sticky=W, pady=25)
    entry1.bind("<Return>", submit_comp)
    space = Label(comp_root, text='    ')
    space.grid(row=0, column=2)

    button = Button(comp_root, text='Submit', command=submit_comp)
    button.grid(row=1, columnspan=3)
    bottom_space = Label(comp_root, text=' ')
    bottom_space.grid(row=2, pady=1)

    comp_root.mainloop()


# The second function for the second class
def submit_comp(*args):
    global class2, entry1, root, test

    class2 = entry1.get()

    if len(class2) > 18:
        class2 = class2[0:16] + '...'

    comp_write = open('comp.txt', 'w')
    comp_write.write(class2)
    comp_write.close()

    comp_root.destroy()

    dims = [root.winfo_x(), root.winfo_y(), root.winfo_height(), root.winfo_width()]
    test.master.destroy()
    root = Tk()
    root.geometry('%dx%d+%d+%d' % (dims[3], dims[2], dims[0], dims[1]))
    test = AverageClass(root)
    root.iconbitmap('favicon.ico')


# The first function for the third class
def prompt_phys():
    global phys_root

    while TRUE:
        try:
            phys_root.destroy()
            break
        finally:
            break

    phys_root = Tk()
    phys_root.title("Name Changer")
    phys_root.iconbitmap('favicon.ico')

    label = Label(phys_root, text='     What would you like to call your third class?')
    label.grid(row=0, column=0, sticky=E, pady=25)
    global entry2
    entry2 = Entry(phys_root)
    entry2.grid(row=0, column=1, sticky=W, pady=25)
    entry2.bind("<Return>", submit_phys)
    space = Label(phys_root, text='    ')
    space.grid(row=0, column=2)

    button = Button(phys_root, text='Submit', command=submit_phys)
    button.grid(row=1, columnspan=3)
    bottom_space = Label(phys_root, text=' ')
    bottom_space.grid(row=2, pady=1)

    phys_root.mainloop()


# The second function for the third class
def submit_phys(*args):
    global class3, entry2, root, test

    class3 = entry2.get()

    if len(class3) > 18:
        class3 = class3[0:16] + '...'

    phys_write = open('phys.txt', 'w')
    phys_write.write(class3)
    phys_write.close()

    phys_root.destroy()

    dims = [root.winfo_x(), root.winfo_y(), root.winfo_height(), root.winfo_width()]
    test.master.destroy()
    root = Tk()
    root.geometry('%dx%d+%d+%d' % (dims[3], dims[2], dims[0], dims[1]))
    test = AverageClass(root)
    root.iconbitmap('favicon.ico')


# The first function for the fourth class
def prompt_span():
    global span_root
    while TRUE:
        try:
            span_root.destroy()
            break
        finally:
            break

    span_root = Tk()
    span_root.title("Name Changer")
    span_root.iconbitmap('favicon.ico')

    label = Label(span_root, text='     What would you like to call your fourth class?')
    label.grid(row=0, column=0, sticky=E, pady=25)
    global entry3
    entry3 = Entry(span_root)
    entry3.grid(row=0, column=1, sticky=W, pady=25)
    entry3.bind("<Return>", submit_span)
    space = Label(span_root, text='    ')
    space.grid(row=0, column=2)

    button = Button(span_root, text='Submit', command=submit_span)
    button.grid(row=1, columnspan=3)
    bottom_space = Label(span_root, text=' ')
    bottom_space.grid(row=2, pady=1)

    span_root.mainloop()


# The first function for the fourth class
def submit_span(*args):
    global class4, entry3, test, root

    class4 = entry3.get()

    if len(class4) > 18:
        class4 = class4[0:16] + '...'

    span_write = open('span.txt', 'w')
    span_write.write(class4)
    span_write.close()

    span_root.destroy()

    dims = [root.winfo_x(), root.winfo_y(), root.winfo_height(), root.winfo_width()]
    test.master.destroy()
    root = Tk()
    root.geometry('%dx%d+%d+%d' % (dims[3], dims[2], dims[0], dims[1]))
    test = AverageClass(root)
    root.iconbitmap('favicon.ico')


# The first function for the fifth class
def prompt_engl():
    global engl_root
    while TRUE:
        try:
            engl_root.destroy()
            break
        finally:
            break

    engl_root = Tk()
    engl_root.title("Name Changer")
    engl_root.iconbitmap('favicon.ico')

    label = Label(engl_root, text='     What would you like to call your fifth class?')
    label.grid(row=0, column=0, sticky=E, pady=25)
    global entry4
    entry4 = Entry(engl_root)
    entry4.grid(row=0, column=1, sticky=W, pady=25)
    entry4.bind("<Return>", submit_engl)
    space = Label(engl_root, text='    ')
    space.grid(row=0, column=2)

    button = Button(engl_root, text='Submit', command=submit_engl)
    button.grid(row=1, columnspan=3)
    bottom_space = Label(engl_root, text=' ')
    bottom_space.grid(row=2, pady=1)

    engl_root.mainloop()


# The second function for the fifth class
def submit_engl(*args):
    global class5, entry4, test, root

    class5 = entry4.get()

    if len(class5) > 18:
        class5 = class5[0:16] + '...'

    engl_write = open('engl.txt', 'w')
    engl_write.write(class5)
    engl_write.close()

    engl_root.destroy()

    dims = [root.winfo_x(), root.winfo_y(), root.winfo_height(), root.winfo_width()]
    test.master.destroy()
    root = Tk()
    root.geometry('%dx%d+%d+%d' % (dims[3], dims[2], dims[0], dims[1]))
    test = AverageClass(root)
    root.iconbitmap('favicon.ico')


# The first function for the sixth class
def prompt_hist():
    global hist_root
    while TRUE:
        try:
            hist_root.destroy()
            break
        finally:
            break

    hist_root = Tk()
    hist_root.title("Name Changer")
    hist_root.iconbitmap('favicon.ico')

    label = Label(hist_root, text='     What would you like to call your fifth class?')
    label.grid(row=0, column=0, sticky=E, pady=25)
    global entry5
    entry5 = Entry(hist_root)
    entry5.grid(row=0, column=1, sticky=W, pady=25)
    entry5.bind("<Return>", submit_hist)
    space = Label(hist_root, text='    ')
    space.grid(row=0, column=2)

    button = Button(hist_root, text='Submit', command=submit_hist)
    button.grid(row=1, columnspan=3)
    bottom_space = Label(hist_root, text=' ')
    bottom_space.grid(row=2, pady=1)

    hist_root.mainloop()


# The second function for the fifth class
def submit_hist(*args):
    global class6, entry5, test, root

    class6 = entry5.get()

    if len(class6) > 18:
        class6 = class6[0:16] + '...'

    hist_write = open('hist.txt', 'w')
    hist_write.write(class6)
    hist_write.close()

    hist_root.destroy()

    dims = [root.winfo_x(), root.winfo_y(), root.winfo_height(), root.winfo_width()]
    test.master.destroy()
    root = Tk()
    root.geometry('%dx%d+%d+%d' % (dims[3], dims[2], dims[0], dims[1]))
    test = AverageClass(root)
    root.iconbitmap('favicon.ico')


# The first function for the seventh class
def prompt_chem():
    global chem_root
    while TRUE:
        try:
            chem_root.destroy()
            break
        finally:
            break

    chem_root = Tk()
    chem_root.title("Name Changer")
    chem_root.iconbitmap('favicon.ico')

    label = Label(chem_root, text='     What would you like to call your fifth class?')
    label.grid(row=0, column=0, sticky=E, pady=25)
    global entry6
    entry6 = Entry(chem_root)
    entry6.grid(row=0, column=1, sticky=W, pady=25)
    entry6.bind("<Return>", submit_chem)
    space = Label(chem_root, text='    ')
    space.grid(row=0, column=2)

    button = Button(chem_root, text='Submit', command=submit_chem)
    button.grid(row=1, columnspan=3)
    bottom_space = Label(chem_root, text=' ')
    bottom_space.grid(row=2, pady=1)

    chem_root.mainloop()


# The second function for the seventh(!) class
def submit_chem(*args):
    global class7, entry6, test, root

    class7 = entry6.get()

    if len(class7) > 18:
        class7 = class7[0:16] + '...'

    chem_write = open('chem.txt', 'w')
    chem_write.write(class7)
    chem_write.close()

    chem_root.destroy()

    dims = [root.winfo_x(), root.winfo_y(), root.winfo_height(), root.winfo_width()]
    test.master.destroy()
    root = Tk()
    root.geometry('%dx%d+%d+%d' % (dims[3], dims[2], dims[0], dims[1]))
    test = AverageClass(root)
    root.iconbitmap('favicon.ico')


test = AverageClass(root)

root.iconbitmap('favicon.ico')

root.mainloop()

# This is just to reset the active scores so that next time the user opens the program, all 0's are displayed
score_writer = open('active.txt', 'w')
score_writer.write('0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0')
score_writer.close()

# What I still want to do:
# 1) Add/remove rows based on class
# 2) Have user choose extra credit
