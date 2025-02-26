import importlib
import inspect
import os
from flet import Container, Row, Column
from ui.components.utils.repr_personalized import ReprPersonalized

def apply_repr_to_ui_components():
    # Verificar se já foi executado
    if getattr(apply_repr_to_ui_components, 'has_run', False):
        return
    apply_repr_to_ui_components.has_run = True

    # Ajuste o caminho base para o diretório do projeto
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ui_path = os.path.join(base_path, 'ui')
    
    print(f"Procurando em: {ui_path}")

    for root, dirs, files in os.walk(ui_path):
        # Ignorar diretórios que não fazem parte do seu projeto
        dirs[:] = [d for d in dirs if d not in ['.venv', '.vscode', 'antigo', 'app']]
        
        for file in files:
            if file.endswith('.py') and not file.startswith('__'):
                module_path = os.path.relpath(os.path.join(root, file[:-3]), base_path).replace(os.sep, '.')
                
                print(f"Tentando importar: {module_path}")

                try:
                    module = importlib.import_module(module_path)
                    print(f"Módulo importado com sucesso: {module_path}")

                    for name, cls in inspect.getmembers(module, inspect.isclass):
                        if issubclass(cls, (Container, Row, Column)) and cls.__module__ == module.__name__:
                            if not hasattr(cls, '_repr_personalized'):
                                setattr(module, name, ReprPersonalized(cls))
                                cls._repr_personalized = True
                                print(f"ReprPersonalized aplicado a: {cls.__name__} no módulo {module.__name__}")

                except Exception as e:
                    print(f"Erro ao importar {module_path}: {str(e)}")

    print("Processo de aplicação do ReprPersonalized concluído.")

# Chame essa função no início da execução do projeto
apply_repr_to_ui_components