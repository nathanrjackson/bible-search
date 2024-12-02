import tkinter as tk
from tkinter import ttk
import csv


def main():
    # Create the main window
    root = tk.Tk()
    root.title("Bible Search")
    root.geometry("800x600")

    # Add a welcome message and short description
    welcome = tk.Label(root, text="Welcome to Bible Search!", font=("Arial", 16))
    desc = tk.Label(root, text="Enter keyword or phrase below", font=("Arial", 16))
    welcome.pack()
    desc.pack()

    # Add an entry field for name
    entry = tk.Entry(root)
    entry.pack()


    # Function to update the UI
    def update_label(entry, submit_button):
        # Get the text from the entry before destroying the widgets
        user_input = entry.get()
        
        # Destroy the button
        submit_button.destroy()

        # Clear all widgets
        scriptures = find_scripture(user_input)
        
        if len(scriptures) == 1:
            presentation_text = "Here is your scripture:"
        elif len(scriptures) > 1:
            presentation_text = "Here are your scriptures:"
        else:
            presentation_text = "No scriptures found"

        presentation_text = tk.Label(root, text=presentation_text, font=("Arial", 14), wraplength=600)
        presentation_text.pack()
        
        for scripture in scriptures:
            # Add a new label with personalized text
            new_label = tk.Label(root, text=scripture, font=("Arial", 14), wraplength=600)
            new_label.pack()
        
        # Add a "Search Again" button
        search_again_button = tk.Button(root, text="Search Again", command=reset_ui)
        search_again_button.pack()


    # Function to reset the UI
    def reset_ui():
        # Clear all widgets
        for widget in root.winfo_children():
            widget.destroy()
        
        # Recreate the original UI
        # global welcome, desc, entry
        welcome = tk.Label(root, text="Welcome to Bible Search!", font=("Arial", 16))
        desc = tk.Label(root, text="Enter keyword or phrase below", font=("Arial", 16))
        welcome.pack()
        desc.pack()

        new_entry = tk.Entry(root)
        new_entry.pack()

        button = tk.Button(root, text="Submit", command=lambda: update_label(new_entry, button))
        button.pack()


    # Add a button
    button = tk.Button(root, text="Submit", command=lambda: update_label(entry, button))
    button.pack()

    # Run the application
    root.mainloop()


def find_scripture(user_input):
    VERSE_ID_INDEX = 0
    BOOK_NAME_INDEX = 1
    BOOK_NUMBER_INDEX = 2
    CHAPTER_INDEX = 3
    VERSE_INDEX = 4
    TEXT_INDEX = 5
    
    requested_scriptures = []

    scriptures = read_csv_file("kjv.csv")

    for scripture in scriptures:
        if user_input.lower() in scripture[TEXT_INDEX].lower():
            requested_scriptures.append(scripture[TEXT_INDEX])
    
    return requested_scriptures


def read_csv_file(filename):
    scriptures = []
    
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)

        next(reader)

        for line in reader:
            scriptures.append(line)

        return scriptures


if __name__ == "__main__":
    main()
