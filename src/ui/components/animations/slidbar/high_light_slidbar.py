def HighLight(e):
    if e.data == "true":
        e.control.bgcolor = "white10"
        e.control.update()

        e.control.content.controls[0].icon_color = "white"
        e.control.content.controls[1].color = "white"
        e.control.content.update()

    else:
        e.control.bgcolor = None
        e.control.update()

        e.control.content.controls[0].icon_color = "white54"
        e.control.content.controls[1].color = "white54"
        e.control.content.update()