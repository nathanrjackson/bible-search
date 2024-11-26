import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Bible Search")
root.geometry("400x300")

# Add a label
label = tk.Label(root, text="Welcome to Bible Search!", font=("Arial", 16))
label.pack()

# Add an entry field for name
entry = tk.Entry(root)
entry.pack()

# Update label to include name
def update_label():
    label.config(text=f"Hello, {entry.get()}!")

# Add a button
button = tk.Button(root, text="Submit", command=update_label)
button.pack()

# Run the application
root.mainloop()
