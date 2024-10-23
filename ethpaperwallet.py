import os
from eth_keys import keys
import qrcode
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageGrab
from mnemonic import Mnemonic
from pathlib import Path

def generate_keys():
    # Step 1: Generate a Private Key
    private_key = os.urandom(32).hex()
    private_key_bytes = bytes.fromhex(private_key)
    private_key_obj = keys.PrivateKey(private_key_bytes)
    public_key = private_key_obj.public_key
    public_address = public_key.to_checksum_address()

    # Step 2: Generate a Seed Phrase
    mnemo = Mnemonic("english")
    seed_phrase = mnemo.generate(strength=256)  # 256 bits for a 24-word seed phrase

    # Display the keys and seed phrase
    private_key_text.config(state=tk.NORMAL)
    private_key_text.delete(1.0, tk.END)
    private_key_text.insert(tk.END, private_key)
    private_key_text.config(state=tk.DISABLED)

    public_address_text.config(state=tk.NORMAL)
    public_address_text.delete(1.0, tk.END)
    public_address_text.insert(tk.END, public_address)
    public_address_text.config(state=tk.DISABLED)

    seed_phrase_text.config(state=tk.NORMAL)
    seed_phrase_text.delete(1.0, tk.END)
    seed_phrase_text.insert(tk.END, seed_phrase)
    seed_phrase_text.config(state=tk.DISABLED)

    # Step 3: Generate QR codes for the private key and public address
    private_qr = qrcode.make(private_key)
    public_qr = qrcode.make(public_address)

    # Resize QR codes to a smaller size using Image.LANCZOS
    private_qr = private_qr.resize((150, 150), Image.LANCZOS)
    public_qr = public_qr.resize((150, 150), Image.LANCZOS)

    # Convert QR codes to images that can be displayed in tkinter
    private_qr_img = ImageTk.PhotoImage(private_qr)
    public_qr_img = ImageTk.PhotoImage(public_qr)

    # Update the labels to show the QR codes
    private_qr_label.config(image=private_qr_img)
    private_qr_label.image = private_qr_img  # Keep a reference to avoid garbage collection
    public_qr_label.config(image=public_qr_img)
    public_qr_label.image = public_qr_img  # Keep a reference to avoid garbage collection

    # Display success message
    messagebox.showinfo("Success", "Keys, seed phrase, and QR codes generated successfully.")

def save_as_jpg():
    # Temporarily hide the buttons
    button_frame.pack_forget()

    # Update the GUI to reflect changes
    root.update_idletasks()

    # Calculate the coordinates of the area to capture
    x = root.winfo_rootx() + frame.winfo_x()
    y = root.winfo_rooty() + frame.winfo_y()
    width = frame.winfo_width()
    height = frame.winfo_height()

    # Capture the specified area of the Tkinter window
    image = ImageGrab.grab(bbox=(x, y, x + width, y + height))

    # Scale the image to a higher resolution
    scale_factor = 3  # Increase the scale factor for better print quality
    new_size = (width * scale_factor, height * scale_factor)
    image = image.resize(new_size, Image.LANCZOS)

    # Construct the path to the desktop
    desktop_path = Path.home() / "Desktop" / "paper_wallet.jpg"

    # Save the image to the desktop with higher DPI and maximum quality
    image.save(desktop_path, dpi=(300, 300), quality=100)

    # Show the buttons again
    button_frame.pack(side=tk.BOTTOM, pady=10)

    # Display success message
    messagebox.showinfo("Saved", f"Screen saved as {desktop_path}")

# Create the main window
root = tk.Tk()
root.title("Ethereum Paper Wallet")
root.geometry("595x842")  # A4 aspect ratio in pixels (approximately 1:1.414)

# Add a frame for better layout management
frame = tk.Frame(root, padx=20, pady=20, bg='white')  # Set a background color for contrast
frame.place(x=0, y=0, relwidth=1, relheight=1)

# Create a separate frame for the buttons
button_frame = tk.Frame(frame, bg='white')
button_frame.pack(side=tk.BOTTOM, pady=10)

# Create and place the generate button
generate_button = tk.Button(button_frame, text="Generate Keys", command=generate_keys, bg="#4CAF50", fg="white", font=("Arial", 14, "bold"))
generate_button.pack(side=tk.LEFT, padx=5)

# Create a save button
save_button = tk.Button(button_frame, text="Save as JPG", command=save_as_jpg, bg="#FF5722", fg="white", font=("Arial", 14, "bold"))
save_button.pack(side=tk.LEFT, padx=5)

# Label and text widget for the private key
private_key_label = tk.Label(frame, text="Private Key:", font=("Arial", 12, "bold"), bg='white')
private_key_label.pack(pady=2)
private_key_text = tk.Text(frame, height=2, wrap='word', font=("Courier", 12), relief="solid", borderwidth=1, bg='white')
private_key_text.pack(pady=5, fill='x')
private_key_text.config(state=tk.DISABLED)

# Add a warning label for the private key
private_key_warning = tk.Label(frame, text="WARNING: Keep your private key secure and never share it!", fg="red", font=("Arial", 10, "bold"), bg='white')
private_key_warning.pack(pady=2)

# Label and text widget for the public address
public_address_label = tk.Label(frame, text="Public Address:", font=("Arial", 12, "bold"), bg='white')
public_address_label.pack(pady=2)
public_address_text = tk.Text(frame, height=2, wrap='word', font=("Courier", 12), relief="solid", borderwidth=1, bg='white')
public_address_text.pack(pady=5, fill='x')
public_address_text.config(state=tk.DISABLED)

# Label and text widget for the seed phrase
seed_phrase_label = tk.Label(frame, text="Seed Phrase:", font=("Arial", 12, "bold"), bg='white')
seed_phrase_label.pack(pady=2)
seed_phrase_text = tk.Text(frame, height=4, wrap='word', font=("Courier", 12), relief="solid", borderwidth=1, bg='white')
seed_phrase_text.pack(pady=5, fill='x')
seed_phrase_text.config(state=tk.DISABLED)

# Create labels to display the QR codes
private_qr_label = tk.Label(frame, relief="solid", borderwidth=1, bg='white')
private_qr_label.pack(pady=5)

private_qr_explanation = tk.Label(frame, text="Scan to reveal Private Key", font=("Arial", 10), bg='white')
private_qr_explanation.pack(pady=2)

public_qr_label = tk.Label(frame, relief="solid", borderwidth=1, bg='white')
public_qr_label.pack(pady=5)

public_qr_explanation = tk.Label(frame, text="Scan to reveal Public Address", font=("Arial", 10), bg='white')
public_qr_explanation.pack(pady=2)

# Run the application
root.mainloop()
