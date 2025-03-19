import importlib
import inspect
import logging
import os

from flet import Column, Container, Row

logging.basicConfig(level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

BASE_CLASSES = {Container, Row, Column}


def repr_personalized(cls):
    """Decorador que personaliza os métodos __str__ e __repr__ de uma classe Flet."""
    if hasattr(cls, "_repr_personalized"):
        return cls

    cls._repr_personalized = True
    original_str = cls.__str__

    cls.__str__ = lambda self: f"{self.__class__.__name__} {original_str(self)}"

    return cls


def get_module(module_path):
    """Importa e retorna um módulo usando importlib."""
    try:
        return importlib.import_module(module_path)
    except ImportError as e:
        logger.error(f"Falha ao importar módulo {module_path}: {e}")
        return None


def is_eligible(cls, module):
    """Verifica se uma classe é elegível para o decorador repr_personalized."""
    return (
        issubclass(cls, tuple(BASE_CLASSES))
        and cls.__module__ == module.__name__
        and not hasattr(cls, "_repr_personalized")
    )


def apply_repr_to_ui_components():
    """Aplica o decorador repr_personalized a classes elegíveis nos módulos de UI."""
    logger.info("Iniciando apply_repr_to_ui_components")

    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    base_path = os.path.join(base_path, "src")
    components_path = os.path.join(base_path, "ui")

    logger.debug(f"Procurando em: {components_path}")

    try:
        logger.debug(f"Conteúdo do diretório {components_path}:")
        for item in os.listdir(components_path):
            logger.debug(f"- {item}")
    except FileNotFoundError:
        logger.error(f"Diretório {components_path} não encontrado.")
        return

    for root, dirs, files in os.walk(components_path):
        for file in files:
            if file.endswith(".py") and not file.startswith("__"):
                file_path = os.path.join(root, file)
                module_path = os.path.relpath(file_path, base_path).replace(os.sep, ".")[:-3]

                logger.debug(f"Tentando importar: {module_path}")

                module = get_module(module_path)
                if module:
                    logger.info(f"Módulo importado com sucesso: {module_path}")

                    for name, cls in inspect.getmembers(module, inspect.isclass):
                        if is_eligible(cls, module):
                            logger.info(f"Classe elegível encontrada: {cls.__name__} no módulo {module.__name__}")
                            decorated_cls = repr_personalized(cls)
                            setattr(module, name, decorated_cls)
                            logger.info(
                                f"repr_personalized aplicado a: {decorated_cls.__name__} no módulo {module.__name__}"
                            )
                        elif inspect.isclass(cls):
                            logger.debug(f"Classe {cls.__name__} não elegível para repr_personalized.")

    logger.info("Processo de aplicação do repr_personalized concluído.")


apply_repr_to_ui_components()
