import importlib
import inspect
import os
from flet import Container, Row, Column
from ui.components.utils.repr_personalized import ReprPersonalized

def apply_repr_to_ui_components():
    print("Iniciando apply_repr_to_ui_components")
    
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ui_path = os.path.join(base_path, 'ui')
    
    print(f"Procurando em: {ui_path}")
    print(f"Conteúdo do diretório ui:")
    for root, dirs, files in os.walk(ui_path):
        level = root.replace(ui_path, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print(f"{indent}{os.path.basename(root)}/")
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print(f"{subindent}{f}")

    for root, dirs, files in os.walk(ui_path):
        for file in files:
            if file.endswith('.py') and not file.startswith('__'):
                module_path = os.path.relpath(os.path.join(root, file[:-3]), base_path).replace(os.sep, '.')
                
                print(f"Tentando importar: {module_path}")

                try:
                    module = importlib.import_module(module_path)
                    print(f"Módulo importado com sucesso: {module_path}")

                    for name, cls in inspect.getmembers(module, inspect.isclass):
                        if inspect.isclass(cls) and issubclass(cls, (Container, Row, Column)) and cls.__module__ == module.__name__:
                            print(f"Classe encontrada: {cls.__name__} no módulo {module.__name__}")
                            decorated_cls = ReprPersonalized(cls)
                            setattr(module, name, decorated_cls)
                            print(f"ReprPersonalized aplicado a: {decorated_cls.__name__} no módulo {module.__name__}")
                        else:
                            if inspect.isclass(cls):
                                print(f"Classe não elegível: {cls.__name__} no módulo {module.__name__} (não herda de Container, Row, Column ou UserControl, ou __module__ diferente)")
                            else:
                                print(f"Membro não é uma classe: {name} no módulo {module.__name__}")

                except Exception as e:
                    print(f"Erro ao importar {module_path}: {str(e)}")

    print("Processo de aplicação do ReprPersonalized concluído.")

# Chame essa função no início da execução do projeto
apply_repr_to_ui_components()