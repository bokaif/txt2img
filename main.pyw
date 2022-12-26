import tkinter as tk
from tkinter import filedialog, colorchooser
from PIL import Image, ImageDraw, ImageFont
import os
import textwrap
import webbrowser

def open_url(url):
   webbrowser.open_new_tab(url)
   
def about_window():
    popup = tk.Toplevel(root)
    popup.title("About")
    popup.geometry("195x80")
    popup.resizable(False, False)
    popup.iconphoto(False, tk.PhotoImage(file="assets/icon.png"))
    elem1 = tk.Label(popup, text="Text to Image Generator - v1.0\nMade by @bokaif")
    elem1.grid(row=0, column=0, padx=8, pady=(8, 2))
    elem2 = tk.Label(popup, text="Github", fg="#685ac4", cursor="hand2")
    elem2.grid(row=1, column=0, padx=0)
    elem2.bind("<Button-1>", lambda e: open_url("https://github.com/bokaif"))
    popup.update_idletasks()
    x = root.winfo_x() + root.winfo_width()//2 - popup.winfo_width()//2
    y = root.winfo_y() + root.winfo_height()//2 - popup.winfo_height()//2
    popup.geometry(f"+{x}+{y}")

def popup_window(title, text):
    popup = tk.Toplevel(root)
    popup.title(title)
    popup.geometry("150x40")
    popup.resizable(False, False)
    popup.iconphoto(False, tk.PhotoImage(file="assets/icon.png"))
    elem1 = tk.Label(popup, text=text)
    elem1.grid(row=0, column=0, padx=8, pady=(8, 2))
    popup.update_idletasks()
    x = root.winfo_x() + root.winfo_width()//2 - popup.winfo_width()//2
    y = root.winfo_y() + root.winfo_height()//2 - popup.winfo_height()//2
    popup.geometry(f"+{x}+{y}")
    popup.after(4000, popup.destroy)

def choose_color(color_type):
    color = colorchooser.askcolor()[1]
    if color_type == 'bg':
        bg_color = '#242424' if color is None else color
        bg_color_button.config(bg=bg_color, text=bg_color)
    else:
        text_color = '#685ac4' if color is None else color
        text_color_button.config(bg=text_color, text=text_color)

global font
font = None
def choose_font():
    font = filedialog.askopenfilename(filetypes=[("TrueType fonts", "*.ttf")])
    font_button.config(text=font.split("/")[-1])

def importTXT():
    mtext_entry.delete("1.0", "end-1c")
    mtext_entry.insert(tk.END, open(filedialog.askopenfilename(filetypes=[("Text files", "*.txt")]), "r").read())

