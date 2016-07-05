from tkinter import *
from tkinter import messagebox
import smtplib
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
import os
import socket
import datetime
import shutil
import platform
from threading import Thread
import sys
import ctypes
import winshell


path = ""

# This program is for discipleship. The program runs every time the computer is started and asks the user if they have
# read their Bible yet today. They can also enter "Setup", where they can enter their information to send to someone
# who's name they enter to an email of their choosing. The email is sent from disciplereading2016@gmail.com
# It is more convenient to have a separate email due to Gmail's 2-step verification process necessary to obtain and
# app password to send from a Python application. All answers are assumed to be honest, but cannot be changed later
# as all results are encrypted in their files. The program itself is stored in Shell:Startup from Run, which is
# deep within the hidden %Appdata% folder. The files storing the information are stored within the folder below so that
# they don't run on startup, in a created directory called "DiscRead". Sounds normal enough, but is actually short for.
# you guessed it, Disciple Reading. The user can also choose to uninstall or remove the program (since it doesn't
# technically install), and that will remove all files created by the program. As of this date, 5/19/16, no testing
# has been done, though I think that the code should at least work as is. To use, simply run DiscipleReading.exe from
# any directory, or even across hard drives, and the program will automatically move itself. I don't yet know if it
# will run right away, but it will at least run on the next startup. I pray that God blesses people through this,
# and it can help disciplers aid their disciples in studying the Scriptures. The idea of the program is that they should
# get in the Word before starting their day. Though I don't think that there's anything wrong with reading at night,
# it has not worked for me thus far and a much rougher version of this has already helped me this summer, and I pray
# that God can use this to encourage others just the same. This was developed by Matthew Niemiec on, as mentioned
# May 19th, 2016, discipled by Derek Gregory, who inspired the program


# This is the function that takes a file name as an input, reads the file, encrypts it, and stores the encrypted
# Data in Results.txt, which in this case (for Windows) stores it in a new directory in the folder below the Startup
# Folder, where the program is stored to run on startup. This function has problems storing text in the same file from
# which it got it, so it always reads in Temp.txt, which I've written unencrypted text to
def encrypt(key, filename):
    chunksize = 64*1024
    output_file = path + "\DiscRead\Results.txt"
    filesize = str(os.path.getsize(filename)).zfill(16)
    IV = Random.new().read(16)

    encryptor = AES.new(key, AES.MODE_CBC, IV)

    with open(filename, 'rb') as infile:
        with open(output_file, 'wb') as outfile:
            outfile.write(filesize.encode('utf-8'))
            outfile.write(IV)

            while True:
                chunk = infile.read(chunksize)

                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b' ' * (16 - (len(chunk) % 16))

                outfile.write(encryptor.encrypt(chunk))


# This function takes the file name as an input argument, which is presumably already encrypted, and stores the
# decrypted text in Results.txt. This function does not have problems storing into a file with the same name as it
# is reading from
def decrypt(key, filename):
    chunksize = 64*1024
    output_file = path + "\DiscRead\Results.txt"

    with open(filename, 'rb') as infile:
        filesize = int(infile.read(16))
        IV = infile.read(16)

        decryptor = AES.new(key, AES.MODE_CBC, IV)

        with open(output_file, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)

                if len(chunk) == 0:
                    break

                outfile.write(decryptor.decrypt(chunk))

            outfile.truncate(filesize)


# This function turns the coders's (my) password into an encoded hash function. I'm not gonna lie, I don't know a lot
# about encryption, so if you're reading this, you may know more about this function than I do at this point
def get_key(password):
    hasher = SHA256.new(password.encode('utf-8'))
    return hasher.digest()


# This function decrypts Results.txt, reads the information, writes the text to Temp.txt, encrypts Temp.txt to
# Results.txt, deletes Temp.txt, and returns the unencrypted text. It can't leave Results.txt unencrypted in the case
# that the user closes out of the program before entering the results, which results in errors the next time the
# program runs, as it can't unencrypt English
def decr_res():
    try:
        decrypt(get_key("n2J4zP"), path + "\DiscRead\Results.txt")
    except FileNotFoundError:
        return ""

    opening = open(path + "\DiscRead\Results.txt", 'r')
    text = opening.read()
    opening.close()

    temp = open(path + "\DiscRead\Temp.txt", 'w')
    temp.write(text)
    temp.close()

    encrypt(get_key("n2J4zP"), path + "\DiscRead\Temp.txt")
    os.remove(path + "\DiscRead\Temp.txt")

    return text


