from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    km_result_label.config(text=f"{km}")

# Window
window = Tk()
window.title("Miles to KM Calculator")
window.config(padx=15, pady=15)
    

# Miles
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
miles_input = Entry(width=12)
miles_input.grid(column=1, row=0)


# Equals
equal_label = Label(text="is equal to:")
equal_label.grid(column=0, row=1)


# Kilometers
km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)
km_label = Label(text="KM")
km_label.grid(column=2, row=1)


# Calculate
calc_button = Button(text="Calculate", command=miles_to_km)
calc_button.grid(column=1, row=2)


window.mainloop()