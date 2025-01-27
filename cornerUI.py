import pystray
import PIL.Image


image = PIL.Image.open("./images/logo.png")

def on_clicked(icon, item):
    if str(item) == "Exit":
        icon.stop()



icon = pystray.Icon("QuickCorners", image, menu=pystray.Menu(
    pystray.MenuItem("Exit", on_clicked),
))


icon.run()