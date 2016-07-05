import os
import platform
import ctypes
import shutil
import winshell
from win32com.client import Dispatch
from tkinter import Tk
import tkinter.messagebox
import sys

# This function will run first thing every time the program is executed. It first checks and makes sure the user is on
# a valid operating system, then checks and makes sure that the program itself is on the correct path (in Startup)
# Of course, if it's not, then it will be moved
def check_path():
    if platform.platform().startswith("Windows"):
        shortcut_path = os.getenv('APPDATA') + "\Microsoft\Windows\Start Menu\Programs"
        CSIDL_PERSONAL = 5  # My Documents
        SHGFP_TYPE_CURRENT = 0  # Get current, not default value
        buf = ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
        ctypes.windll.shell32.SHGetFolderPathW(None, CSIDL_PERSONAL, None, SHGFP_TYPE_CURRENT, buf)

        doc_path = buf.value + r"\DRead"
    else:
        raise OSError

    try:
        shutil.copytree(os.getcwd(), doc_path)
    except FileExistsError:
        pass

    desktop = winshell.desktop()
    path = os.path.join(desktop, "DiscipleReading.lnk")
    target = doc_path + r"\DiscipleReading.exe"
    wDir = doc_path
    icon = doc_path + r"\favicon.ico"

    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = target
    shortcut.WorkingDirectory = wDir
    shortcut.IconLocation = icon
    shortcut.save()
    root = Tk()
    root.withdraw()
    tkinter.messagebox.showinfo("Congrats!", "You're all set up! You'll\nfind a shortcut on your desktop")
    sys.exit(0)

