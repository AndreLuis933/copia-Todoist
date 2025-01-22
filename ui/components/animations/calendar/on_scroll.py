from datetime import timedelta
from flet import OnScrollEvent

class OnScroll():
    def __init__(self, calendar):
        self.calendar = calendar
        self.scroll_position = 0
        self.is_loading = False

    def get_month_from_position(self, scroll_position):
        for i, position in enumerate(self.calendar.month_positions):
            if scroll_position < position:
                return i - 1 if i > 0 else 0
        return len(self.calendar.month_positions) - 1

    def adicionar_mais_meses(self):
        if self.scroll_position >= self.max_scroll_extent - 200:
            self.calendar.load_more_months(1)

    def update_header(self):
        new_visible_month = self.calendar.current_date + timedelta(
            days=30.44 * self.calendar.month_offset
        )
        if new_visible_month.month != self.calendar.visible_month.month:
            self.calendar.visible_month = new_visible_month
            self.calendar.current_month_text.content = self.calendar.header(
                self.calendar.visible_month.month, self.calendar.visible_month.year
            )

    def month_shortcut(self):
        shortcuts = self.calendar.content.controls[0].controls[0].controls[2].controls

        def disabled(shortcut):
            if self.calendar.month_offset:
                shortcut.disabled = False
                shortcut.opacity = 1
            else:
                shortcut.disabled = True
                shortcut.opacity = 0.1

        def create_scroll_function(offset):
            def scroll_to(e):
                if self.calendar.month_offset + offset >= 0:
                    Scroll = self.calendar.month_positions[self.calendar.month_offset + offset]
                    self.calendar.list.scroll_to(Scroll)

            return scroll_to

        shortcuts[0].on_click = create_scroll_function(-1)
        shortcuts[2].on_click = create_scroll_function(1)
        disabled(shortcuts[0])
        disabled(shortcuts[1])

    def on_scroll(self, e: OnScrollEvent):
        if not self.is_loading:
            self.is_loading = True
            self.scroll_position = int(e.pixels)
            self.max_scroll_extent = int(e.max_scroll_extent)
            self.calendar.month_offset = self.get_month_from_position(self.scroll_position)

            self.adicionar_mais_meses()
            self.update_header()
            self.month_shortcut()

            self.calendar.update()
            self.is_loading = False
