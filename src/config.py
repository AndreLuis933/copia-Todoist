import importlib
import inspect
import os
import logging
from functools import lru_cache
from flet import Container, Row, Column

# Configuração do logging para um controle mais granular e flexível da saída de informações.
# Permite definir o nível de detalhe das mensagens (DEBUG, INFO, WARNING, ERROR, CRITICAL)
# e o formato da saída (data/hora, nível, mensagem).
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Conjunto (set) de classes base para uma verificação de herança mais rápida e eficiente.
# Usar um set permite verificações de pertencimento em tempo constante (O(1)),
# o que é mais rápido do que usar uma tupla ou lista para grandes quantidades de classes base.
BASE_CLASSES = {Container, Row, Column}

# Cache para armazenar módulos já importados, evitando reimportações desnecessárias.
# Reimportar módulos pode ser custoso em termos de tempo e recursos, especialmente
# se os módulos contêm muitas dependências ou realizam operações complexas na inicialização.
CACHED_MODULES = {}

def ReprPersonalized(cls):
    """
    Decorador que personaliza os métodos __str__ e __repr__ de uma classe.
    Adiciona o nome da classe à representação string e de debugging do objeto,
    facilitando a identificação e o rastreamento de instâncias durante o desenvolvimento.
    """
    # Verifica se o decorador já foi aplicado à classe.
    # Isso evita a aplicação múltipla do decorador, o que poderia levar a resultados inesperados
    # ou a um aumento desnecessário na complexidade do código.
    if hasattr(cls, '_repr_personalized'):
        return cls
    
    # Marca a classe como já decorada.
    # O atributo _repr_personalized é usado como um flag para indicar que o decorador já foi aplicado.
    # O nome do atributo começa com um underscore para indicar que é um atributo interno,
    # que não deve ser acessado diretamente fora da classe.
    cls._repr_personalized = True
    
    # Armazena os métodos originais.
    # Isso permite que o decorador chame os métodos __str__ e __repr__ originais da classe,
    # preservando o comportamento original da classe e adicionando apenas a personalização desejada.
    original_str = cls.__str__
    original_repr = cls.__repr__
    
    # Define novos métodos __str__ e __repr__ usando lambda functions.
    # Lambda functions são funções anônimas que podem ser definidas em uma única linha.
    # Elas são usadas aqui para criar funções que chamam os métodos originais e adicionam
    # o nome da classe à representação.
    # O uso de lambda functions evita a necessidade de definir funções separadas para cada classe,
    # tornando o código mais conciso e legível.
    cls.__str__ = lambda self: f"{self.__class__.__name__} {original_str(self)}"
    cls.__repr__ = lambda self: f"{self.__class__.__name__}({original_repr(self)})"
    
    return cls

@lru_cache(maxsize=None)
def get_module(module_path):
    """
    Importa e retorna um módulo. Usa lru_cache para memoização,
    evitando importações repetidas do mesmo módulo.
    """
    # Importa o módulo usando importlib.import_module.
    # Se o módulo já foi importado antes, o resultado será recuperado do cache lru_cache.
    # Caso contrário, o módulo será importado e o resultado será armazenado no cache.
    return importlib.import_module(module_path)

def is_eligible(cls, module):
    """
    Verifica se uma classe é elegível para aplicação do decorador ReprPersonalized.
    Uma classe é considerada elegível se:
        - Herda de Container, Row ou Column (ou qualquer outra classe definida em BASE_CLASSES).
        - É definida no mesmo módulo que está sendo processado.
        - Não foi decorada anteriormente com ReprPersonalized.
    """
    # Retorna True se a classe for elegível e False caso contrário.
    return (
        issubclass(cls, tuple(BASE_CLASSES)) and 
        cls.__module__ == module.__name__ and
        not hasattr(cls, '_repr_personalized')
    )

