from flet import *
from datetime import datetime, timedelta
import calendar
from ui.components.configs.CalendarioConfig import CalendarioConfig
<<<<<<< HEAD
=======
import locale


locale.setlocale(locale.LC_TIME, "pt_BR.UTF-8")
>>>>>>> trabalho-temporario


class Calendario(Container):
    def __init__(self, config: CalendarioConfig = CalendarioConfig()):
        super().__init__()
        self.current_date = datetime.now()
        self.months_loaded = 0
        self.is_loading = False
        self.config = config
        self.height = config.height
        self.width = config.width
<<<<<<< HEAD
        self.border = border.all(1, config.border_color)
        self.border_radius = config.border_radius
        self.content = ListView(
            expand=True,
            on_scroll=self.on_scroll,
        )

    def create_month_calendar(self, year, month):
        calendar.setfirstweekday(6)
        cal = calendar.monthcalendar(year, month)
        month_name = calendar.month_name[month]

        calendar_grid = Column(spacing=5)

        header = Row(
            [
                Text(
                    f"{month_name} {year}",
                    size=24,
                    weight=FontWeight.BOLD,
                    color=self.config.header_color,
                )
            ],
            alignment=MainAxisAlignment.CENTER,
        )
        calendar_grid.controls.append(header)

        days_of_week = Row(
=======
        self.padding = padding.only(left=config.padding, right=config.padding)
        #self.border = border.all(1, config.border_color)
        #self.border_radius = config.border_radius
        #self.bgcolor = "#1E1E1E"
        self.list = ListView(
            expand=True,
            on_scroll=self.on_scroll,
        )
        self.visible_month = self.current_date
        self.current_month_text = Container(
            content=self.header(self.visible_month.month, self.visible_month.year),
            padding=padding.only(left=10),
        )
        self.scroll_position = 0
        self.month_positions = [0]
        self.content = self.build()

    def build(self):
        return Column(
            spacing=5,
            expand=True,
            controls=[
                Column(
                    [
                        Row(
                            [
                                self.current_month_text,
                                Container(width=0, expand=True),
                                Row(
                                    [
                                        self.movimentacion_icons(
                                            Icons.KEYBOARD_ARROW_LEFT,
                                            disabled=True,
                                            opacity=0.1,
                                        ),
                                        self.movimentacion_icons(
                                            Icons.RADIO_BUTTON_UNCHECKED,
                                            lambda e: self.list.scroll_to(0),
                                            size=15,
                                            disabled=True,
                                            opacity=0.1,
                                        ),
                                        self.movimentacion_icons(
                                            Icons.KEYBOARD_ARROW_RIGHT,
                                            lambda e: self.list.scroll_to(self.month_positions[1]),
                                        ),
                                    ],
                                    # spacing=0,
                                ),
                            ],
                            alignment=MainAxisAlignment.SPACE_BETWEEN,
                        ),
                        self.days_of_week(),
                    ]
                ),
                self.list,
            ],
        )

    def movimentacion_icons(
        self, icon, position=None, disabled=False, opacity=1, size=20
    ):
        return Container(
            Icon(name=icon, size=size, color=Colors.WHITE),
            on_click=position,
            ink=True,
            disabled=disabled,
            opacity=opacity,
        )

    def is_current_day(self, year, month, day):
        return (
            year == self.current_date.year
            and month == self.current_date.month
            and day == self.current_date.day
        )

    def selecionar_data(self, e, month_name, year):
        dia = e.control.content.value
        print(f"{dia}/{month_name}/{year}")

    def header(self, month, ano=None):
        month_name = calendar.month_name[month].capitalize()[:3]
        return Text(
            f"{month_name} {ano if ano else ''}",
            size=24,
            weight=FontWeight.BOLD,
            color=self.config.header_color,
        )

    def days_of_week(self):
        return Row(
>>>>>>> trabalho-temporario
            [
                Container(
                    content=Text(day, size=14, color=self.config.day_color),
                    width=self.config.tamanho,
                    height=self.config.tamanho,
                    bgcolor=self.config.header_color,
                    border_radius=border_radius.all(5),
                    alignment=alignment.center,
                )
                for day in ["D", "S", "T", "Q", "Q", "S", "S"]
            ],
            alignment=MainAxisAlignment.CENTER,
        )
<<<<<<< HEAD
        calendar_grid.controls.append(days_of_week)
=======

    def create_month_calendar(self, year, month, start_day=1):
        calendar.setfirstweekday(6)
        cal = calendar.monthcalendar(year, month)

        calendar_grid = Column(spacing=self.config.spacing_week)
        semanas = 0
>>>>>>> trabalho-temporario

        for week in cal:
            week_row = Row(alignment=MainAxisAlignment.CENTER)
            for day in week:
<<<<<<< HEAD
                if day != 0:
                    week_row.controls.append(
                        Container(
                            content=Text(str(day), size=16, color="#E0E0E0"),
=======
                if day != 0 and day >= start_day:
                    is_current = self.is_current_day(year, month, day)
                    week_row.controls.append(
                        Container(
                            content=Text(
                                str(day),
                                size=16,
                                color="#E0E0E0" if not is_current else Colors.RED,
                            ),
                            width=self.config.tamanho,
                            height=self.config.tamanho,
                            bgcolor=self.config.day_bg_color,
                            border_radius=border_radius.all(5),
                            alignment=alignment.center,
                            on_click=lambda e: self.selecionar_data(e, month, year),
                        )
                    )
                elif day != 0:
                    week_row.controls.append(
                        Container(
                            content=Text(
                                str(day), size=16, color="#E0E0E0", opacity=0.5
                            ),
>>>>>>> trabalho-temporario
                            width=self.config.tamanho,
                            height=self.config.tamanho,
                            bgcolor=self.config.day_bg_color,
                            border_radius=border_radius.all(5),
                            alignment=alignment.center,
                        )
                    )
                else:
                    week_row.controls.append(
                        Container(width=self.config.tamanho, height=self.config.tamanho)
                    )
<<<<<<< HEAD
            calendar_grid.controls.append(week_row)

        return Container(
            content=calendar_grid,
            margin=margin.only(bottom=20),
            # padding=20,
            bgcolor="#1E1E1E",
            border_radius=border_radius.all(10),
            shadow=BoxShadow(
                spread_radius=1,
                blur_radius=10,
                color=Colors.BLACK54,
                offset=Offset(0, 0),
            ),
=======
            if any(day != 0 and day >= start_day for day in week):
                semanas += 1
                calendar_grid.controls.append(week_row)

        distancia = (
            semanas * self.config.tamanho
            + semanas * self.config.spacing_week
            + self.config.divider_spacing
            + self.config.margin
            + 24
            + 5
            + self.month_positions[-1]
        )
        self.month_positions.append(distancia)
        # print(self.month_positions)
        return Container(
            content=calendar_grid,
            margin=margin.only(bottom=self.config.margin),
            # padding=20,
            # bgcolor="#1E1E1E",
            # border_radius=border_radius.all(10),
            # shadow=BoxShadow(
            #     spread_radius=1,
            #     blur_radius=10,
            #     color=Colors.BLACK54,
            #     offset=Offset(0, 0),
            # ),
>>>>>>> trabalho-temporario
        )

    def load_more_months(self, count):
        new_months = []
        for _ in range(count):
            date = self.current_date + timedelta(days=30.44 * self.months_loaded)
            year, month = date.year, date.month
<<<<<<< HEAD
            month_calendar = self.create_month_calendar(year, month)
            new_months.append(month_calendar)
            self.months_loaded += 1
        self.content.controls.extend(new_months)

    def on_scroll(self, e: OnScrollEvent):
        self.is_loading
        if not self.is_loading and e.pixels >= e.max_scroll_extent - 100:
            self.is_loading = True
            self.load_more_months(1)
=======
            if year == self.current_date.year and month == self.current_date.month:
                month_calendar = self.create_month_calendar(
                    year, month, self.current_date.day
                )
            else:
                month_calendar = self.create_month_calendar(year, month)

                new_months.append(
                    Container(
                        self.header(month),
                        padding=padding.only(left=10),
                    )
                )
                new_months.append(Divider(height=self.config.divider_spacing))
            new_months.append(month_calendar)

            self.months_loaded += 1

        self.content.controls[1].controls.extend(new_months)

    def get_month_from_position(self, scroll_position):
        for i, position in enumerate(self.month_positions):
            if scroll_position < position:
                return i - 1 if i > 0 else 0
        return len(self.month_positions) - 1

    def adicionar_mais_meses(self):
        if self.scroll_position >= self.max_scroll_extent - 200:
            self.load_more_months(1)

    def update_header(self):
        new_visible_month = self.current_date + timedelta(
            days=30.44 * self.month_offset
        )
        if new_visible_month.month != self.visible_month.month:
            self.visible_month = new_visible_month
            self.current_month_text.content = self.header(
                self.visible_month.month, self.visible_month.year
            )

    def month_shortcut(self):
        shortcuts = self.content.controls[0].controls[0].controls[2].controls

        def disabled(shortcut):
            if self.month_offset:
                shortcut.disabled = False
                shortcut.opacity = 1
            else:
                shortcut.disabled = True
                shortcut.opacity = 0.1

        def create_scroll_function(offset):
            def scroll_to(e):
                if self.month_offset + offset >= 0:
                    Scroll = self.month_positions[self.month_offset + offset]
                    self.list.scroll_to(Scroll)

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
            self.month_offset = self.get_month_from_position(self.scroll_position)

            self.adicionar_mais_meses()
            self.update_header()
            self.month_shortcut()

>>>>>>> trabalho-temporario
            self.update()
            self.is_loading = False