def generate():
    root.update()
    bg_color = bg_color_button['bg']
    text_color = text_color_button['bg']
    mtext = mtext_entry.get("1.0", "end-1c")
    try:
        size = int(size_entry.get())
        width = int(width_entry.get())
        height = int(height_entry.get())
    except:
        popup_window("Error", "Invalid input")
        return
    if size < 2:
        popup_window("Error", "Text size is too small")
        return
    if width//size < 2 or height//size < 2:
        popup_window("Error", "Text size is too big")
        return
    else:
        generate_button.config(text="Generating...")
        generate_button.config(state="disabled")
        root.update()
        max_chars = (width // (size // 2))-2
        max_lines = (height // size)-1
        lines = textwrap.wrap(mtext, max_chars)
        folder_name = "Output"
        os.makedirs(folder_name, exist_ok=True)

        for file in os.listdir(folder_name):
            os.remove(os.path.join(folder_name, file))

        i = 1
        while lines:
            x, y = 4, 4
            img = Image.new('RGB', (width, height), color=bg_color)
            d = ImageDraw.Draw(img)
            if font:
                fnt = ImageFont.truetype(font, size)
            else:
                fnt = ImageFont.truetype("assets/OpenSans-Regular.ttf", size)
            for line in lines[:max_lines]:
                d.text((x, y), line, fill=text_color, font=fnt)
                y += size
            img.save(f'{folder_name}/{i}.jpg')
            i += 1
            lines = lines[max_lines:]
        popup_window("Success", "Images generated")
    generate_button.config(text="Generate")
    generate_button.config(state="normal")
    root.update()

root = tk.Tk()
root.geometry("380x334")
root.resizable(False, False)
root.iconphoto(False, tk.PhotoImage(file="./assets/icon.png"))
root.title("txt2img")
root.config(bg="#171717")

root.option_add("*background", "#171717")
root.option_add("*foreground", "white")
root.option_add("*Font", "OpenSans-Regular 10")

widgets = ["Button", "Entry", "Text"]

for widget in widgets:
    if widget == "Button":
        root.option_add(f"*{widget}.background", "#685ac4")
        root.option_add(f"*{widget}.highlightThickness", 0)
    else:
        root.option_add(f"*{widget}.background", "#171717")
        root.option_add(f"*{widget}.highlightThickness", 1)
    root.option_add(f"*{widget}.foreground", "white")
    root.option_add(f"*{widget}.highlightColor", "#685ac4")
    root.option_add(f"*{widget}.highlightBackground", "#685ac4")
    root.option_add(f"*{widget}.relief", "flat")
    root.option_add(f"*{widget}.borderWidth", 0)
    root.option_add(f"*{widget}.focusColor", "#685ac4")
    root.option_add(f"*{widget}.focusRelief", "flat")
    root.option_add(f"*{widget}.focusWidth", 0)
    root.option_add(f"*{widget}.selectColor", "#685ac4")
    root.option_add(f"*{widget}.selectRelief", "flat")
    root.option_add(f"*{widget}.selectBorderWidth", 0)
    root.option_add(f"*{widget}.selectForeground", "white")
    root.option_add(f"*{widget}.selectBackground", "#685ac4")
    root.option_add(f"*{widget}.insertWidth", 1)
    root.option_add(f"*{widget}.insertBorderWidth", 0)
    root.option_add(f"*{widget}.insertOffTime", 0)
    root.option_add(f"*{widget}.insertOnTime", 0)
    root.option_add(f"*{widget}.insertUnfocussed", "none")
    root.option_add(f"*{widget}.insertBackground", "white")

menu = tk.Menu(root)
root.config(menu=menu)

import_menu = tk.Menu(menu, tearoff=0)
menu.add_command(label="Import", command=importTXT)

about_menu = tk.Menu(menu, tearoff=0)
menu.add_command(label="About", command=about_window)

bg_color_label = tk.Label(root, text="Background Color:")
bg_color_button = tk.Button(root, bg="#242424", text="#242424", command=lambda: choose_color('bg'), width=30, height=1)
text_color_label = tk.Label(root, text="Text Color:")
text_color_button = tk.Button(root, bg="#685ac4", text="#685ac4", command=lambda: choose_color('text'), width=30, height=1)

mtext_label = tk.Label(root, text="Text:")
mtext_entry = tk.Text(root, height=5, width=34)

size_label = tk.Label(root, text="Font Size (px):")
size_entry = tk.Entry(root, width=34)
width_label = tk.Label(root, text="Image Width (px):")
width_entry = tk.Entry(root, width=34)
height_label = tk.Label(root, text="Image Height (px):")
height_entry = tk.Entry(root, width=34)
font_label = tk.Label(root, text="Font:")
font_button = tk.Button(root, text="assets/OpenSans-Regular.ttf", command=choose_font, width=30, height=1)
generate_button = tk.Button(root, text="Generate", command=generate, width=46, height=2, bg="#685ac4", fg="white")

bg_color_label.grid(row=0, column=0, padx=4, pady=(5, 0), sticky="e")
bg_color_button.grid(row=0, column=1, padx=4, pady=(5, 0), sticky="w")
text_color_label.grid(row=1, column=0, padx=4, pady=(5, 0), sticky="e")
text_color_button.grid(row=1, column=1, padx=4, pady=(5, 0), sticky="w")
mtext_label.grid(row=2, column=0, padx=4, pady=(5, 0), sticky="e")
mtext_entry.grid(row=2, column=1, padx=4, pady=(5, 0), sticky="w")
size_label.grid(row=3, column=0, padx=4, pady=(5, 0), sticky="e")
size_entry.grid(row=3, column=1, padx=4, pady=(5, 0), sticky="w")
width_label.grid(row=4, column=0, padx=4, pady=(5, 0), sticky="e")
width_entry.grid(row=4, column=1, padx=4, pady=(5, 0), sticky="w")
height_label.grid(row=5, column=0, padx=4, pady=(5, 0), sticky="e")
height_entry.grid(row=5, column=1, padx=4, pady=(5, 0), sticky="w")
font_label.grid(row=6, column=0, padx=4, pady=(5, 0), sticky="e")
font_button.grid(row=6, column=1, padx=4, pady=(5, 0), sticky="w")
generate_button.grid(row=7, column=0, padx=4, pady=(20, 5), columnspan=2)

root.mainloop()