import os
import sys
from tkinter import *
from tkinter import ttk
from bober_lob import Bober
import webbrowser

def main():
   root = Tk()    
   root.title("BoberLob")     
   root.geometry("250x300")    
   
   if getattr(sys, 'frozen', False):
      application_path = sys._MEIPASS
   elif __file__:
      application_path = os.path.dirname(__file__)

   iconFile = "BoberLobIco.ico"
   root.iconbitmap(default=os.path.join(application_path, iconFile))
   root.resizable(False, False)
   root.configure(bg='grey')

   status_label = Label(
      root, 
      text="Статус: Ожидание", 
      font=("Helvetica", 12, "bold"), 
      bg='grey', 
      fg='black' 
   )
   status_label.pack(pady=20)
   github_url = "https://github.com/Progress-ux/AntiAfk.git"

   def open_github_url(event):
      webbrowser.open_new(github_url)

   info_label = Label(
      root,
      text=f"Posted by Progress",
      font=("Helvetica", 8, "underline"), 
      bg='grey', 
      fg='blue',                          
      cursor="hand2"                      
   )
   info_label.bind("<Button-1>", open_github_url)
   info_label.pack(side="bottom", anchor='se', pady=10, padx=10)

   bober = Bober(label=status_label)
   
   button_frame = ttk.Frame(root)
   button_frame.pack(pady=10)

   btn = ttk.Button(
      button_frame, 
      text="Старт/Стоп", 
      command=bober.toggle 
   )
   btn.pack()

   def on_closing():
      bober.running = False 
      root.destroy()

   root.protocol("WM_DELETE_WINDOW", on_closing)
   root.mainloop()

if __name__ == "__main__":
   main()