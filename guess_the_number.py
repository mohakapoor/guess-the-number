import random
from tkinter import *

def generate_num():
    global n
    n = random.randint(0,100)

def retry():
    v.config(text="")

def submit():
    
    if entry.get().isnumeric():
        guess = int(entry.get())
    else :
        status.config(text="Pls enter a valid Integer")
    if guess == n:
        v.config(text="You guessed it congrats")
        win()
    elif guess > n:
        status.config(text="Lower")    
    elif guess < n:
        status.config(text="Higher")    

def win():
    entry.delete(0,END)
    status.config(text="")
    generate_num()




window = Tk()

generate_num()

window.title("Guess the number")

window.geometry("420x420")
window.config(background="#424549")

label = Label(window,
              text="Guess A number between 0 and 100",
              fg="White",
              bg="#424549",
              font="Helvetica"

)
label.pack()

status = Label(window,
              text="",
              fg="White",
              bg="#424549",
              font="Helvetica"

)
status.pack(pady=10)


entry = Entry(window,
              font="Helvetica",
              
              
              )
entry.pack(pady=20)

v = Label(window,
              text="",
              fg="White",
              bg="#424549",
              font="Helvetica"

)
v.pack(pady=10)

submitButton = Button(window,
                      text="Submit",
                      command=submit,
                      
                      
                      
                      )
submitButton.place(x =150,y =200)

retryButton = Button(window,
                      text="Retry",
                      command=retry,
                      
                      
                      
                      )
retryButton.place(x =250,y =200)




window.mainloop()