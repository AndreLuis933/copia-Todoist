from flet import *
from ..animations.high_light import high_light
from ..utils.card_manager import CardManager

class EFalsificado():
    data = None
    control = None

class Card_prioridade(Container):
    def __init__(self, controler):
        super().__init__()
        self.visible = False
        self.controler = controler
        self.padrao = 4
        self.controler.save.prioridade = self.padrao
        self.width = 150
        self.left = 350
        self.top = 170
        self.bgcolor = "#1E1E1E"
        self.border = border.all(0.5, Colors.OUTLINE)
        self.border_radius = border_radius.all(10)
        self.content = self.build()

    def select_priority(self, priority, e=None):
        if len(priority) == 2:
            priority = "p" + f'{self.padrao}'

        priority = int(priority[-1])
        self.update_select_priority(priority, e)



    def update_select_priority(self,priority, e=None):
        card = CardManager.get_current_card()

        for i in range(4):
            self.content.controls[i].content.controls[2].visible = False

        self.content.controls[priority - 1].content.controls[2].visible = True
        self.controler.save.prioridade = priority
        self.controler.hide_all()
        
        if not e:
            for i in self.content.controls:
                texto = i.content.controls[1].value[-1]
                if  texto== str(priority):
                    EFalsificado.control = i
                    EFalsificado.data = 'True'
                    e = EFalsificado
                    break

        if priority == 4:
            card.adicionar_prefixo(1, None)
            card.atualizar_definitions(1, "Prioridade")
        else:
            card.adicionar_prefixo(1, f"p{priority}", self.select_priority)
            card.atualizar_definitions(1, f"P{priority}",e.control.content.controls[0].color, self.select_priority)
        self.page.update()

    def cards_prioridade(self, icon, cor, texto, visible=False):
        return Container(
            content=Row(
                controls=[
                    Icon(icon, color=cor, size=22),
                    Text(texto, size=14),
                    Icon(Icons.CHECK, size=14, color=Colors.RED, visible=visible),
                ],
            ),
            padding=padding.symmetric(vertical=4, horizontal=8),
            height=40,
            on_click=lambda e: self.select_priority(texto, e),
            bgcolor="#272727",
            on_hover=lambda e: high_light(e,'#272727','#383838'),
        )

    def build(self):
        return Column(
            controls=[
                self.cards_prioridade(Icons.FLAG, Colors.RED, "Prioridade 1"),
                self.cards_prioridade(Icons.FLAG, Colors.ORANGE, "Prioridade 2"),
                self.cards_prioridade(Icons.FLAG, Colors.BLUE, "Prioridade 3"),
                self.cards_prioridade(
                    Icons.FLAG, Colors.GREY, "Prioridade 4", visible=True
                ),
            ],
            spacing=0,
        )