# This program takes the newly updated text, writes it to Temp.txt, encrypts to Results.txt, and deletes Temp.txt
def encr_res(text):
    decrypted_text = open(path + "\DiscRead\Temp.txt", 'w')
    decrypted_text.write(text)
    decrypted_text.close()

    encrypt(get_key("n2J4zP"), path + "\DiscRead\Temp.txt")
    os.remove(path + "\DiscRead\Temp.txt")


# This function returns the date in format '05/19/2016'
def get_date():
    date = str(datetime.datetime.now())[:10]
    date = "%s/%s/%s" % (date[5:7], date[8:10], date[0:4])
    return date


# This is the function that runs every time on startup that checks if the user has already logged in to their computer
# yet that day. This may not be the most convenient location for it, granted.
def check_day():
    date = get_date()
    try:
        text = decr_res()
    except FileNotFoundError:
        return True

    if date in text[-15:]:
        return False
    return True


# This function runs when the user presses Help in the GUI. It is an incredibly basic GUI
def help_menu():
    info = ("Commands:\n1) Uninstall - This will stop the program from\nrunning on startup and remove all files from "
            "your computer\nExit this, then go to Run and enter Shell:Startup\nand delete DiscipleReading.exe\n"
            "2) Send Results - This will send your results regardless\nof the date, "
            "provided you have an Internet connection")

    root = Tk()
    root.title("Help")

    label = Label(root, text=info)
    label.pack(padx=20, pady=20)

    root.mainloop()


# This function runs when the user sets up their name and email. It sends aan email to their discipler, letting them
# know what's up and give them a chance to reply and opt out in the case of a wrong address
def mail_setup(name, discipler, email):

    text = ('Subject: Dsiciple Reading Setup\nHi ' + discipler + ', you\'ve been requested to'
                        ' receive results for ' + name + '\'s Bible reading every month. ' + name + ' will'
                        ' be asked daily if they\'ve read the Bible before turning on their computer, and '
                        'they\'ve entered your email to receive their results. If this doesn\'t sound familiar'
                        ', please give a brief reply to ensure you don\'t keep getting emails. '
                        'Thank you for serving!')

    return mail_sender(email, text)


# This function is, well, the point of the program. It runs the first of every month and lets the receiver know how the
# user has done. It checks to make sure it can open the file, checks and makes sure that there's an Internet connection,
# and if all goes well sends the results. It also deletes the Reuslts.txt file so that results are not cumulative
def mail_results():
    try:
        getting = open(path + "\DiscRead\Info.txt", 'r')
        name, discipler, email = getting.read().split('\n')
        getting.close()
    except FileNotFoundError:
        Tk().withdraw()
        messagebox.showinfo("Email Your Results!", "Let someone know how you've done! "
                                                    "Next time you start your computer, enter 'setup' "
                                                    "and press enter")
        return

    date = get_date()
    if "/01/" not in date:
        return

    try:
        text = decr_res()
        os.remove(path + "\DiscRead\Results.txt")
    except FileNotFoundError:
        Tk().withdraw()
        messagebox.showerror("No results!", "It looks like you don't have any results to send!")
        return

    yeses = text.count("Yes")
    nos = text.count("No")

    sending_text = ('Subject: Monthly Reading Results.\n' + discipler + ' - here\'s the monthly results '
                                                                        'from reading my Bible! '
                                                                        'Please be praying for me'
                                                                        ' that I might continue in His Word.\n\n- '
                    + name + '\n\n' + text + '\n\nTimes Bible was read before using computer: ' +
                    str(yeses) + "\nTimes Bible was not read before using computer: " + str(nos))

    mail_sender(email, sending_text)


# This function is the same as the last, only instead of running on the first of each month, it runs whenever the user
# enters 'Send Results'. The text is worded a little bit differently
def mail_manually():
    try:
        getting = open(path + "\DiscRead\Info.txt", 'r')
        name, discipler, email = getting.read().split('\n')
        getting.close()
    except FileNotFoundError:
        Tk().withdraw()
        messagebox.showerror("Not Again...", "Sorry, but you're still not connected to the Internet. Check "
                                             "your connection and try again")
        return

    try:
        text = decr_res()
        os.remove(path + "\DiscRead\Results.txt")
    except FileNotFoundError:
        Tk().withdraw()
        messagebox.showerror("No results!", "It looks like you don't have any results to send!")
        return

    yeses = text.count("Yes")
    nos = text.count("No")

    date = get_date()

    sending_text = ('Subject: Monthly Reading Results.\n' + discipler + ' - here\'s the monthly results '
                                                                       'from reading my Bible! '
                                                                       'Please be praying for me '
                                                                       'that I might continue in His Word.\n\n- '
    + name + '\n\n' + text + '\n\nTimes Bible was read before using computer: ' +
    str(yeses) + "\nTimes Bible was not read before using computer: " + str(nos))

    if "/01/" in date or "/1/" in date:
        mail_sender(email, sending_text)


