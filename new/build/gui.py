from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog
from moviepy.editor import *
from tkinter.filedialog import askopenfilename
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\ASUS\Desktop\new\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("Video Editing App")
window.geometry("360x800")







canvas = Canvas(
    window,
    height = 800,
    width = 360,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
x_position = 200
y_position = 100
video_position = (x_position, y_position)

def import_video():
    file_path = askopenfilename()

    # Load the video clip
    video_clip = VideoFileClip(file_path)

    # Set the position of the video clip on the black clip
    video_clip = video_clip.set_position(video_position)

    # Add the video clip to the composite clip
    global composite_clip
    composite_clip = CompositeVideoClip([video_clip])

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    360.0,
    800.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    0.0,
    433.0,
    360.0,
    497.0,
    fill="#2C2C2C",
    outline="")





canvas.create_rectangle(
    0.0,
    49.0,
    360.0,
    385.0,
    fill="#333333",
    outline="")

canvas.create_rectangle(
    0.0,
    497.0,
    360.0,
    565.0,
    fill="#191919",
    outline="")

canvas.create_rectangle(
    0.0,
    635.0,
    360.0,
    712.0,
    fill="#191919",
    outline="")

canvas.create_rectangle(
    0.0,
    566.0,
    360.0,
    635.0,
    fill="#262626",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    command=lambda: print("button_1 clicked"),
    relief="flat",
    bg="#191919"
)

button_1.place(
    x=15.0,
    y=506.0,
    width=48.0,
    height=46.22222900390625
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat",
    bg="#000000"
)
button_2.place(
    x=312.0,
    y=1.0,
    width=48.0,
    height=48.0
)

    
button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=import_video,
    relief="flat",
     bg="#000000"
    
)

button_3.place(
    x=2.0,
    y=1.0,
    width=48.0,
    height=48.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat",
     bg="#000000"
)
button_4.place(
    x=233.0,
    y=385.0,
    width=48.0,
    height=48.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat",
     bg="#000000"
)
button_5.place(
    x=305.0,
    y=385.0,
    width=48.0,
    height=48.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat",
     bg="#000000"
)
button_6.place(
    x=151.0,
    y=736.0,
    width=48.0,
    height=48.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat",
     bg="#000000"
)
button_7.place(
    x=86.0,
    y=736.0,
    width=48.0,
    height=48.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat",
     bg="#000000"
)
button_8.place(
    x=31.0,
    y=736.0,
    width=48.0,
    height=48.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_9 clicked"),
    relief="flat",
     bg="#000000"
)
button_9.place(
    x=216.0,
    y=736.0,
    width=48.0,
    height=48.0
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_10 clicked"),
    relief="flat",
     bg="#000000"
)
button_10.place(
    x=281.0,
    y=737.0,
    width=48.0,
    height=48.0
)

button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_11 clicked"),
     bg="#333333"
)
button_11.place(
    x=15.0,
    y=441.0,
    width=48.0,
    height=48.0,
    
)

button_image_12 = PhotoImage(
    file=relative_to_assets("button_12.png"))
button_12 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_12 clicked"),
     bg="#000000"
)
button_12.place(
    x=15.0,
    y=384.0,
    width=48.0,
    height=48.0
)

button_image_13 = PhotoImage(
    file=relative_to_assets("button_13.png"))
button_13 = Button(
    image=button_image_13,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_13 clicked"),
    relief="flat",
     bg="#000000"
)
button_13.place(
    x=67.0,
    y=384.0,
    width=48.0,
    height=48.0
)
window.resizable(False, False)
window.mainloop()
