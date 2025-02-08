def high_light(e,before,after):
    if e.data == "true":
        e.control.bgcolor = after
    else:
        e.control.bgcolor = before
    e.control.update()

def default_high_light(e,before):
    e.control.bgcolor = before
    e.control.update()