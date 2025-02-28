from app.database.operations import salvar_tarefa, save_projetc,update_task_db


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
        self.completa = False
        self.edit = None
        

    def save_task(self):
        values = [
            self.title,
            self.description,
            self.vencimento,
            self.prioridade,
            self.prazo,
            self.local,
            self.tag,
            self.completa,
        ]

        salvar_tarefa(values,self.lembrete)

        self.controler.lista_tarefas.adicionar_tarefas()
        self.controler.page.update()
    
    def update_task(self):
        values = [
            self.edit,
            self.title,
            self.description,
            self.vencimento,
            self.prioridade,
            self.prazo,
            self.local,
            self.tag,
            self.completa,
        ]
        update_task_db(values, self.lembrete)
        self.controler.lista_tarefas.adicionar_tarefas()
        self.controler.page.update()

    def save_projetc(self,projetos):
        
        save_projetc(projetos)
        pass