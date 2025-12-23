import tkinter as tk

def calculate():
    try:
        h = float(height.get()) / 100
        w = float(weight.get())
        bmi = w / (h * h)
        bmi_value.set(f"{bmi:.1f}")

        if bmi < 18.5:
            category.set("Underweight")
            tip.set("Increase calorie intake with healthy food.")
            result_label.config(fg="#1e88e5")
        elif bmi < 25:
            category.set("Normal")
            tip.set("Perfect! Keep maintaining your lifestyle.")
            result_label.config(fg="#2e7d32")
        elif bmi < 30:
            category.set("Overweight")
            tip.set("Add daily exercise & control diet.")
            result_label.config(fg="#f9a825")
        else:
            category.set("Obese")
            tip.set("Consult a doctor or nutritionist.")
            result_label.config(fg="#c62828")
    except:
        bmi_value.set("--")
        category.set("Invalid Input")
        tip.set("Please enter valid numbers")

# ---------------- Window ----------------
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("420x420")
root.configure(bg="#f4f6f8")
root.resizable(False, False)

# ---------------- Card ----------------
card = tk.Frame(root, bg="white", bd=0, relief="ridge")
card.place(relx=0.5, rely=0.5, anchor="center", width=360, height=360)

# ---------------- Title ----------------
tk.Label(
    card,
    text="BMI Calculator",
    bg="white",
    fg="#333",
    font=("Segoe UI", 18, "bold")
).pack(pady=15)

# ---------------- Input Section ----------------
input_frame = tk.Frame(card, bg="white")
input_frame.pack(pady=10)

tk.Label(input_frame, text="Height (cm)", bg="white").grid(row=0, column=0, padx=10, pady=8)
height = tk.Entry(input_frame, width=15)
height.grid(row=0, column=1)

tk.Label(input_frame, text="Weight (kg)", bg="white").grid(row=1, column=0, padx=10, pady=8)
weight = tk.Entry(input_frame, width=15)
weight.grid(row=1, column=1)

# ---------------- Button ----------------
tk.Button(
    card,
    text="CALCULATE",
    command=calculate,
    bg="#1976d2",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    relief="flat",
    width=20
).pack(pady=15)

# ---------------- Result ----------------
bmi_value = tk.StringVar(value="--")
category = tk.StringVar()
tip = tk.StringVar()

result_label = tk.Label(
    card,
    textvariable=bmi_value,
    bg="white",
    font=("Segoe UI", 32, "bold")
)
result_label.pack()

tk.Label(
    card,
    textvariable=category,
    bg="white",
    font=("Segoe UI", 14, "bold")
).pack(pady=5)

tk.Label(
    card,
    textvariable=tip,
    bg="white",
    fg="#555",
    wraplength=300,
    justify="center"
).pack(pady=10)

root.mainloop()
