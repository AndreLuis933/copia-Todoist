from flet import *
from datetime import datetime, timedelta
import calendar


class Calendario(Container):
    def __init__(self):
        super().__init__()
        self.current_date = datetime.now()
        self.months_loaded = 0
        self.is_loading = False
        self.tamanho = 20
        self.height = 205
        self.width = 250
        self.border = border.all(1, Colors.BLACK)
        self.border_radius = 10
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
                    color="#BB86FC",
                )
            ],
            alignment=MainAxisAlignment.CENTER,
        )
        calendar_grid.controls.append(header)

        days_of_week = Row(
            [
                Container(
                    content=Text(day, size=14, color="#121212"),
                    width=self.tamanho,
                    height=self.tamanho,
                    bgcolor="#BB86FC",
                    border_radius=border_radius.all(5),
                    alignment=alignment.center,
                )
                for day in ["D", "S", "T", "Q", "Q", "S", "S"]
            ],
            alignment=MainAxisAlignment.CENTER,
        )
        calendar_grid.controls.append(days_of_week)

        for week in cal:
            week_row = Row(alignment=MainAxisAlignment.CENTER)
            for day in week:
                if day != 0:
                    week_row.controls.append(
                        Container(
                            content=Text(str(day), size=16, color="#E0E0E0"),
                            width=self.tamanho,
                            height=self.tamanho,
                            bgcolor="#1F1F1F",
                            border_radius=border_radius.all(5),
                            alignment=alignment.center,
                        )
                    )
                else:
                    week_row.controls.append(
                        Container(width=self.tamanho, height=self.tamanho)
                    )
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
        )

    def load_more_months(self, count):
        new_months = []
        for _ in range(count):
            date = self.current_date + timedelta(days=30.44 * self.months_loaded)
            year, month = date.year, date.month
            month_calendar = self.create_month_calendar(year, month)
            new_months.append(month_calendar)
            self.months_loaded += 1
        self.content.controls.extend(new_months)

    def on_scroll(self, e: OnScrollEvent):
        self.is_loading
        if not self.is_loading and e.pixels >= e.max_scroll_extent - 100:
            self.is_loading = True
            self.load_more_months(1)
            self.update()
            self.is_loading = False
