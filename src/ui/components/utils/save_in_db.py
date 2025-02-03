from app.database.operations import salvar_tarefa


class SaveInDB:
    def __init__(self, controler):
        self.controler = controler
        self.title = None
        self.description = None
        self.vencimento = None
        self.data = None
        self.hora = None
        self.prioridade = None
        self.lembrete = []
        self.prazo = None
        self.local = None
        self.tag = None
        

    def save_clicked(self):
        values = [
            self.title,
            self.description,
            self.vencimento,
            self.prioridade,
            self.prazo,
            self.local,
            self.tag,
        ]

        salvar_tarefa(values,self.lembrete)

        self.controler.lista_tarefas.adicionar_tarefas()
        self.controler.page.update()
