import tkinter as tk
from tkinter import filedialog
from tkinterdnd2 import DND_FILES, TkinterDnD
from PIL import Image
import uuid
import os

BG_COLOR = "#F3F3F3"
PRIMARY_COLOR = "#29ADB2"
SECONDARY_COLOR = "#9AD0C2"
# global variables
visible = False
images = []
watermark = None
percentage = 0.1
position = "bottom_right"

def drop(event):
    global images
    # Retrieve the file path of the dropped images
    file_paths = event.data
    list_file_paths = file_paths.split("} {")
    for file_path in list_file_paths:
        if file_path.strip("}{"):
            file_path = file_path.strip("}{")
            image = Image.open(file_path)
            images.append(image)
            image_message.config(text="image(s) added!")
        else:
            error_message.config(text="File not found\nIf you dropped multiple files please try to do one each time.")

def browse_image():
    global images
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif;*.jfif")])
    
    if file_path:
        image = Image.open(file_path)
        images.append(image)
        image_message.config(text="image added!")
        error_message.config(text="")
    else:
        error_message.config(text="File not found")

def browse_watermark():
    global watermark
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif;*.jfif")])
    if file_path:
        watermark = Image.open(file_path).convert("RGBA")
        watermark_message.config(text="watermark added!")
        error_message.config(text="")
    else:
        error_message.config(text="File not found")

def add_watermark():
    global watermark
    global images
    global percentage
    global position

    try:
        # Position the watermark
        for image in images:
            image_width = image.width
            image_height = image.height
            # save the watermark
            saved_watermark = watermark
            # Resize the watermark
            watermark_width = watermark.width
            watermark_height = watermark.height
            
            aspect_ratio = watermark_width / watermark_height
            new_height = int(image_height * percentage)
            new_width = int(new_height * aspect_ratio)

            watermark = watermark.resize((new_width,new_height), Image.NEAREST)

            if position == "bottom_right":
                x = image_width - new_width - 20
                y = image_height - new_height - 20
            elif position == "bottom_left":
                x = 20
                y = image_height - new_height - 20
            elif position == "top_right":
                x = image_width - new_width - 20
                y = 20
            elif position == "top_left":
                x = 20
                y = 20
            
            image.paste(watermark, (x,y), mask = watermark) 
            watermark = saved_watermark

            # Generate a unique name for the image
            unique_name = str(uuid.uuid4()) + ".png"
            save_folder = "./results"

            # Create the folder if it doesn't exist
            if not os.path.exists(save_folder):
                os.makedirs(save_folder)

            save_path = os.path.join(save_folder, unique_name)
            image.save(save_path)
            print(f"Image saved to: {save_path}")
        download_button.grid(row=17, column=1)
        reset_button.grid(row=17,column=2)
        error_message.config(text="")

    except AttributeError as e:
        error_message.config(text=f"Error: {e}")

def download():
    global images
    for image in images:
        file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                              filetypes=[("PNG files", "*.png"), ("All Files", "*.*")])
        try:
            image.save(file_path)
        except ValueError as e:
            error_message.config(text=f"Error: {e}")

def show_settings():
    global visible
    if visible == False:
        positions_label.grid(row=9,column=1, columnspan=2)
        top_left_option.grid(row=10,column=1)
        top_right_option.grid(row=10,column=2)
        bottom_left_option.grid(row=11,column=1)
        bottom_right_option.grid(row=11,column=2)
        size_label.grid(row=12,column=1, columnspan=2, pady=3)
        new_size.grid(row=13,column=1, columnspan=2)
        apply_button.grid(row=14,column=1,columnspan=2, pady=3)
        visible = True
    else: 
        positions_label.grid_forget()
        top_left_option.grid_forget()
        top_right_option.grid_forget()
        bottom_left_option.grid_forget()
        bottom_right_option.grid_forget()
        size_label.grid_forget()
        new_size.grid_forget()
        apply_button.grid_forget()
        visible = False

def apply_changes():
    global percentage
    global position

    position = new_position.get()
    if new_size.get() != '' :
        try:
            new_percentage = float(new_size.get())
            if new_percentage > 1 or new_percentage < 0 :
                raise ValueError
            percentage = new_percentage
            error_message.config(text="")
        except ValueError:
            error_message.config(text="Invalid input. The default size is applied!")
    print("Changes Applied!")
    applied_message.config(text="Changes Applied!")

