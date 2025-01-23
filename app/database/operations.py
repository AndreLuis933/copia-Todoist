import os
from .setup import Session, Tarefa, ENGINE, Base


def database_exists():
    return os.path.exists(
        os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "TODO.db"
        )
    )


def create_tables():
    Base.metadata.create_all(ENGINE)


if not database_exists():
    print("Criando banco de dados...")
    create_tables()

