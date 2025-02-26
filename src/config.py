import sys
from flet import Container, Row, Column  # Importe todas as classes base relevantes do flet
from ui.components.utils.repr_personalized import ReprPersonalized

def apply_repr_to_flet_subclasses():
    flet_base_classes = (Container, Row, Column)  # Adicione outras classes base conforme necessário
    
    def wrapper(cls):
        if issubclass(cls, flet_base_classes) and cls not in flet_base_classes:
            return ReprPersonalized(cls)
        return cls

    class ReprFinder:
        def find_module(self, fullname, path=None):
            if fullname.startswith('ui.components'):  # Ajuste conforme a estrutura do seu projeto
                return self
            return None

        def load_module(self, fullname):
            if fullname in sys.modules:
                return sys.modules[fullname]
            
            module = __import__(fullname, fromlist=[''])
            for name, obj in list(module.__dict__.items):
                if isinstance(obj, type):
                    wrapped = wrapper(obj)
                    setattr(module, name, wrapped)
            
            return module

    sys.meta_path.insert(0, ReprFinder)

# Chame esta função no início da execução do seu programa
apply_repr_to_flet_subclasses()