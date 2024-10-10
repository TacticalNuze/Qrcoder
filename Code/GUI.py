import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
import os
from Code.Qrcoder import Qr_png  # Ensure this is imported correctly


def browse_directory():
    # Open a directory dialog to select a folder
    folder_path = filedialog.askdirectory()
    if folder_path:
        directory_entry.delete(0, tk.END)
        directory_entry.insert(0, folder_path)

def confirm_action():
    directory = directory_entry.get()
    filename = filename_entry.get()

    if directory and filename:
        # Combine the directory and filename to create the full path
        full_path = os.path.join(directory,filename)
        messagebox.showinfo("Confirmation", f"File will be created at:\n{full_path}")
        return full_path
    else:
        messagebox.showwarning("Warning", "Please provide both the directory and filename!")
        return None

def generate_and_display_qr_png():
    # Get the full path where the image will be saved
    full_path = confirm_action()
    if full_path:
        # Generate the QR code image using the Qr_png function
        if data_entry.get():
            img = Qr_png(data_entry.get())  # Assuming this returns the path to the QR code image
            
            # Save the QR code image to the specified location
            img.save(f"{full_path}.png")
            
            # Display the image in the Tkinter window
            tk_image = ImageTk.PhotoImage(img)
            image_label.config(image=tk_image)
            image_label.image = tk_image  # Keep a reference to avoid garbage collection
        else:
            messagebox.showwarning("Warning", "Please provide an URL for the QR code")

def generate_and_display_qr_svg():
    # Get the full path where the image will be saved
    full_path = confirm_action()
    if full_path:
        # Generate the QR code image using the Qr_png function
        if data_entry.get():
            svg = Qr_svg(data_entry.get())  # Assuming this returns the path to the QR code image
            
            # Save the QR code image to the specified location
            svg.save(f"{full_path}.png")
            
            # Display the image in the Tkinter window
            tk_image = ImageTk.PhotoImage(img)
            image_label.config(image=tk_image)
            image_label.image = tk_image  # Keep a reference to avoid garbage collection
        else:
            messagebox.showwarning("Warning", "Please provide an URL for the QR code")

# Create the main window
root = tk.Tk()
root.title("File Creator")
root.geometry("400x500")

# Create a title label
title_label = tk.Label(root, text="Create a New File", font=("Arial", 16))
title_label.pack(pady=10)

# File destination input
directory_label = tk.Label(root, text="File Destination:")
directory_label.pack(pady=5)
directory_entry = tk.Entry(root, width=50)
directory_entry.pack(pady=5)

# Browse button for selecting a directory
browse_button = tk.Button(root, text="Browse", command=browse_directory)
browse_button.pack(pady=5)

# Filename input
filename_label = tk.Label(root, text="The QR code name:")
filename_label.pack(pady=5)
filename_entry = tk.Entry(root, width=50)
filename_entry.pack(pady=5)
# Data input
data_label = tk.Label(root, text="Url to be used:")
data_label.pack(pady=5)
data_entry = tk.Entry(root, width=50)
data_entry.pack(pady=5)
# Create button
create_button = tk.Button(root, text="Create", command=generate_and_display_qr)
create_button.pack(pady=20)

# Image label to display the QR code
image_label = tk.Label(root)
image_label.pack(pady=20)

# Start the main event loop
root.mainloop()