# This function has the task of connecting to Gmail and actually sending the text previously writeen
def mail_sender(send_to, text):
    try:
        smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_obj.ehlo()
        smtp_obj.starttls()
        smtp_obj.login("disciplereading2016@gmail.com", 'kllngcezryttzzvg')
        smtp_obj.sendmail('disciplereading2016@gmail.com', send_to, text)

        smtp_obj.quit()
        return True
    except socket.gaierror:
        Tk().withdraw()
        messagebox.showerror("Error!", "Your results were supposed to be sent, but it looks"
                                       " like you're not connected to the Internet. Check Help for info on sending"
                                       " results manually once you've reconnected")
        return False


# This program removes the program and all it's files, including the created directory, off of the user's computer
def uninstall():
    Tk().withdraw()
    if messagebox.askokcancel("No Going Back!", "Uninstalling will remove the program "
                                                "and all files from your computer!"):
        try:
            os.remove(path + "\DiscRead\Temp.txt")
        except FileNotFoundError:
            pass
        try:
            os.remove(path + "\DiscRead\Results.txt")
        except FileNotFoundError:
            pass
        try:
            os.remove(path + "\DiscRead\Info.txt")
        except FileNotFoundError:
            pass
        try:
            shutil.rmtree(path + "\DiscRead")
        except FileNotFoundError:
            pass
        try:
            shutil.move("DiscipleReading.exe", path + "\DiscipleReading.exe")
            sys.exit(0)
        except FileNotFoundError:
            Tk().withdraw()
            messagebox.showerror("Sorry!", "We are still working on finding a solution to uninstallation, but you'll"
                                           "have to delete it manually in the meantime!. Please refer to 'Help'")


# This is the class GUI used to set up the user's name, their discipler's name, and their discipler's email address
# It is incredibly self-explanatory, so there will be minimal commenting
class Setup:
    def __init__(self):
        # Creating the GUI
        self.first_name = ""
        self.first_discipler = ""
        self.address = ""

        self.root = Tk()
        self.root.title("Disciple Reading")

        self.welcome = Label(self.root, text="Welcome to Disciple Reading!", font=("Helvetica", 16))
        self.welcome.grid(row=0, column=0, columnspan=3, padx=65, pady=30)

        Label(self.root, text="What is your name?").grid(row=1, column=0, padx=0, pady=10, sticky=E)
        self.name = Entry(self.root)
        self.name.grid(row=1, column=1, padx=0, pady=0, sticky=W)
        self.name.bind("<Return>", self.sumbit_info)

        Label(self.root, text="What is the name of your discipler?").grid(row=2, column=0, padx=0, pady=10, sticky=E)
        self.discipler = Entry(self.root)
        self.discipler.grid(row=2, column=1, padx=0, pady=10, sticky=W)
        self.discipler.bind("<Return>", self.sumbit_info)

        Label(self.root, text="What is their email address?").grid(row=3, column=0, padx=0, pady=10, sticky=E)
        self.email = Entry(self.root)
        self.email.grid(row=3, column=1, padx=0, pady=10, sticky=W)
        self.email.bind("<Return>", self.sumbit_info)

        Label(self.root, text="Please confirm their email address").grid(row=4, column=0, padx=0, pady=10, sticky=E)
        self.confirm = Entry(self.root)
        self.confirm.grid(row=4, column=1, padx=0, pady=10, sticky=W)
        self.confirm.bind("<Return>", self.sumbit_info)

        self.submit = Button(self.root, text="Submit", command=lambda: Thread(target=self.sumbit_info))
        self.submit.grid(row=90, column=0, padx=20, pady=20)

        self.switch = Button(self.root, text="Daily results", command=self.daily)
        self.switch.grid(row=90, column=1, padx=20, pady=20)

        self.status = Label(self.root, text="")
        self.status.grid(row=99, column=0, columnspan=2, padx=20, pady=20)

        self.root.mainloop()

    # Checks and collects info from entries and sends email to discipler
    def sumbit_info(self, *args):
        self.status.config(text="Getting set up...")
        self.first_name = self.name.get().split()

        self.first_discipler = self.discipler.get().split()
        if not self.first_name or not self.first_discipler:
            self.first_name = ""
            self.first_discipler = ""
        else:
            self.first_name = self.first_name[0].title()
            self.first_discipler = self.first_discipler[0].title()

        self.address = self.email.get()
        confirmed = self.confirm.get()

        if self.first_name == "" or self.first_discipler == "" or self.address == "" or confirmed == "":
            self.status.config(text="One or more boxes is empty")
            return
        elif not self.is_good(self.address):
            self.status.config(text="Not a valid email address")
            return
        elif self.address != confirmed:
            self.status.config(text="Emails do not match!")
            return
        else:
            if self.check_txt():
                Tk().withdraw()
                if not messagebox.askyesno("Are You Sure?", "You've already been set up. "
                                                            "Are you sure you want to continue?"):
                    self.status.config(text="Take your time")
                    return

            self.write_results()
            if mail_setup(self.first_name, self.first_discipler, self.address):
                self.status.config(text="Congrats! You're all set up!")
            else:
                self.status.config(text="You're set up but I don't think you're connected to the Internet")

    # Checks if user is already set up
    def check_txt(self):
        try:
            checking = open(path + "\DiscRead\Info.txt", 'r')
            checking.close()
            return True
        except FileNotFoundError:
            return False

    # Writes results to Info.txt. Not encrypted
    def write_results(self):
        text = self.first_name + '\n' + self.first_discipler + '\n' + self.address
        writing = open(path + "\DiscRead\Info.txt", 'w')
        writing.write(text)
        writing.close()

    # Check that email address is at least a feasible email address
    def is_good(self, address):
        if '@' not in address:
            return False
        elif len(address) < 7:
            return False
        elif address[-4] != '.':
            return False
        elif '..' in address:
            return False
        return True

    def daily(self):
        self.root.destroy()
        main()


