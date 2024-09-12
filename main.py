from customtkinter import *
import tkinter as tk

# Create the main window
app = tk.Tk()
app.configure(bg='#B0E0A8')
app.title("Example")
app.geometry('600x400')


# Define the start game function
def start_game():
    print("Game started!")  # Replace with your game starting logic
    frame1.pack_forget()


frame1 = CTkFrame(app , bg='#446A46')
frame1.pack()
# Create the button with CustomTkinter
button = CTkButton(
    frame1,
    text="Start Game!",
    text_color='#446A46',
    height= 60,
    width= 200 ,
    command=start_game,
    fg_color="#FCC2FC",  # Button background color
    corner_radius= 15,
    border_width= 2,
    border_color= '#71A95A',
    font=("BIPs", 20 , 'bold') , # Font and size
    hover_color = '#FEB9C8'
)

button.place(relx= 0.5 , rely= 0.5 ,anchor= 'center' )

# Run the main loop
app.mainloop()
