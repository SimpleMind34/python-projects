import tkinter as tk #for the logic
#  from tkinter import ttk #for the widgets
import ttkbootstrap as ttk

def convert():
  print(entry.get())
  #number = entry_int.get() 
  number = entry.get()
  if number.isdigit():
    
    converted_mile = int(number) * 1.60934
    print(converted_mile)
    # output_label.config(text=str(converted_mile) + ' Kilometers',font='Elephant 20',foreground='black')
    output_string.set(str(converted_mile) + ' Kilometers')
  else: 
    # output_label.config(text='Please insert a number', foreground='red',font='Arial 10 bold')
    output_string.set('Please enter a digit')
# creating a window
window = ttk.Window(themename="journal") 
#we can change the title of the window like this
window.title('Miles converter')
#set the size of the window
window.geometry('300x200') #width*height
#creating widgets
  # creating the titles
title_label = ttk.Label(master=window,text = 'Miles to kilometers', font = 'Calibri 24 bold') #the master is the container
#placing the label in the window
title_label.pack()
# creating input fields
#frame
input_frame = ttk.Frame(master=window)
#entry
entry_int = tk.IntVar()
entry = ttk.Entry(master=input_frame,textvariable=entry_int)
#button
button = ttk.Button(master=input_frame, text = 'Convert', command= convert )
entry.pack(side='left',padx=5,pady=5)
button.pack(side='left')
input_frame.pack(pady=10)
output_string = tk.StringVar()
output_label = ttk.Label(master=window,text='Output',font=('Elephant',16),textvariable=output_string)
output_label.pack(pady=5)

#to run the app we need to call the main loop method
window.mainloop()