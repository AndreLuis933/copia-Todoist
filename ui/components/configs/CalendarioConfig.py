from dataclasses import dataclass

@dataclass
class CalendarioConfig:
    height_container: int = 25
    width_container: int = 20
    size_text_header: int = 16
    padding: int = 8
    height: int = 305
    width: int = 250
    spacing_week: int = 5
    margin: int = 10
    divider_spacing: int = 20
    border_color: str = "black"
    border_radius: int = 10
    header_color: str = "#BB86FC"
    day_color: str = "#121212"
    day_bg_color: str = "#1F1F1F"