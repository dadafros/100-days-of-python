import tkinter as tk

window = tk.Tk()
window.title("Mile to Kilometer Converter")
window.config(padx=20, pady=20)


def convert():
    tk.Label(text=f"{int(entry_box.get()) * 1.609}").grid(row=1, column=1)


entry_box = tk.Entry(width=8)
entry_box.grid(row=0, column=1)

label_miles = tk.Label(text="Miles")
label_miles.grid(row=0, column=2)

label_eq = tk.Label(text="is equal to")
label_eq.grid(row=1, column=0)

label_km = tk.Label(text="Km")
label_km.grid(row=1, column=2)

button = tk.Button(text="Convert", command=convert)
button.grid(row=2, column=1)

window.mainloop()
