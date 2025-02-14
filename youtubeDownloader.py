import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk
from pytubefix import YouTube

def get_link():
  link = input_entry.get()
  format = selected_format.get()
  yt = YouTube(link, use_oauth=True, allow_oauth_cache=True)
  if(format == "High"):
    output_text.set(yt.title + " is downloading in high resolution...")
    yd = yt.streams.get_highest_resolution()
    if yd:
      yd.download('C:/Users/RYZEN/Videos/pytubed')
      output_text.set("Video downloaded successfully in C:/Users/RYZEN/Videos/pytubed")
  elif(format == "Low"):
    output_text.set(yt.title + " is downloading in Low resolution...")
    yd = yt.streams.get_lowest_resolution()
    if yd:
      yd.download('C:/Users/RYZEN/Videos/pytubed')
      output_text.set("Video downloaded successfully in C:/Users/RYZEN/Videos/pytubed")
  elif(format == "Audio"):
    output_text.set(yt.title + " is downloading in audio format...")
    yd = yt.streams.get_audio_only()
    if yd:
      yd.download('C:/Users/RYZEN/Videos/pytubed')
      output_text.set("Audio downloaded successfully in C:/Users/RYZEN/Videos/pytubed")

def cancel():
  quit()



window = ttk.Window(themename="darkly")
window.title('Youtube downloader')
window.geometry('500x500')

title_label = ttk.Label(master=window, text='Youtube video downloader', font=("JetBrains Mono ExtraBold",16,"bold"))
title_label.pack()
input_field = ttk.Frame(master=window)

input_entry = ttk.Entry(master=input_field)
input_button = ttk.Button(master=input_field,text="Submit", command=get_link)
selected_format = tk.StringVar(value="High")
radio1 = ttk.Radiobutton(master=window,text="High",variable=selected_format,value="High")
radio2 = ttk.Radiobutton(master=window,text="Low",variable=selected_format,value="Low")
radio3 = ttk.Radiobutton(master=window,text="Audio",variable=selected_format,value="Audio")

input_entry.pack(side='left',padx=5,pady=5)
input_button.pack(side='left')
input_field.pack(pady=10)
radio_label = ttk.Label(master=window,text="Please select a format (Default is High)")
radio_label.pack()
radio1.pack( padx=5,pady=5)
radio2.pack( padx=5,pady=5)
radio3.pack( padx=5,pady=5)
output_text = tk.StringVar()
output_label = ttk.Label(master=window,textvariable=output_text)
output_label.pack(padx=5,pady=5)
cancel_button = ttk.Button(master=window, text="Cancel", command=cancel)
cancel_button.pack(pady=5,padx=5)
#output_label = ttk.Label(master=window,text='Output',font='Mudir MT')

window.mainloop()