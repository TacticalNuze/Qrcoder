import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
import os
from Qrcoder import Qr_png,Qr_svg # Ensure this is imported correctly


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

def generate_and_display_qr():
    # Get the full path where the image will be saved
    full_path = confirm_action()
    if full_path and format_var:
        # Generate the QR code image using the Qr_png function
        if data_entry.get():
            format=format_var.get()
            if  format in ["png","jpeg"]:
                img = Qr_png(data_entry.get())  # Assuming this returns the path to the QR code image
                # Save the QR code image to the specified location
                img.save(f"{full_path}.{format}")
            elif format_var.get()=="svg":
                img=Qr_svg(data_entry.get())
                # Save the QR code image to the specified location
                img.save(f"{full_path}.{format}")
            else:
                messagebox.showwarning("Warning", "No format received")
            # Display the image in the Tkinter window
            if format in ["png","jpeg"]:
                tk_image = ImageTk.PhotoImage(img)
                image_label.config(image=tk_image)
                image_label.image = tk_image  
        else:
            messagebox.showwarning("Warning", "Please provide an URL for the QR code")
    else:
        messagebox.showwarning("Warning", "Please provide a path for your QR code")



# Create the main window
root = tk.Tk()
root.title("Qr code generator")
root.geometry("400x500")

# Create a title label
title_label = tk.Label(root, text="Create a New File", font=("Calibri", 24))
title_label.pack(pady=10)

# File destination input
directory_label = tk.Label(root, text="File Destination:",font=("Calibri", 18))
directory_label.pack(pady=5)
directory_entry = tk.Entry(root, width=50)
directory_entry.pack(pady=5)

# Browse button for selecting a directory
browse_button = tk.Button(root, text="Browse", command=browse_directory)
browse_button.pack(pady=5)

# Filename input
filename_label = tk.Label(root, text="The QR code name:",font=("Calibri", 18))
filename_label.pack(pady=5)
filename_entry = tk.Entry(root, width=50)
filename_entry.pack(pady=5)
# Data input
data_label = tk.Label(root, text="Url to be used:",font=("Calibri", 18))
data_label.pack(pady=5)
data_entry = tk.Entry(root, width=50)
data_entry.pack(pady=5)
# File format selection using radio buttons
format_var = tk.StringVar()
format_var.set("png")  # Default format

format_label = tk.Label(root, text="Choose file format:")
format_label.pack(pady=10)

radio_png = tk.Radiobutton(root, text="PNG", variable=format_var, value="png")
radio_png.pack(anchor="w")

radio_jpeg = tk.Radiobutton(root, text="JPEG", variable=format_var, value="jpeg")
radio_jpeg.pack(anchor="w")

radio_svg = tk.Radiobutton(root, text="SVG", variable=format_var, value="svg")
radio_svg.pack(anchor="w")
# Create button
create_button = tk.Button(root, text="Create", command=generate_and_display_qr)
create_button.pack(pady=20)

# Image label to display the QR code
image_label = tk.Label(root)
image_label.pack(pady=20)

# Start the main event loop
root.mainloop()
