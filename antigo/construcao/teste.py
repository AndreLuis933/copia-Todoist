import flet as ft
from typing import List, Callable

# Model
class Task:
    def __init__(self, title: str, completed: bool = False):
        self.title = title
        self.completed = completed

class TaskList:
    def __init__(self):
        self.tasks: List[Task] = []
        self.observers: List[Callable] = []

    def add_task(self, task: Task):
        self.tasks.append(task)
        self.notify_observers()

    def toggle_task(self, index: int):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = not self.tasks[index].completed
            self.notify_observers()

    def add_observer(self, observer: Callable):
        self.observers.append(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer()

# View
class TaskView(ft.UserControl):
    def __init__(self, task: Task, on_toggle: Callable):
        super().__init__()
        self.task = task
        self.on_toggle = on_toggle

    def build(self):
        return ft.Checkbox(
            label=self.task.title,
            value=self.task.completed,
            on_change=lambda _: self.on_toggle()
        )

class TaskListView(ft.UserControl):
    def __init__(self, task_list: TaskList):
        super().__init__()
        self.task_list = task_list
        self.task_list.add_observer(self.update)

    def build(self):
        self.tasks_container = ft.Column()
        self.new_task_input = ft.TextField(hint_text="Add a new task")
        self.add_button = ft.ElevatedButton("Add", on_click=self.add_task)
        
        return ft.Column([
            ft.Text("Task List", size=20, weight="bold"),
            self.tasks_container,
            ft.Row([self.new_task_input, self.add_button])
        ])

    def update(self):
        self.tasks_container.controls = [
            TaskView(task, lambda task=task, index=i: self.task_list.toggle_task(index))
            for i, task in enumerate(self.task_list.tasks)
        ]
        self.update()

    def add_task(self, e):
        if self.new_task_input.value:
            self.task_list.add_task(Task(self.new_task_input.value))
            self.new_task_input.value = ""
            self.new_task_input.update()

# Controller
class TaskController:
    def __init__(self, task_list: TaskList):
        self.task_list = task_list

    def add_task(self, title: str):
        self.task_list.add_task(Task(title))

    def toggle_task(self, index: int):
        self.task_list.toggle_task(index)

# Main App
def main(page: ft.Page):
    page.title = "Task List App"
    
    task_list = TaskList()
    controller = TaskController(task_list)
    view = TaskListView(task_list)
    
    page.add(view)

ft.app(target=main)