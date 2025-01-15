from dataclasses import dataclass

@dataclass
class CalendarioConfig:
    tamanho: int = 20
    height: int = 205
    width: int = 250
    border_color: str = "black"
    border_radius: int = 10
    header_color: str = "#BB86FC"
    day_color: str = "#121212"
    day_bg_color: str = "#1F1F1F"