def reset():
    global watermark
    global images
    global percentage
    global position
    global visible

    show_settings()
    images = []
    watermark = None
    percentage = 0.1
    position = "bottom_right"
    watermark_message.config(text="")
    image_message.config(text="")
    applied_message.config(text="")
    error_message.config(text="")
    download_button.grid_forget()
    reset_button.grid_forget()

main_window = TkinterDnD.Tk()
main_window.title("Add a watermark to your photos")
main_window.configure(bg=BG_COLOR)
main_window.geometry("400x660")
main_window.resizable(False, False)

main_window.drop_target_register(DND_FILES)
main_window.dnd_bind('<<Drop>>', drop)

# Main window elements
logo_image = tk.PhotoImage(file="logo.png")
canvas = tk.Canvas(main_window, width=160, height=160)
canvas.create_image(80, 80, image=logo_image)
canvas.grid(row=1, column=1, columnspan=2)

label1 = tk.Label(main_window,text="You can either drag and drop your image(s) \nhere or browse to upload it :",font=('SimSun', 12))
label1.grid(row=2, column=1, columnspan=2, pady=3,padx=20)

browse_button1 = tk.Button(main_window, text="Browse", command=browse_image,font=('SimSun', 10))
browse_button1.grid(row=3, column=1, columnspan=2)

image_message = tk.Label(main_window,text="",fg="green")
image_message.grid(row=4,column=1, columnspan=2)

label2 = tk.Label(main_window,text="Add your watermark here:\n(* you can only darg the images\n not the watermark!)",font=('SimSun', 12), width=45)
label2.grid(row=5, column=1, columnspan=2, pady=3,padx=20)

browse_button2 = tk.Button(main_window, text="Browse", command=browse_watermark,font=('SimSun', 10))
browse_button2.grid(row=6, column=1, columnspan=2)

watermark_message = tk.Label(main_window,text="",fg="green")
watermark_message.grid(row=7,column=1, columnspan=2)

# Settings
settings_button = tk.Button(main_window, text="Settings", command=show_settings,font=('SimSun', 10))
settings_button.grid(row=8,column=1, columnspan=2)

positions_label = tk.Label(main_window, text="Choose where to put the watermark:",font=('SimSun', 10))
new_position= tk.StringVar()
top_left_option = tk.Radiobutton(main_window, text="Top left",font=('SimSun', 10),variable=new_position, value="top_left")
top_right_option = tk.Radiobutton(main_window, text="Top right",font=('SimSun', 10),variable=new_position, value="top_right")
bottom_left_option = tk.Radiobutton(main_window, text="Bottom left",font=('SimSun', 10),variable=new_position, value="bottom_left")
bottom_right_option = tk.Radiobutton(main_window, text="Bottom right",font=('SimSun', 10),variable=new_position, value="bottom_right")
new_position.set("bottom_right")

size_label = tk.Label(main_window, text="Choose the size en percentage :\n* empty for default (0.1 eq 10%;\n the watermark is 10% the size of the image.)",font=('SimSun', 10))
new_size = tk.Entry(main_window, width=5)

apply_button = tk.Button(main_window, text="Apply", command=apply_changes,font=('SimSun', 10))
applied_message = tk.Label(main_window, text="", fg="green")
applied_message.grid(row=15, column=1, columnspan=2)

submit = tk.Button(main_window, text="Add Watermark", command=add_watermark, bg=PRIMARY_COLOR, fg=BG_COLOR,font=('Sika Text', 14))
submit.grid(row=16, column=1, columnspan=2, pady=5)

error_message = tk.Label(main_window,text="",fg="red")
error_message.grid(row=18,column=1, columnspan=2)

download_button = tk.Button(main_window, text="Download",width=10 , command=download, bg=SECONDARY_COLOR, fg=BG_COLOR, font=('SimSun', 14))
reset_button = tk.Button(main_window, text="Reset",width=10 , command=reset, bg=SECONDARY_COLOR, fg=BG_COLOR, font=('SimSun', 14))

main_window.mainloop()
