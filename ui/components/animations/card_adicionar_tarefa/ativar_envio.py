from flet import Colors

class AtivarEnvio():
    def __init__(self, card):
        self.card = card

    def ativar_envio(self, e):
        botao = self.card.content.controls[3].controls[1]
        if e.data:
            botao.opacity = 1
            botao.bgcolor = Colors.RED
            botao.disabled = False
            botao.update()
        else:
            botao.opacity = 0.3
            botao.bgdcolor = Colors.RED_900
            botao.disabled = True
            botao.update()
