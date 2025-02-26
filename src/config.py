import importlib
import inspect
import os
from flet import Container, Row, Column # Adicionei UserControl
from ui.components.utils.repr_personalized import ReprPersonalized

def apply_repr_to_ui_components():
    base_path = os.path.join(os.path.dirname(__file__), "components")
    package = "ui.components"
    
    print(f"Procurando em: {base_path}")

    # Verificar se o diretório existe
    if not os.path.exists(base_path):
        print(f"O diretório {base_path} não existe!")
        return

    # Listar todos os arquivos e diretórios
    print("Conteúdo do diretório:")
    for item in os.listdir(base_path):
        print(f" - {item}")

    for root, dirs, files in os.walk(base_path):
        print(f"Explorando diretório: {root}")
        print(f"Arquivos encontrados: {files}")
        
        for file in files:
            if file.endswith(".py") and not file.startswith("__"):
                module_path = os.path.relpath(os.path.join(root, file), base_path) \
                                .replace(os.sep, ".") \
                                .replace(".py", "")
                
                full_module_name = f"{package}.{module_path}"
                print(f"Tentando importar: {full_module_name}")

                try:
                    module = importlib.import_module(full_module_name)
                    print(f"Módulo importado com sucesso: {full_module_name}")

                    for name, cls in inspect.getmembers(module, inspect.isclass):
                        if issubclass(cls, (Container, Row, Column)) and cls.__module__ == full_module_name:
                            setattr(module, name, ReprPersonalized(cls))
                            print(f"ReprPersonalized aplicado a: {cls.__name__} no módulo {module.__name__}")
                        else:
                            print(f"Classe não elegível: {cls.__name__} no módulo {module.__name__}")
                except Exception as e:
                    print(f"Erro ao importar {full_module_name}: {str(e)}")

    print("Processo de aplicação do ReprPersonalized concluído.")
apply_repr_to_ui_components()