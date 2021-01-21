##https://blog.furas.pl/python-tkinter-update-image-on-canvas-with-button-click-gb.html
import tkinter as tk
from PIL import ImageTk
from PIL import Image

#create Grey Image
img = Image.open("image.jpg")
width, height = img.width, img.height
for x in range(width):
    for y in range(height):
        r,g,b = img.getpixel( (x,y) )
        grey = int((r+g+b)/3)
        img.putpixel( (x,y), (grey,grey,grey) )
img.save("imageGrey.jpg")

imgGrey = Image.open("imageGrey.jpg")


#-- functions --

def toggle_grey():
    global current_image_number

    # next image
    current_image_number += 1

    # return to first image
    if current_image_number == len(images):
        current_image_number = 0

    # change image on canvas
    canvas.itemconfig(image_id, image=images[current_image_number])


def dispaly_details():
    if current_image_number==0:
        pixel5_10=img.getpixel( (5,10) )
    elif current_image_number==1:
        pixel5_10=imgGrey.getpixel( (5,10) )
    
    img_details= str(img.width) + "x" + str(img.height) + "     " +str(pixel5_10)
    label.config(text=img_details)
 

# --- main ---

root = tk.Tk()

# canvas for image
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# button to change image
button = tk.Button(root, text="Grey", command=toggle_grey)
button.pack()

button = tk.Button(root, text="Details", command=dispaly_details)
button.pack()

label = tk.Label(root, text="Click \"Details button\" for image details")
label.pack()

# images
images = [
    ImageTk.PhotoImage(file="image.jpg"),
    ImageTk.PhotoImage(file="imageGrey.jpg"),
]
current_image_number = 0

# set first image on canvas
image_id = canvas.create_image(0, 0, anchor='nw', image=images[current_image_number])

root.mainloop()
