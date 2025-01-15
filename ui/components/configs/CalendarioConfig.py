from dataclasses import dataclass

@dataclass
class CalendarioConfig:
    tamanho: int = 20
    height: int = 205
    width: int = 250
    border_color: str = "black"
    border_radius: int = 10