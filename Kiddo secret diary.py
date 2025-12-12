import tkinter as tk
from tkinter import messagebox
import os

DIARY_FILE = "secret_diary.txt"
KEY_FILE = "key.txt"

# Initialize key if not exists
if not os.path.exists(KEY_FILE):
    with open(KEY_FILE, "w") as f:
        f.write("1234")  # default key

def get_saved_key():
    with open(KEY_FILE, "r") as f:
        return f.read().strip()

def save_key(new_key):
    with open(KEY_FILE, "w") as f:
        f.write(new_key)

# Load diary
def load_diary():
    if os.path.exists(DIARY_FILE):
        with open(DIARY_FILE, "r", encoding="utf-8") as f:
            diary_box.insert(tk.END, f.read())

# Save diary
def save_entry():
    text = diary_box.get("1.0", tk.END).rstrip("\n")
    with open(DIARY_FILE, "w", encoding="utf-8") as f:
        f.write(text)
    messagebox.showinfo("Saved", "Your diary has been saved!")

# Check login key
def check_key():
    entered_key = key_entry.get().strip()
    if entered_key == get_saved_key():
        messagebox.showinfo("Access Granted", "Welcome to your secret diary!")
        login_frame.pack_forget()
        diary_frame.pack()
        load_diary()
    else:
        messagebox.showerror("Access Denied", "Incorrect key! Try again.")

# Change password
def change_password():
    old_key = old_key_entry.get().strip()
    new_key = new_key_entry.get().strip()
    if old_key == get_saved_key():
        if new_key == "":
            messagebox.showerror("Error", "New key cannot be empty!")
            return
        save_key(new_key)
        messagebox.showinfo("Success", "Password changed successfully!")
        old_key_entry.delete(0, tk.END)
        new_key_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Old password is incorrect!")

# ---------------- GUI ----------------
root = tk.Tk()
root.title("Kiddo Secret Diary - Key Access")
root.geometry("600x550")

# Login frame
login_frame = tk.Frame(root)
login_frame.pack(pady=50)

tk.Label(login_frame, text="Enter your secret key:", font=("Arial", 14)).pack(pady=10)
key_entry = tk.Entry(login_frame, font=("Arial", 14), width=15, show="*")
key_entry.pack(pady=5)
tk.Button(login_frame, text="Enter Diary", font=("Arial", 12), bg="#4CAF50", fg="white", command=check_key).pack(pady=10)

# Diary frame (hidden initially)
diary_frame = tk.Frame(root)

tk.Label(diary_frame, text="Your Secret Diary:", font=("Arial", 14)).pack(pady=5)
diary_box = tk.Text(diary_frame, height=20, width=70, font=("Courier", 12))
diary_box.pack(pady=10)

tk.Button(diary_frame, text="Save Diary", font=("Arial", 12), bg="#2196F3", fg="white", command=save_entry).pack(pady=5)

# Change password frame
tk.Label(diary_frame, text="Change Password:", font=("Arial", 12, "bold")).pack(pady=10)
tk.Label(diary_frame, text="Old Password:").pack()
old_key_entry = tk.Entry(diary_frame, show="*", width=15)
old_key_entry.pack(pady=2)

tk.Label(diary_frame, text="New Password:").pack()
new_key_entry = tk.Entry(diary_frame, show="*", width=15)
new_key_entry.pack(pady=2)

tk.Button(diary_frame, text="Change Password", font=("Arial", 12), bg="#FF9800", fg="white", command=change_password).pack(pady=5)

root.mainloop()
