from dataclasses import dataclass

@dataclass
class CalendarioConfig:
    tamanho: int = 20
<<<<<<< HEAD
    height: int = 205
    width: int = 250
=======
    padding: int = 8
    height: int = 305
    width: int = 250
    spacing_week: int = 5
    margin: int = 10
    divider_spacing: int = 20
>>>>>>> trabalho-temporario
    border_color: str = "black"
    border_radius: int = 10
    header_color: str = "#BB86FC"
    day_color: str = "#121212"
    day_bg_color: str = "#1F1F1F"