# This is the GUI that runs daily on the user's computer. Again, very basic
class Daily:
    def __init__(self):
        self.answer = ""

        self.root = Tk()
        self.root.title("Disciple Reading")

        menu = Menu(self.root)
        self.root.config(menu=menu)
        menu.add_command(label='Help', command=help_menu)

        Label(self.root, text="Welcome to Disciple Reading!", font=("Helvetica", 16)).grid(row=0, padx=60, pady=40)

        Label(self.root, text="Have you ready your Bible today? (yes/no)"
                              "\n(Enter \"Setup\" to add email option").grid(row=1)
        self.entry = Entry(self.root)
        self.entry.grid(row=2)
        self.entry.bind("<Return>", self.submit)

        self.submit = Button(self.root, text="Submit", command=self.submit)
        self.submit.grid(row=5, padx=10, pady=10)

        self.status = Label(self.root, text="")
        self.status.grid(row=99, padx=10, pady=10)

        self.root.mainloop()

    # Collects user input
    def submit(self, *args):
        self.status.config(text="Submitting...")
        self.answer = self.entry.get().title()
        if self.answer == "Setup":
            self.status.config(text="Loading setup menu")
            self.root.destroy()
            Setup()
            return
        elif self.answer == "Remove" or self.answer == "Uninstall":
            uninstall()
            return
        elif self.answer == "Yes":
            self.status.config(text="Good Job!")
        elif self.answer == "No":
            self.status.config(text="Too bad :(")
        else:
            self.status.config(text="That is not a valid option!")
            return

        self.write_info()
        sys.exit(0)

    # Writes updated info to Results.txt
    def write_info(self):
        text = decr_res()
        encr_res(text + get_date() + " " + self.answer + '\n')


# Where the execution of script starts. If the program is already in the right spot, it continues. Else it corrects
# the location and prompts the user to set up the Info.txt and ends. Then if the program has not been run today yet
# then it continues to ask the user if they've read their Bible yet and checks the date for mailing results.
def main():
    added = check_path()
    if added == 0:
        Tk().withdraw()
        messagebox.showinfo("Thanks!", "You're all set up! Next time you turn on your computer you will be asked "
                                       "if you'va read your Bible. Be sure to enter 'Setup' to mail your results!")
    elif check_day():
        Daily()
        mail_results()
    sys.exit(0)

# A Pythonic formality
if __name__ in "__main__":
    main()
