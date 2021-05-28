def Processor(InputX, InputY, InputName):
    OutputText = format(InputX) + " " + format(InputY)
    X, Y = Math(InputX, InputY)
    Output(X, Y, InputName, OutputText)

def Math(InputX, InputY):
    X = 1418 + round(InputX/100)*2
    Y = 678 + round(InputY/100)*2
    return(X, Y)

def Output(X, Y, InputName, OutputText):   
    NWS = Image.open(resource_path("nws.png"))
    XImage = Image.open(resource_path("x.png"))
    OutImage = NWS.copy()
    OutImage.paste(XImage, (X, Y), XImage)
    WorkingImage = ImageDraw.Draw(OutImage)
    WorkingImage.text((15, 15), OutputText, (235, 64, 52), font=ImageFont.truetype(resource_path("playfair.ttf"), 100))
    OutImage.save(ProjectPath + InputName + ".png", quality=100)
    sg.PopupCancel("Image saved.")

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

#############################################

from PIL import Image, ImageFont, ImageDraw
import PySimpleGUI as sg
import os

#############################################

ProjectPath = os.path.join(os.environ["HOMEPATH"], "Desktop/")

layout = [
    [sg.Text("Enter full number including negative symbol")],
    [sg.Text("Target", size=(15, 1)), sg.InputText()],
    [sg.Text("First Number(X)", size=(15, 1)), sg.InputText()],
    [sg.Text("Second Number(Y", size=(15, 1)), sg.InputText()],
    [sg.Submit()]
]

window = sg.Window("New World Survey Maker",grab_anywhere = False).Layout(layout)

while True:
    button, value = window.Read()
    Name = value[0]
    X = value[1]
    Y = value[2]

    try:
        X = int(X)
        Y = int(Y)
        if not Name:
            Name = format(X) + "_" +format(Y)
        Processor(X, Y, Name)

    except:
        sg.PopupCancel("Please input proper X and Y values.")