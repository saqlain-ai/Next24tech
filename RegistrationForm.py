import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import webbrowser
import datetime

def signup():
    full_name = name_entry.get()
    email = email_entry.get()
    dob = dob_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()

    if not validate_email(email):
        messagebox.showerror("Error", "Invalid email format.")
        return
    
    if not validate_dob(dob):
        messagebox.showerror("Error", "Invalid date of birth format. Please use YYYY-MM-DD.")
        return
    
    if not (full_name and email and dob and password and confirm_password):
        messagebox.showerror("Error", "Please fill in all fields.")
        return
    
    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match.")
        return

    messagebox.showinfo("Success", "Sign up successful!")

def validate_email(email):
    if "@" in email and "." in email:
        return True
    else:
        return False

def validate_dob(dob):
    try:
        datetime.datetime.strptime(dob, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def open_url(url):
    webbrowser.open_new(url)

def signup_with_google():
    google_oauth_url = "https://accounts.google.com/o/oauth2/auth?client_id=YOUR_CLIENT_ID&redirect_uri=YOUR_REDIRECT_URI&response_type=code&scope=email%20profile"
    open_url(google_oauth_url)

def signup_with_facebook():
    facebook_oauth_url = "https://www.facebook.com/v13.0/dialog/oauth?client_id=YOUR_CLIENT_ID&redirect_uri=YOUR_REDIRECT_URI&scope=email"
    open_url(facebook_oauth_url)

window = tk.Tk()
window.title("REGISTRATION FORM")
window.geometry('480x480')  
window.configure(bg='#FFFDD0')


try:
    logo_image = Image.open(r"C:\Users\LENOVO\OneDrive\Desktop\python.vscode\first project\CORPORATE6585796c2870f1703246188.png")
    logo = ImageTk.PhotoImage(logo_image)
except FileNotFoundError:
    messagebox.showerror("Error", "Logo image file not found.")
    window.destroy()
    exit()

frame = tk.Frame(window, bg='#FFFDD0')

logo_label = tk.Label(frame, image=logo, bg='#FFFDD0')
name_label = tk.Label(frame, text="Full Name", bg='#FFFDD0', font=("Arial", 16))
name_entry = tk.Entry(frame, font=("Arial", 16))
email_label = tk.Label(frame, text="Email", bg='#FFFDD0', font=("Arial", 16))
email_entry = tk.Entry(frame, font=("Arial", 16))
dob_label = tk.Label(frame, text="D.O.B", bg='#FFFDD0', font=("Arial", 16))
dob_entry = tk.Entry(frame, font=("Arial", 16))
password_label = tk.Label(frame, text="Password", bg='#FFFDD0', font=("Arial", 16))
password_entry = tk.Entry(frame, show='*', font=("Arial", 16))
confirm_password_label = tk.Label(frame, text="Confirm Password", bg='#FFFDD0', font=("Arial", 16))
confirm_password_entry = tk.Entry(frame, show='*', font=("Arial", 16))
sign_up_button = tk.Button(frame, text="Sign Up", bg="#00FFFF", fg="#333333", font=("Arial", 16), command=signup)
google_button = tk.Button(frame, text="Sign in with Google", bg="#FFFFFF", fg="#000000", font=("Arial", 12), command=signup_with_google)
facebook_button = tk.Button(frame, text="Sign in with Facebook", bg="#3B5998", fg="#FFFFFF", font=("Arial", 12), command=signup_with_facebook)

logo_label.grid(row=0, column=0, columnspan=2, sticky='news', pady=40)
name_label.grid(row=1, column=0, pady=10)
name_entry.grid(row=1, column=1, pady=5)
email_label.grid(row=2, column=0, pady=10)
email_entry.grid(row=2, column=1, pady=5)
dob_label.grid(row=3, column=0, pady=10)
dob_entry.grid(row=3, column=1, pady=5)
password_label.grid(row=4, column=0, pady=10)
password_entry.grid(row=4, column=1, pady=5)
confirm_password_label.grid(row=5, column=0, pady=10)
confirm_password_entry.grid(row=5, column=1, pady=5)
sign_up_button.grid(row=6, column=0, pady=10, columnspan=2, sticky='we')
google_button.grid(row=7, column=0, pady=10, columnspan=2, sticky='we')
facebook_button.grid(row=8, column=0, pady=10, columnspan=2, sticky='we')

frame.pack()
window.mainloop()
