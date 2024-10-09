import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import os

def browse_directory():
    # Open a directory dialog to select a folder
    folder_path = filedialog.askdirectory()
    # Set the folder path to the entry widget
    if folder_path:
        directory_entry.delete(0, tk.END)  # Clear the entry
        directory_entry.insert(0, folder_path)  # Insert the selected folder path

def confirm_action():
    directory = directory_entry.get()
    filename = filename_entry.get()

    if directory and filename:
        # Combine the directory and filename to create the full path
        full_path = os.path.join(directory, filename)
        messagebox.showinfo("Confirmation", f"File will be created at:\n{full_path}")
    else:
        messagebox.showwarning("Warning", "Please provide both the directory and filename!")

# Create the main window
root = tk.Tk()
root.title("File Creator")

# Set the window size
root.geometry("400x250")

# Create a title label
title_label = tk.Label(root, text="Create a New File", font=("Arial", 16))
title_label.pack(pady=10)

# Create a text entry field for the file destination
directory_label = tk.Label(root, text="File Destination:")
directory_label.pack(pady=5)
directory_entry = tk.Entry(root, width=50)
directory_entry.pack(pady=5)

# Create a browse button for selecting a directory
browse_button = tk.Button(root, text="Browse", command=browse_directory)
browse_button.pack(pady=5)

# Create a text entry field for the filename
filename_label = tk.Label(root, text="Filename:")
filename_label.pack(pady=5)
filename_entry = tk.Entry(root, width=50)
filename_entry.pack(pady=5)

# Create a create button
create_button = tk.Button(root, text="Create", command=confirm_action)
create_button.pack(pady=20)

# Start the main event loop
root.mainloop()
