import tkinter as tk
from tkinter import filedialog
from PIL import Image

def convert_dds_to_png():
    dds_file_path = filedialog.askopenfilename(filetypes=[("DDS files", "*.dds")])
    if dds_file_path:
        with Image.open(dds_file_path) as img:
            png_file_path = dds_file_path.rsplit(".", 1)[0] + ".png"
            img.save(png_file_path, "PNG")
            print("Conversion completed. PNG file saved at:", png_file_path)

root = tk.Tk()
root.title("DDS to PNG Converter")

convert_button = tk.Button(root, text="Convert DDS to PNG", command=convert_dds_to_png)
convert_button.pack(pady=10)

root.mainloop()
