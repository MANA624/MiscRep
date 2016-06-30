import sys
import shutil
import os
from tkinter import messagebox
from tkinter import Tk


def installer():
    if not sys.platform.startswith('win'):
        return

    import ctypes.wintypes
    import winshell
    from win32com.client import Dispatch

    CSIDL_PERSONAL = 5  # My Documents
    SHGFP_TYPE_CURRENT = 0  # Get current, not default value
    buf = ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
    ctypes.windll.shell32.SHGetFolderPathW(None, CSIDL_PERSONAL, None, SHGFP_TYPE_CURRENT, buf)

    full_path = buf.value + r"\Averager"
    if full_path == os.getcwd():
        return
    try:
        shutil.copytree(os.getcwd(), full_path)
    except FileExistsError:
        pass

    desktop = winshell.desktop()
    path = os.path.join(desktop, "Averager.lnk")
    target = full_path + r"\Averager.exe"
    wDir = full_path
    icon = full_path + r"\favicon.ico"

    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = target
    shortcut.WorkingDirectory = wDir
    shortcut.IconLocation = icon
    shortcut.save()
    root = Tk()
    root.withdraw()
    messagebox.showinfo("Congrats!", "You're all set up! You'll\nfind a shortcut on your desktop")
    sys.exit(0)


def main():
    installer()

if __name__ in "__main__":
    main()
