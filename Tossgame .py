#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image, ImageTk  # You need to install Pillow: pip install Pillow

def toss_coin():
    # Get user's choice (H for heads, T for tails)
    user_choice = choice_var.get()

    # Simulate the coin toss
    toss_result = random.choice(['H', 'T'])

    # Display the corresponding image
    if toss_result == 'H':
        result_image.config(image=heads_image)
    else:
        result_image.config(image=tails_image)

    # Check if the user won
    if user_choice == toss_result:
        messagebox.showinfo("Result", "You win!")
    else:
        messagebox.showinfo("Result", "You lose!")

# Initialize the window
window = tk.Tk()
window.title("Coin Toss Game")

# Variable to store the user’s choice
choice_var = tk.StringVar()

# Load the images for heads and tails
heads_img = Image.open("heads.png")
tails_img = Image.open("tails.png")

# Resize the images (optional)
heads_img = heads_img.resize((150, 150), Image.LANCZOS)
tails_img = tails_img.resize((150, 150), Image.LANCZOS)

# Convert images to PhotoImage
heads_image = ImageTk.PhotoImage(heads_img)
tails_image = ImageTk.PhotoImage(tails_img)

# Create a label to display the coin toss result (default: heads image)
result_image = tk.Label(window, image=heads_image)
result_image.pack(pady=20)

# Create buttons for heads and tails choices
heads_button = tk.Radiobutton(window, image=heads_image ,text="Heads", variable=choice_var, value='H',  indicatoron=0, height=150, width=150 , font=('Arial', 16))
heads_button.pack(side="left", padx=20)

tails_button = tk.Radiobutton(window, text="Tails",image=tails_image ,  variable=choice_var, value='T',  indicatoron=0, height=150, width=150 , font=('Arial', 16))
tails_button.pack(side="right", padx=20)

# Create a button to toss the coin
toss_button = tk.Button(window, text="Toss Coin", command=toss_coin, font=('Arial', 16))
toss_button.pack(pady=20)

# Run the GUI main loop
window.mainloop()


# In[13]:





# In[ ]:




