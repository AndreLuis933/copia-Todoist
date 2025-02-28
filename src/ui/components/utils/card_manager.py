from __future__ import annotations

class CardManager:
    instance: CardManager
    _current_card = None

    def __new__(cls) -> CardManager:
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

    @classmethod
    def set_current_card(cls, card):
        cls._current_card = card

    @classmethod
    def get_current_card(cls):
        return cls._current_card
