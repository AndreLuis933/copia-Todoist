from flet import *
from datetime import datetime, timedelta
import calendar
from ..configs.CalendarioConfig import CalendarioConfig
from ..animations.calendar.on_scroll import OnScroll
from dateutil.relativedelta import relativedelta

class Calendario(Container):
    def __init__(self, controler, config: CalendarioConfig = CalendarioConfig()):
        super().__init__()
        self.current_date = datetime.now()
        self.controler = controler
        self.on_scroll = OnScroll(self)
        self.months_loaded = 0
        self.highlighted_day = None
        self.current_day = False
        self.config = config
        self.height = config.height
        self.width = config.width
        self.padding = padding.only(left=config.padding, right=config.padding)
        self.list = ListView(expand=True, on_scroll=self.on_scroll.on_scroll)
        self.visible_month = self.current_date
        self.current_month_text = Container(
            content=self.header(self.visible_month.month, self.visible_month.year),
            padding=padding.only(left=10),
        )
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
                                            lambda e: self.list.scroll_to(
                                                self.month_positions[1]
                                            ),
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

    def selecionar_data(self, e, month, year):
        dia = e.control.content.value
        data_datetime = datetime.strptime(f"{dia}/{month}/{year}", "%d/%m/%Y")

        self.salvar_data(data_datetime)

    def salvar_data(self, data):
        if not isinstance(data, datetime):
            self.controler.save.vencimento = None
            self.remover_destaque()
        else:
            atual = self.controler.save.vencimento

            data = data.replace(hour=0, minute=0, second=0, microsecond=0)
            if atual:
                data = datetime.combine(data.date(), atual.time())

            self.controler.save.vencimento = data
            self.controler.save.data = data.date()
            self.buscar_data(data)
        self.controler.hide_all()
        self.controler.tarefa.update_text()

    def localizar_data(self, data_alvo):
        ano_alvo, mes_alvo, dia_alvo = data_alvo.year, data_alvo.month, data_alvo.day

        # Verifica se o mês alvo já está carregado
        meses_necessarios = (
            (ano_alvo - self.current_date.year) * 12
            + mes_alvo
            - self.current_date.month
        )
        if meses_necessarios > self.months_loaded:
            self.load_more_months(meses_necessarios - self.months_loaded)

        mes_atual = self.current_date.month
        ano_atual = self.current_date.year

        for container in self.list.controls:
            if isinstance(container, Container) and isinstance(
                container.content, Column
            ):
                if ano_atual == ano_alvo and mes_atual == mes_alvo:
                    dia_encontrado = self.procurar_dia_no_mes(container, dia_alvo)
                    if dia_encontrado:
                        return True

                mes_atual += 1
                if mes_atual > 12:
                    mes_atual = 1
                    ano_atual += 1

        return False

    def procurar_dia_no_mes(self, container, dia_alvo):
        for week_row in container.content.controls:
            for day_container in week_row.controls:
                if isinstance(day_container, Container) and isinstance(
                    day_container.content, Text
                ):
                    try:
                        dia = int(day_container.content.value)
                        if dia == dia_alvo:
                            self.destacar_dia(day_container)
                            return True
                    except ValueError:
                        print("Erro ao converter dia para int")
                        continue
        return False

    def destacar_dia(self, day_container):
        if self.highlighted_day:
            self.remover_destaque()

        self.current_day = True if day_container.content.color == Colors.RED else False
        day_container.bgcolor = Colors.RED
        day_container.content.color = Colors.WHITE
        day_container.content.weight = FontWeight.BOLD
        self.highlighted_day = day_container

    def remover_destaque(self):
        if self.highlighted_day:
            self.highlighted_day.bgcolor = None
            self.highlighted_day.content.weight = FontWeight.NORMAL
            self.highlighted_day.content.color = (
                "#E0E0E0" if not self.current_day else Colors.RED
            )
            self.highlighted_day = None

    def buscar_data(self, data):
        self.remover_destaque()
        self.localizar_data(data)
        self.update()

    def header(self, month, ano=None):
        month_name = calendar.month_name[month].capitalize()[:3]
        return Text(
            f"{month_name} {ano if ano else ''}",
            size=self.config.size_text_header,
            weight=FontWeight.BOLD,
        )

    def days_of_week(self):
        return Column(
            [
                Row(
                    [
                        Container(
                            content=Text(
                                day, size=12, color=Colors.WHITE54, weight="w650"
                            ),
                            width=self.config.height_container,
                            height=self.config.height_container,
                            border_radius=border_radius.all(5),
                            alignment=alignment.center,
                        )
                        for day in ["D", "S", "T", "Q", "Q", "S", "S"]
                    ],
                    alignment=MainAxisAlignment.CENTER,
                    spacing=5,
                ),
                Divider(height=1),
            ],
            spacing=5,
        )

    def create_month_calendar(self, year, month, start_day=1):
        calendar.setfirstweekday(6)
        cal = calendar.monthcalendar(year, month)

        calendar_grid = Column(spacing=self.config.spacing_week)
        semanas = 0

        for week in cal:
            week_row = Row(alignment=MainAxisAlignment.CENTER, spacing=5)
            for day in week:
                if day != 0 and day >= start_day:
                    is_current = self.is_current_day(year, month, day)
                    week_row.controls.append(
                        Container(
                            content=Text(
                                str(day),
                                text_align=TextAlign.START,
                                size=14,
                                color="#E0E0E0" if not is_current else Colors.RED,
                            ),
                            width=self.config.height_container,
                            height=self.config.height_container,
                            border_radius=border_radius.all(15),
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
                            width=self.config.height_container,
                            height=self.config.height_container,
                            border_radius=border_radius.all(15),
                            alignment=alignment.center,
                        )
                    )
                else:
                    week_row.controls.append(
                        Container(
                            width=self.config.height_container,
                            height=self.config.height_container,
                        )
                    )
            if any(day != 0 and day >= start_day for day in week):
                semanas += 1
                calendar_grid.controls.append(week_row)

        distancia = (
            semanas * self.config.height_container
            + semanas * self.config.spacing_week
            + self.config.divider_spacing
            + self.config.margin
            + self.config.size_text_header
            + 2
            + self.month_positions[-1]
        )
        self.month_positions.append(distancia)
        return Container(
            content=calendar_grid,
            margin=margin.only(bottom=self.config.margin),
        )

    def load_more_months(self, count):
        new_months = []
        for _ in range(count):
            date = self.current_date + relativedelta(months=self.months_loaded)
            year, month = date.year, date.month
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