def apply_repr_to_ui_components():
    """
    Função que percorre os módulos no diretório 'ui/components' e aplica o decorador
    ReprPersonalized a todas as classes elegíveis.
    """
    # Registra o início do processo de aplicação do decorador.
    logger.info("Iniciando apply_repr_to_ui_components")
    
    # Ajuste o caminho base para o diretório do projeto.
    # Determina o caminho absoluto do diretório do script atual e sobe dois níveis
    # para encontrar o diretório base do projeto.
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    base_path = os.path.join(base_path, 'src')
    components_path = os.path.join(base_path, 'ui', 'components')
    
    # Registra o diretório onde os componentes estão sendo procurados.
    logger.debug(f"Procurando em: {components_path}")

    # Verifica se o diretório existe e lista seu conteúdo.
    # Isso ajuda a verificar se o caminho para o diretório de componentes está correto
    # e se os arquivos estão presentes.
    try:
        logger.debug(f"Conteúdo do diretório {components_path}:")
        for item in os.listdir(components_path):
            logger.debug(f"- {item}")
    except FileNotFoundError:
        logger.error(f"Diretório {components_path} não encontrado.")
        return

    # Percorre recursivamente o diretório de componentes.
    # O os.walk gera os nomes dos arquivos em cada diretório da árvore,
    # começando do diretório raiz especificado.
    for root, dirs, files in os.walk(components_path):
        for file in files:
            # Processa apenas arquivos Python que não são especiais.
            # Arquivos que começam com '__' são geralmente arquivos especiais do Python,
            # como __init__.py, que não precisam ser processados.
            if file.endswith('.py') and not file.startswith('__'):
                file_path = os.path.join(root, file)
                module_path = os.path.relpath(file_path, base_path).replace(os.sep, '.')[:-3]
                
                # Registra o módulo que está sendo importado.
                logger.debug(f"Tentando importar: {module_path}")

                try:
                    # Usa o cache de módulos para evitar reimportações.
                    # Se o módulo já foi importado antes, ele será recuperado do cache.
                    # Caso contrário, ele será importado e armazenado no cache.
                    if module_path in CACHED_MODULES:
                        module = CACHED_MODULES[module_path]
                    else:
                        module = get_module(module_path)
                        CACHED_MODULES[module_path] = module

                    # Registra o sucesso da importação do módulo.
                    logger.info(f"Módulo importado com sucesso: {module_path}")

                    # Itera sobre os membros do módulo.
                    # O inspect.getmembers retorna todos os membros de um objeto (neste caso, um módulo),
                    # filtrando apenas as classes.
                    for name, cls in inspect.getmembers(module, inspect.isclass):
                        # Verifica se a classe é elegível para receber o decorador.
                        if is_eligible(cls, module):
                            # Registra a classe elegível encontrada.
                            logger.info(f"Classe elegível encontrada: {cls.__name__} no módulo {module.__name__}")
                            # Aplica o decorador à classe.
                            decorated_cls = ReprPersonalized(cls)
                            # Substitui a classe original pela classe decorada no módulo.
                            setattr(module, name, decorated_cls)
                            # Registra a aplicação do decorador.
                            logger.info(f"ReprPersonalized aplicado a: {decorated_cls.__name__} no módulo {module.__name__}")
                        else:
                            # Registra que a classe não é elegível.
                            if inspect.isclass(cls):
                                logger.debug(f"Classe {cls.__name__} não elegível para ReprPersonalized.")
                            else:
                                logger.debug(f"Membro {name} não é uma classe.")

                # Trata erros de importação.
                except ImportError as e:
                    logger.warning(f"Erro ao importar {module_path}: {e}")
                # Trata outros erros inesperados.
                except Exception as e:
                    logger.error(f"Erro inesperado ao processar {module_path}: {e}", exc_info=True)

    # Registra o fim do processo de aplicação do decorador.
    logger.info("Processo de aplicação do ReprPersonalized concluído.")

