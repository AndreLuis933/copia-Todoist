import inspect
from flet import Container
from ui.components.utils.repr_personalized import ReprPersonalized

def apply_repr_to_container_subclasses(module):
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj) and issubclass(obj, Container) and obj != Container:
            setattr(module, name, ReprPersonalized(obj))