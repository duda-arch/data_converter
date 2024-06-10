from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

from classConverions import Conversions


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/home/duda-arch/Área de trabalho/duda-arch/data_converter/assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("data_converter")
window.geometry("809x397")
window.configure(bg = "#E3EBF0")


textValues = [Conversions.HEX_TWO_ASCII,
              Conversions.FLOAT_BIG_ENDIAN_ABCD,
              Conversions.FLOAT_LITTLE_ENDIAN_DCBA,
              Conversions.INT16_BIG_ENDIAN_AB,
              Conversions.INT32_BIG_ENDIAN_ABCD,
              Conversions.STRING_TWO_HEX,
              Conversions.HEX_TWO_STRING,
              ]


def changeValue():
    input_value = entry_1.get()
    for textIndiceItem in range(len(TextList)):
        if(len(input_value) <= 0):
            canvas.itemconfig(TextList[textIndiceItem], text="waiting for value")
        else:
            canvas.itemconfig(TextList[textIndiceItem], text=textValues[textIndiceItem](input_value))

canvas = Canvas(
    window,
    bg = "#E3EBF0",
    height = 397,
    width = 809,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: changeValue(),
    relief="flat"
)
button_1.place(
    x=460.0,
    y=43.0,
    width=131.0,
    height=40.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    relief="flat"
)
button_2.place(
    x=20.0,
    y=111.0,
    width=192.0,
    height=32.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    relief="flat"
)
button_4.place(
    x=20.0,
    y=150.0,
    width=192.0,
    height=32.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    relief="flat"
)
button_5.place(
    x=20.0,
    y=189.0,
    width=192.0,
    height=32.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    relief="flat"
)
button_6.place(
    x=20.0,
    y=227.0,
    width=192.0,
    height=32.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    relief="flat"
)
button_7.place(
    x=20.0,
    y=341.0,
    width=192.0,
    height=32.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    relief="flat"
)
button_8.place(
    x=20.0,
    y=266.0,
    width=192.0,
    height=68.0
)


entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    220.0,
    66.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#E4CCFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.insert(0,"enther the value")
entry_1.bind("<FocusIn>", lambda args: entry_1.delete('0', 'end'))
entry_1.place(
    x=28.0,
    y=50.0,
    width=384.0,
    height=31.0
)


TextList = [
            
            canvas.create_text(224.0,
                114.0,
                anchor="nw",
                text=" ",
                fill="#000000",
                font=("Inter SemiBoldItalic", 13 * -1)
            ),
            canvas.create_text(224.0,
                157.0,
                anchor="nw",
                text=" ",
                fill="#000000",
                font=("Inter SemiBoldItalic", 13 * -1)
            ),

            canvas.create_text(
                224.0,
                196.0,
                anchor="nw",
                text=" ",
                fill="#000000",
                font=("Inter SemiBoldItalic", 13 * -1)
            ),

            canvas.create_text(
                224.0,
                234.0,
                anchor="nw",
                text=" ",
                fill="#000000",
                font=("Inter SemiBoldItalic", 13 * -1)
            ),

            canvas.create_text(
                224.0,
                309.0,
                anchor="nw",
                text=" ",
                fill="#000000",
                font=("Inter SemiBoldItalic", 13 * -1)
            ),

            canvas.create_text(
                224.0,
                349.0,
                anchor="nw",
                text=" ",
                fill="#000000",
                font=("Inter SemiBoldItalic", 13 * -1)
            ),

            canvas.create_text(
                224.0,
                269.0,
                anchor="nw",
                text=" ",
                fill="#000000",
                font=("Inter SemiBoldItalic", 13 * -1)
            ),
        ]


window.resizable(False, False)
window.mainloop()
