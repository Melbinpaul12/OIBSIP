import tkinter as tk
import random
import string

def generate():
    try:
        length = int(length_entry.get())
        chars = string.ascii_letters + string.digits + "!@#$%^&*"
        pwd = ''.join(random.choice(chars) for _ in range(length))
        password.set(pwd)

        if length < 8:
            strength.set("WEAK")
            strength_label.config(fg="#c62828")
        elif length < 12:
            strength.set("MEDIUM")
            strength_label.config(fg="#f9a825")
        else:
            strength.set("STRONG")
            strength_label.config(fg="#2e7d32")
    except:
        password.set("Invalid Input")
        strength.set("ERROR")
        strength_label.config(fg="black")

# ---------------- Window ----------------
root = tk.Tk()
root.title("Password Generator")
root.geometry("420x380")
root.configure(bg="#f4f6f8")
root.resizable(False, False)

# ---------------- Card ----------------
card = tk.Frame(root, bg="white", bd=0)
card.place(relx=0.5, rely=0.5, anchor="center", width=360, height=340)

# ---------------- Title ----------------
tk.Label(
    card,
    text="Password Generator",
    bg="white",
    fg="#333",
    font=("Segoe UI", 18, "bold")
).pack(pady=15)

# ---------------- Length Section ----------------
tk.Label(card, text="Password Length", bg="white", fg="#555").pack(pady=(10, 5))

length_entry = tk.Entry(card, width=15, justify="center", font=("Segoe UI", 11))
length_entry.insert(0, "12")
length_entry.pack()

# ---------------- Button ----------------
tk.Button(
    card,
    text="GENERATE PASSWORD",
    command=generate,
    bg="#1976d2",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    relief="flat",
    width=22
).pack(pady=15)

# ---------------- Output ----------------
password = tk.StringVar()
strength = tk.StringVar()

tk.Entry(
    card,
    textvariable=password,
    font=("Consolas", 12),
    width=28,
    justify="center"
).pack(pady=10)

strength_label = tk.Label(
    card,
    textvariable=strength,
    bg="white",
    font=("Segoe UI", 14, "bold")
)
strength_label.pack(pady=5)

# ---------------- Footer ----------------
tk.Label(
    card,
    text="Use strong passwords for better security",
    bg="white",
    fg="#777",
    font=("Segoe UI", 9)
).pack(side="bottom", pady=10)

root.mainloop()
