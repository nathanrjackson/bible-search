import tkinter as tk
import csv

# # Create the main window
# root = tk.Tk()
# root.title("Bible Search")
# root.geometry("400x300")

# # Add a label
# label = tk.Label(root, text="Welcome to Bible Search!", font=("Arial", 16))
# label.pack()

# # Add an entry field for name
# entry = tk.Entry(root)
# entry.pack()

# # Update label to include name
# def update_label():
#     label.config(text=f"Hello, {entry.get()}!")

# # Add a button
# button = tk.Button(root, text="Submit", command=update_label)
# button.pack()

# # Run the application
# root.mainloop()


def main():
    VERSE_ID_INDEX = 0
    BOOK_NAME_INDEX = 1
    BOOK_NUMBER_INDEX = 2
    CHAPTER_INDEX = 3
    VERSE_INDEX = 4
    TEXT_INDEX = 5
    
    scriptures = read_csv_file("kjv.csv")

    for scripture in scriptures:
        if "potiphar" in scripture[TEXT_INDEX].lower():
            print(scripture[TEXT_INDEX])


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