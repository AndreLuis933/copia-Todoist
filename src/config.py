import importlib
import inspect
import os
from flet import Container, Row, Column

def ReprPersonalized(cls):
    original_str = cls.__str__
    original_repr = cls.__repr__

    def new_str(self):
        return f"{self.__class__.__name__} {original_str(self)}"

    def new_repr(self):
        return f"{self.__class__.__name__}({original_repr(self)})"

    cls.__str__ = new_str
    cls.__repr__ = new_repr
    return cls

def apply_repr_to_ui_components():
    """
    Função que percorre os módulos no diretório 'ui/components' e aplica o decorador
    ReprPersonalized a todas as classes que herdam de Container, Row ou Column.
    """
    print("Iniciando apply_repr_to_ui_components")
    
    # Ajuste o caminho base para o diretório do projeto
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    base_path = os.path.join(base_path,'src')
    components_path = os.path.join(base_path,'ui', 'components')
    
    print(f"Procurando em: {components_path}")

    # Imprime o conteúdo do diretório components_path para diagnóstico
    print(f"Conteúdo do diretório {components_path}:")
    try:
        for item in os.listdir(components_path):
            print(f"- {item}")
    except FileNotFoundError:
        print(f"Diretório {components_path} não encontrado.")
        return

    for root, dirs, files in os.walk(components_path):
        for file in files:
            if file.endswith('.py') and not file.startswith('__'):
                file_path = os.path.join(root, file)
                module_path = os.path.relpath(file_path, base_path).replace(os.sep, '.')[:-3]
                
                print(f"Tentando importar: {module_path}")

                try:
                    module = importlib.import_module(module_path)
                    print(f"Módulo importado com sucesso: {module_path}")

                    for name, cls in inspect.getmembers(module, inspect.isclass):
                        if issubclass(cls, (Container, Row, Column)) and cls.__module__ == module.__name__:
                            print(f"Classe encontrada: {cls.__name__} no módulo {module.__name__}")
                            decorated_cls = ReprPersonalized(cls)
                            setattr(module, name, decorated_cls)
                            print(f"ReprPersonalized aplicado a: {decorated_cls.__name__} no módulo {module.__name__}")
                        else:
                            if inspect.isclass(cls):
                                print(f"Classe {cls.__name__} não elegível para ReprPersonalized.")
                            else:
                                print(f"Membro {name} não é uma classe.")

                except Exception as e:
                    print(f"Erro ao importar {module_path}: {str(e)}")
                    print(f"Detalhes do erro: {e}")

    print("Processo de aplicação do ReprPersonalized concluído.")

