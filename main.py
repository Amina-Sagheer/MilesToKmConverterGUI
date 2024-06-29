import tkinter as tk


def display():
    """
    Takes in teh user_input value and converts it into kilo_meters. Then prints the output statement with the
    distance value in miles.
    :return:
    None
    """
    value = user_input.get()
    result = float(value) * (8 / 5)
    text.delete(1.0, tk.END)  # Clear previous text
    text.insert(tk.END, f"The distance in kilometers is {result:.2f}")


# Initialize the main window
window = tk.Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=500, height=400)
window.config(bg="lightblue")

# Create a label to prompt the user
label = tk.Label(window, text="Enter the distance in miles")
label.pack(pady=10)

# Create an entry widget for user input
user_input = tk.Entry(window)
user_input.pack(pady=10)

# Create a button that triggers the conversion
button = tk.Button(window, text="Click me", command=display)
button.pack(pady=10)

# Create a Text widget to display the result
text = tk.Text(height=5, width=40)
text.pack()

window.mainloop()