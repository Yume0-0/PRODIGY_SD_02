import customtkinter as ctk
import tkinter as tk
import random


root = tk.Tk()
root.title("Stylish Page Switch Example")
root.geometry("750x400")
root.configure(background='#365E32')
main_frame = ctk.CTkFrame(root, fg_color="#a0c888")
main_frame.pack(pady=20, padx=20, fill="both", expand=True)

# Second frame (Page 2) with another light
second_frame = ctk.CTkFrame(root, fg_color="#DDDDDD")
#random number :
random_num = None
#functions :
#generate a random number :
def generate() :
    global random_num
    random_num = random.randint(1,100)

#function to switch to the second frame
def switch_to_second_frame():
    main_frame.pack_forget()  # Hide the main frame
    second_frame.pack(pady=20, padx=20, fill="both", expand=True)  # Show the second frame
    root.configure(background= '#000000')
    generate()

#function to switch back to the main frame
def switch_to_main_frame():
    second_frame.pack_forget()  # Hide the second frame
    main_frame.pack(pady=20, padx=20, fill="both", expand=True)  # Show the main frame
    root.configure(background='#365E32')  # Main frame (Page 1) with a light background color
#function to restart :
def restart():
    result_text.set('')
    generate()

#function to guess :
def guess():
    global random_num
    gss = int(value.get())
    try:
        if (gss >= 0 and gss <= 100):
            if gss == random_num :
                result_text.set('YAAAY !! you made it Congrats , click restart to replay !')
            elif gss < random_num :
                result_text.set("too small")
            elif gss > random_num :
                result_text.set("too big")
        else:
            result_text.set('enter valid input plz')
    except ValueError:
        result_text.set('Please enter a valid number.')





start_button = ctk.CTkButton(
    main_frame,
    text="Start Game!",
    text_color='#FFFFFF',
    hover_color='#FF9BD2',
    height=60,
    width=200,
    command=switch_to_second_frame,
    fg_color="#F2C2CE",
    corner_radius=15,
    font=("Verdana", 20, "bold")
)
start_button.place(relx =0.5 , rely = 0.5 , anchor = 'center')

#welcome label
welcome_label = ctk.CTkLabel(
    main_frame,
    text="🎉 Welcome, Player! 🎉",
    text_color="#f1c2ce",
    corner_radius=10,    # Rounded corners to make it look more fun
    font=("Comic Sans MS", 26, "bold"),  # Goofy and playful font style
    width=300,
    height=50
)
welcome_label.pack(pady=50)

#game label
#to enter the guesses

value = tk.StringVar()
entry = ctk.CTkEntry(
    second_frame,
    text_color="white",
    width=300,
    height=30,
    font=("Verdana", 20),
    textvariable=value
    )
result_text = tk.StringVar()
reult = ctk.CTkLabel(second_frame , textvariable = result_text , text_color='black' ,
                     font=('Verdana' , 25 ),
                     )

buttons = ctk.CTkFrame(second_frame , fg_color='transparent')

back_button = ctk.CTkButton(
    buttons,
    text="Back to Main",
    text_color='#eeeeee',
    hover_color='#254F32',
    height=60,
    width=100,
    fg_color="#000000",
    corner_radius=15,
    border_width=2,
    border_color= '#AAB396',
    font=("Verdana", 20, "bold"),
    command=switch_to_main_frame
)

restart_button = ctk.CTkButton(
    buttons,
    text="Restart",
    text_color='#000000',
    hover_color='#D9BB25',
    height=60,
    width=100,
    fg_color="#ffffff",
    corner_radius=15,
    border_width=2,
    border_color='#AAB396',
    font=("Verdana", 20, "bold"),
    command=restart
)
guess_button = ctk.CTkButton(
    buttons,
    text="Guess",
    text_color='#eeeeee',
    hover_color='#254F32',
    height=60,
    width=100,
    fg_color="#000000",
    corner_radius=15,
    border_width=2,
    border_color= '#AAB396',
    font=("Verdana", 20, "bold"),
    command = guess
)

entry.pack(pady=30)
reult.pack(pady = 20)
back_button.pack(padx =5 , side = 'left')
restart_button.pack(padx = 5 , side = 'left')
guess_button.pack(padx = 5 , side = 'right')
buttons.place(relx =0.5 , rely = 0.5 , anchor = 'center')



root.mainloop()
